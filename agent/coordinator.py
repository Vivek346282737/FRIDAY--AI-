from ai.brain import brain
from ai.executor import executor
from ai.workflow_planner import workflow_planner


class Coordinator:

    def __init__(self):

        self.history = []

    # =====================================================
    # BUILD CONVERSATION CONTEXT
    # =====================================================

    def _build_conversation_context(
        self,
        limit=10
    ):

        recent_history = self.history[-limit:]

        if not recent_history:
            return ""

        lines = []

        for item in recent_history:

            user_message = item.get(
                "user",
                ""
            )

            assistant_message = item.get(
                "assistant",
                ""
            )

            lines.append(
                f"User: {user_message}"
            )

            lines.append(
                f"FRIDAY: {assistant_message}"
            )

        return "\n".join(lines)

    # =====================================================
    # MAIN PROCESS
    # =====================================================

    def process(
        self,
        message: str,
        memory: str = "",
        conversation: str = ""
    ):

        # -------------------------------------------------
        # VALIDATE MESSAGE
        # -------------------------------------------------

        if not message:

            return {
                "success": False,
                "message": "Please provide a message.",
                "execution": None
            }

        # -------------------------------------------------
        # BUILD CONVERSATION CONTEXT
        # -------------------------------------------------

        if not conversation:

            conversation = (
                self._build_conversation_context()
            )

        # =================================================
        # 1. ASK BRAIN
        # =================================================

        try:

            ai_reply = brain.ask(
                message,
                memory,
                conversation
            )

        except Exception as e:

            return {
                "success": False,
                "message": (
                    f"Brain error: {str(e)}"
                ),
                "execution": None
            }

        # =================================================
        # 2. CREATE WORKFLOW PLAN
        # =================================================

        plan = workflow_planner.create_plan(
            ai_reply
        )

        if not plan.get(
            "success",
            False
        ):

            final_message = (
                "I understood the request, but "
                "the generated action plan was invalid. "
                + plan.get(
                    "message",
                    ""
                )
            )

            self.history.append({
                "user": message,
                "assistant": final_message
            })

            return {
                "success": False,
                "message": final_message,
                "ai_reply": ai_reply,
                "plan": plan,
                "execution": None
            }

        # =================================================
        # 3. EXECUTE WORKFLOW
        # =================================================

        actions = plan.get(
            "actions",
            []
        )

        execution = None

        if actions:

            # IMPORTANT:
            # Executor expects a dictionary containing
            # the actions list, not the raw list itself.

            workflow = {
                "actions": actions
            }

            execution = (
                executor.execute_workflow(
                    workflow
                )
            )

        # =================================================
        # 4. BUILD INITIAL RESPONSE
        # =================================================

        final_message = ai_reply.get(
            "message",
            ""
        )

        if not final_message:

            final_message = (
                "I'm ready, boss."
            )

        # =================================================
        # 5. HANDLE EXECUTION RESULT
        # =================================================

        if execution is not None:

            if execution.get(
                "success",
                False
            ):

                if not ai_reply.get(
                    "message"
                ):

                    final_message = (
                        "The requested workflow "
                        "was completed successfully."
                    )

            else:

                error_message = execution.get(
                    "message",
                    "Workflow failed."
                )

                final_message = (
                    "I couldn't complete the "
                    "full workflow, boss. "
                    f"{error_message}"
                )

        # =================================================
        # 6. STORE HISTORY
        # =================================================

        self.history.append({

            "user": message,

            "assistant": final_message

        })

        # =================================================
        # 7. FINAL RESPONSE
        # =================================================

        return {

            "success": (

                execution is None

                or execution.get(
                    "success",
                    False
                )

            ),

            "message": final_message,

            "ai_reply": ai_reply,

            "plan": plan,

            "execution": execution

        }

    # =====================================================
    # HISTORY
    # =====================================================

    def history_size(self):

        return len(
            self.history
        )

    def get_history(self):

        return self.history

    def clear_history(self):

        self.history.clear()

        return {

            "success": True,

            "message": (
                "Conversation history cleared."
            )

        }


coordinator = Coordinator()
