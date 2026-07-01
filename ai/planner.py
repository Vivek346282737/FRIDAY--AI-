from ai.intent import IntentType
from ai.router import router


class Planner:

    def create_plan(self, message: str):

        route = router.route(message)

        intent = route["intent"]

        plan = []

        # -----------------------------
        # APP CONTROL
        # -----------------------------

        if intent == IntentType.APP_CONTROL:

            plan = [
                "Understand application request",
                "Identify target application",
                "Verify application name",
                "Execute application control",
                "Confirm execution"
            ]

        # -----------------------------
        # BROWSER
        # -----------------------------

        elif intent == IntentType.BROWSER:

            plan = [
                "Understand browser request",
                "Launch browser if required",
                "Navigate to requested website",
                "Perform requested action",
                "Collect result",
                "Return summary"
            ]

        # -----------------------------
        # FILES
        # -----------------------------

        elif intent == IntentType.FILE:

            plan = [
                "Understand file operation",
                "Locate target",
                "Validate file",
                "Execute operation",
                "Verify result"
            ]

        # -----------------------------
        # MEMORY
        # -----------------------------

        elif intent == IntentType.MEMORY:

            plan = [
                "Extract memory",
                "Store memory",
                "Verify storage"
            ]

        # -----------------------------
        # SYSTEM
        # -----------------------------

        elif intent == IntentType.SYSTEM:

            plan = [
                "Inspect system",
                "Collect information",
                "Analyze condition",
                "Suggest optimization"
            ]

        # -----------------------------
        # CODING
        # -----------------------------

        elif intent == IntentType.CODING:

            plan = [
                "Understand programming task",
                "Design solution",
                "Generate clean code",
                "Review code",
                "Return final solution"
            ]

        # -----------------------------
        # CHAT
        # -----------------------------

        else:

            plan = [
                "Understand user",
                "Think carefully",
                "Generate natural response"
            ]

        return {
            "intent": intent,
            "steps": plan
        }


planner = Planner()