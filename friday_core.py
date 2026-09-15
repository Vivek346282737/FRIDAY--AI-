"""
FRIDAY Core
Main entry point for FRIDAY task processing.
"""

from agent.agent_loop import agent_loop


def process_message(

    message: str,

    memory: str = "",

    conversation: str = ""

) -> dict:

    if not message:

        return {

            "success": False,

            "message": "Please provide a message.",

            "actions": [],

            "execution": None

        }

    message = message.strip()

    if not message:

        return {

            "success": False,

            "message": "Please provide a message.",

            "actions": [],

            "execution": None

        }

    return agent_loop.run(

        message,

        memory,

        conversation

    )
