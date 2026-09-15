"""
FRIDAY Planner V2
=================

Responsibilities

1. Detect intent
2. Build execution plan
3. Retrieve semantic project context
4. Generate execution hints
5. Produce planner output for Reasoner

Compatible with:

- brain.py
- reasoner.py
- executor.py
- router.py
- CodeMemory (RAG)
"""

from __future__ import annotations

from typing import Dict, List

from ai.intent import IntentType
from ai.router import router
from coding.code_memory import code_memory


class Planner:

    def __init__(self):

        self.max_context_results = 5

    # =====================================================
    # Public API
    # =====================================================

    def create_plan(self, message: str) -> Dict:

        route = router.route(message)

        intent = route["intent"]

        context = self._collect_context(
            message,
            intent
        )

        steps = self._build_steps(
            intent,
            message
        )

        hints = self._build_hints(
            intent,
            message
        )

        confidence = self._confidence(
            intent,
            context
        )

        return {

            "intent": intent,

            "steps": steps,

            "context": context,

            "hints": hints,

            "confidence": confidence

        }

    # =====================================================
    # Context Retrieval
    # =====================================================

    def _collect_context(
        self,
        message: str,
        intent: IntentType
    ) -> List[Dict]:

        if intent != IntentType.CODING:

            return []

        try:

            return code_memory.search(
                message,
                self.max_context_results
            )

        except Exception:

            return []

    # =====================================================
    # Confidence
    # =====================================================

    def _confidence(
        self,
        intent,
        context
    ) -> float:

        score = 0.60

        if intent == IntentType.CODING:
            score += 0.20

        if context:
            score += 0.15

        return min(score, 1.0)
        # =====================================================
    # Planning Steps
    # =====================================================

    def _build_steps(
        self,
        intent: IntentType,
        message: str
    ) -> List[str]:

        if intent == IntentType.APP_CONTROL:
            return self._app_steps(message)

        if intent == IntentType.BROWSER:
            return self._browser_steps(message)

        if intent == IntentType.FILE:
            return self._file_steps(message)

        if intent == IntentType.MEMORY:
            return self._memory_steps(message)

        if intent == IntentType.SYSTEM:
            return self._system_steps(message)

        if intent == IntentType.CODING:
            return self._coding_steps(message)

        return self._chat_steps(message)

    # =====================================================
    # APP
    # =====================================================

    def _app_steps(
        self,
        message: str
    ) -> List[str]:

        return [

            "Understand application request",

            "Identify target application",

            "Verify application name",

            "Launch or close application",

            "Validate successful execution",

            "Return execution summary"

        ]

    # =====================================================
    # BROWSER
    # =====================================================

    def _browser_steps(
        self,
        message: str
    ) -> List[str]:

        return [

            "Understand browser request",

            "Check browser availability",

            "Launch browser if required",

            "Navigate to requested destination",

            "Execute browser action",

            "Collect browser result",

            "Return final summary"

        ]

    # =====================================================
    # FILE
    # =====================================================

    def _file_steps(
        self,
        message: str
    ) -> List[str]:

        return [

            "Understand requested file operation",

            "Locate target file or folder",

            "Verify permissions",

            "Execute requested operation",

            "Verify changes",

            "Return final status"

        ]

    # =====================================================
    # MEMORY
    # =====================================================

    def _memory_steps(
        self,
        message: str
    ) -> List[str]:

        return [

            "Extract memory information",

            "Validate important facts",

            "Store memory safely",

            "Verify storage",

            "Return confirmation"

        ]

    # =====================================================
    # SYSTEM
    # =====================================================

    def _system_steps(
        self,
        message: str
    ) -> List[str]:

        return [

            "Inspect requested system resource",

            "Collect diagnostics",

            "Analyze health",

            "Suggest optimization",

            "Return report"

        ]
    # =====================================================
    # CODING
    # =====================================================

    def _coding_steps(
        self,
        message: str
    ) -> List[str]:

        steps = [

            "Understand programming request",

            "Identify affected project modules",

            "Retrieve relevant project code using semantic search",

            "Analyze retrieved implementation",

            "Design safest solution",

            "Generate clean implementation",

            "Review generated solution",

            "Verify compatibility with existing project",

            "Return implementation"

        ]

        if self._collect_context(
            message,
            IntentType.CODING
        ):

            steps.insert(
                3,
                "Use semantic RAG context before generating code"
            )

        return steps

    # =====================================================
    # CHAT
    # =====================================================

    def _chat_steps(
        self,
        message: str
    ) -> List[str]:

        return [

            "Understand the user's intent",

            "Identify missing information if any",

            "Think carefully",

            "Generate a natural response",

            "Keep response concise and helpful"

        ]

    # =====================================================
    # Dynamic Planner Hints
    # =====================================================

    def _build_hints(
        self,
        intent: IntentType,
        message: str
    ) -> List[str]:

        hints = []

        if intent == IntentType.CODING:

            hints.extend([

                "Always use retrieved project context.",

                "Never invent filenames.",

                "Prefer existing project architecture.",

                "Modify existing implementation before creating new files.",

                "Generate production quality code."

            ])

        elif intent == IntentType.BROWSER:

            hints.extend([

                "Prefer existing browser controller.",

                "Avoid duplicate browser instances.",

                "Return browser execution result."

            ])

        elif intent == IntentType.APP_CONTROL:

            hints.extend([

                "Verify application existence.",

                "Handle failures gracefully."

            ])

        elif intent == IntentType.SYSTEM:

            hints.extend([

                "Do not perform destructive operations.",

                "Collect diagnostics before recommendations."

            ])

        else:

            hints.append(
                "Respond naturally."
            )

        return hints

    # =====================================================
    # Planner Summary
    # =====================================================

    def summary(
        self,
        plan: Dict
    ) -> str:

        lines = []

        lines.append(
            f"Intent : {plan['intent']}"
        )

        lines.append(
            f"Confidence : {plan['confidence']:.2f}"
        )

        lines.append("")

        lines.append("Execution Steps:")

        for i, step in enumerate(
            plan["steps"],
            start=1
        ):

            lines.append(
                f"{i}. {step}"
            )

        return "\n".join(lines)
        # =====================================================
    # Context Formatter
    # =====================================================

    def format_context(
        self,
        plan: Dict
    ) -> str:

        if not plan.get("context"):
            return ""

        sections = []

        for item in plan["context"]:

            try:

                sections.append(
                    f"""
==================================================
FILE : {item["path"]}
CHUNK : {item["chunk"] + 1}/{item["total_chunks"]}
==================================================

{item["text"]}

"""
                )

            except Exception:
                continue

        return "\n".join(sections)

    # =====================================================
    # Prompt Context
    # =====================================================

    def build_prompt_context(
        self,
        message: str
    ) -> str:

        plan = self.create_plan(message)

        output = []

        output.append(
            "=============================="
        )

        output.append(
            "FRIDAY EXECUTION PLAN"
        )

        output.append(
            "=============================="
        )

        output.append("")

        output.append(
            f"Intent : {plan['intent']}"
        )

        output.append(
            f"Confidence : {plan['confidence']:.2f}"
        )

        output.append("")

        output.append(
            "Execution Steps:"
        )

        for index, step in enumerate(
            plan["steps"],
            start=1
        ):

            output.append(
                f"{index}. {step}"
            )

        output.append("")

        if plan["hints"]:

            output.append(
                "Planner Hints:"
            )

            for hint in plan["hints"]:

                output.append(
                    f"- {hint}"
                )

            output.append("")

        context = self.format_context(plan)

        if context:

            output.append(
                "Relevant Project Context:"
            )

            output.append(context)

        return "\n".join(output)


# =====================================================
# Singleton
# =====================================================

planner = Planner()