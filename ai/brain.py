import os

from ai.llm import llm
from ai.prompts import prompts
from ai.planner import planner
from ai.reasoner import reasoner

from vision.screen_analyzer import screen


def ask_ai(
    message: str,
    memory: str = "",
    conversation: str = ""
):

    # ----------------------------------
    # Planning
    # ----------------------------------

    plan = planner.create_plan(message)

    # ----------------------------------
    # Reasoning
    # ----------------------------------

    reasoning = reasoner.summarize(
        reasoner.analyze(plan)
    )

    # ----------------------------------
    # Current Screen
    # ----------------------------------

    try:
        screen_info = screen.summary()
    except Exception as e:
        screen_info = f"Vision unavailable: {e}"

    # ----------------------------------
    # Build System Prompt
    # ----------------------------------

    system_prompt = f"""
{prompts.SYSTEM}

{prompts.MEMORY.format(memory=memory)}

{prompts.CONVERSATION.format(conversation=conversation)}

{prompts.PLANNER}

Plan:

{chr(10).join(plan["steps"])}

{prompts.REASONER}

Reasoning:

{reasoning}

{prompts.VISION}

Current Screen:

{screen_info}

{prompts.EXECUTOR}
"""

    messages = [

        {
            "role": "system",
            "content": system_prompt
        },

        {
            "role": "user",
            "content": message
        }

    ]

    return llm.chat(messages)