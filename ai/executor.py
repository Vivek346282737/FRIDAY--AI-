from services.process_service import open_app, close_app

from browser.browser_agent import browser_agent
from desktop.desktop_agent import desktop_agent
from desktop.desktop_actions import execute_sequence
from vision.vision_agent import vision_agent


class Executor:

    # =====================================================
    # EXECUTE SINGLE ACTION
    # =====================================================

    def execute_single(self, action, target=None, steps=None):

        if not action:

            return {
                "success": False,
                "message": "Action is missing."
            }

        action = str(action).upper().strip()

        if target is not None:
            target = str(target).strip()

        try:

            # =============================================
            # OPEN APPLICATION
            # =============================================

            if action == "OPEN":

                if not target:
                    return {
                        "success": False,
                        "message": "Application target is missing."
                    }

                return open_app(target)


            # =============================================
            # CLOSE APPLICATION
            # =============================================

            if action == "CLOSE":

                if not target:
                    return {
                        "success": False,
                        "message": "Application target is missing."
                    }

                return close_app(target)


            # =============================================
            # BROWSER
            # =============================================

            if action == "BROWSER":

                if not target:
                    return {
                        "success": False,
                        "message": "Browser instruction is missing."
                    }

                return browser_agent.execute(target)


            # =============================================
            # DESKTOP SINGLE ACTION
            # =============================================

            if action == "DESKTOP":

                if not target:
                    return {
                        "success": False,
                        "message": "Desktop instruction is missing."
                    }

                return desktop_agent.execute(target)


            # =============================================
            # DESKTOP MULTI-STEP SEQUENCE
            # =============================================

            if action == "DESKTOP_SEQUENCE":

                if not isinstance(steps, list):

                    return {
                        "success": False,
                        "message": "Desktop sequence steps are missing."
                    }

                result = execute_sequence(steps)

                result["type"] = "desktop_sequence"

                if result.get("success"):
                    result["message"] = (
                        "Desktop sequence completed."
                    )

                return result


            # =============================================
            # VISION
            # =============================================

            if action == "VISION":

                if not target:
                    return {
                        "success": False,
                        "message": "Vision instruction is missing."
                    }

                return vision_agent.execute(target)


            # =============================================
            # FILE
            # =============================================

            if action == "FILE":

                return {
                    "success": True,
                    "type": "file",
                    "instruction": target
                }


            # =============================================
            # SYSTEM
            # =============================================

            if action == "SYSTEM":

                return {
                    "success": True,
                    "type": "system",
                    "instruction": target
                }


            return {
                "success": False,
                "message": f"Unknown action: {action}"
            }


        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }


    # =====================================================
    # EXECUTE WORKFLOW
    # =====================================================

    def execute_workflow(self, workflow):

        return self.execute(workflow)


    # =====================================================
    # EXECUTE RESPONSE / WORKFLOW
    # =====================================================

    def execute(self, ai_reply):

        # ---------------------------------------------
        # VALIDATE
        # ---------------------------------------------

        if not ai_reply:

            return {
                "success": False,
                "message": "AI response is empty."
            }


        if not isinstance(ai_reply, dict):

            return {
                "success": False,
                "message": "Invalid AI response format."
            }


        # =============================================
        # MULTIPLE ACTIONS
        # =============================================

        actions = ai_reply.get("actions")


        if isinstance(actions, list):

            results = []


            for index, item in enumerate(
                actions,
                start=1
            ):

                if not isinstance(item, dict):

                    result = {
                        "success": False,
                        "message": "Invalid action item."
                    }


                    results.append({
                        "step": index,
                        "action": None,
                        "target": None,
                        "result": result
                    })


                    return {
                        "success": False,
                        "type": "workflow",
                        "results": results,
                        "message": "Workflow failed."
                    }


                action = item.get("action")
                target = item.get("target")
                steps = item.get("steps")


                result = self.execute_single(
                    action=action,
                    target=target,
                    steps=steps
                )


                results.append({

                    "step": index,

                    "action": action,

                    "target": target,

                    "result": result

                })


                # -------------------------------------
                # STOP WORKFLOW ON FAILURE
                # -------------------------------------

                if not result.get("success", False):

                    return {

                        "success": False,

                        "type": "workflow",

                        "results": results,

                        "message": (
                            result.get(
                                "message",
                                "Workflow failed."
                            )
                        )

                    }


            return {

                "success": True,

                "type": "workflow",

                "results": results,

                "message": (
                    "Workflow completed successfully."
                )

            }


        # =============================================
        # SINGLE ACTION
        # =============================================

        action = ai_reply.get("action")
        target = ai_reply.get("target")
        steps = ai_reply.get("steps")


        if not action:

            return {

                "success": True,

                "type": "conversation",

                "message": ai_reply.get(
                    "message",
                    ""
                )

            }


        return self.execute_single(

            action=action,

            target=target,

            steps=steps

        )


executor = Executor()
