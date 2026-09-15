from unittest.mock import patch

from agent.coordinator import coordinator


mock_ai_response = {
    "message": "Opening Notepad, boss.",
    "action": "OPEN",
    "target": "notepad"
}


with patch(
    "agent.coordinator.brain.ask",
    return_value=mock_ai_response
):

    with patch(
        "ai.executor.open_app",
        return_value={
            "success": True,
            "message": "Mock Notepad opened."
        }
    ) as mock_open:

        result = coordinator.process(
            "Open Notepad"
        )

        print("FINAL RESULT:")
        print(result)

        print()
        print("OPEN APP CALLED:")
        print(mock_open.called)

        print()
        print("OPEN APP ARGUMENT:")
        print(mock_open.call_args)
