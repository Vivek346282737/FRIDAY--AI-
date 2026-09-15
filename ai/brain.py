import json
import re

from ai.llm import llm
from ai.prompts import prompts
from ai.planner import planner
from ai.reasoner import reasoner

from vision.screen_analyzer import screen


class Brain:

    def __init__(self):

        self.max_context = 5

    # =====================================================
    # BUILD PROMPT
    # =====================================================

    def build_prompt(
        self,
        message: str,
        memory: str = "",
        conversation: str = ""
    ):

        try:

            plan = planner.create_plan(
                message
            )

            planner_summary = (
                planner.summary(
                    plan
                )
            )

            rag_context = (
                planner.format_context(
                    plan
                )
            )

        except Exception as e:

            planner_summary = (
                f"Planner unavailable: {e}"
            )

            rag_context = ""

        try:

            reasoning = reasoner.summarize(
                reasoner.analyze(
                    plan
                    if "plan" in locals()
                    else {}
                )
            )

        except Exception as e:

            reasoning = (
                f"Reasoner unavailable: {e}"
            )

        try:

            screen_info = screen.summary()

        except Exception as e:

            screen_info = (
                f"Vision unavailable: {e}"
            )

        system_prompt = f"""
{prompts.SYSTEM}

====================================================
MEMORY
====================================================

{prompts.MEMORY.format(memory=memory)}

====================================================
CONVERSATION
====================================================

{prompts.CONVERSATION.format(conversation=conversation)}

====================================================
PLANNER
====================================================

{planner_summary}

====================================================
REASONER
====================================================

{reasoning}

====================================================
PROJECT CONTEXT
====================================================

{rag_context}

====================================================
VISION
====================================================

{screen_info}

====================================================
EXECUTION
====================================================

{prompts.EXECUTOR}
"""

        return [

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content": message
            }

        ]

    # =====================================================
    # EXTRACT JSON
    # =====================================================

    def _extract_json(
        self,
        response
    ):

        if isinstance(
            response,
            dict
        ):

            return response

        if response is None:

            return None

        text = str(
            response
        ).strip()

        text = re.sub(
            r"^```(?:json)?",
            "",
            text,
            flags=re.IGNORECASE
        )

        text = re.sub(
            r"```$",
            "",
            text
        )

        text = text.strip()

        try:

            return json.loads(
                text
            )

        except Exception:
            pass

        start = text.find(
            "{"
        )

        end = text.rfind(
            "}"
        )

        if (
            start != -1
            and end != -1
            and end > start
        ):

            candidate = text[
                start:end + 1
            ]

            try:

                return json.loads(
                    candidate
                )

            except Exception:
                pass

        return None

    # =====================================================
    # NORMALIZE RESPONSE
    # =====================================================

    def _normalize_response(
        self,
        data,
        original_text
    ):

        if not isinstance(
            data,
            dict
        ):

            return {

                "message": str(
                    original_text
                ).strip(),

                "action": None,

                "target": None,

                "actions": None
            }

        message = data.get(
            "message",
            ""
        )

        action = data.get(
            "action"
        )

        target = data.get(
            "target"
        )

        actions = data.get(
            "actions"
        )

        if action is not None:

            action = str(
                action
            ).upper().strip()

        if target is not None:

            target = str(
                target
            ).strip()

        if not isinstance(
            actions,
            list
        ):

            actions = None

        else:

            cleaned_actions = []

            for item in actions:

                if not isinstance(
                    item,
                    dict
                ):

                    continue

                cleaned = {}

                item_action = item.get(
                    "action"
                )

                if item_action:

                    cleaned[
                        "action"
                    ] = str(
                        item_action
                    ).upper().strip()

                if "target" in item:

                    cleaned[
                        "target"
                    ] = item.get(
                        "target"
                    )

                if "steps" in item:

                    cleaned[
                        "steps"
                    ] = item.get(
                        "steps"
                    )

                for key, value in item.items():

                    if key not in cleaned:

                        cleaned[
                            key
                        ] = value

                if cleaned.get(
                    "action"
                ):

                    cleaned_actions.append(
                        cleaned
                    )

            actions = cleaned_actions

        if actions:

            action = None
            target = None

        return {

            "message": str(
                message
            ).strip(),

            "action": action,

            "target": target,

            "actions": actions
        }

    # =====================================================
    # PARSE RESPONSE
    # =====================================================

    def parse_response(
        self,
        response
    ):

        data = self._extract_json(
            response
        )

        return self._normalize_response(
            data,
            response
        )

    # =====================================================
    # ASK
    # =====================================================

    def ask(
        self,
        message: str,
        memory: str = "",
        conversation: str = ""
    ):

        messages = self.build_prompt(
            message,
            memory,
            conversation
        )

        response = llm.chat(
            messages
        )

        return self.parse_response(
            response
        )


brain = Brain()
