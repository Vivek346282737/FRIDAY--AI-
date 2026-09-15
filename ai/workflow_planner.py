class WorkflowPlanner:

    VALID_ACTIONS = {

        "OPEN",
        "CLOSE",
        "BROWSER",
        "DESKTOP",
        "DESKTOP_SEQUENCE",
        "VISION",
        "FILE",
        "SYSTEM"

    }

    # =====================================================
    # VALIDATE DESKTOP STEP
    # =====================================================

    def validate_desktop_step(self, step):

        if not isinstance(
            step,
            dict
        ):

            return False, (
                "Desktop step must be an object."
            )

        action = step.get(
            "action"
        )

        if not action:

            return False, (
                "Desktop step action is missing."
            )

        action = str(
            action
        ).lower().strip()

        valid_steps = {

            "move",
            "click",
            "double_click",
            "right_click",
            "type",
            "press",
            "hotkey",
            "scroll",
            "wait"

        }

        if action not in valid_steps:

            return False, (
                f"Unsupported desktop step: "
                f"{action}"
            )

        return True, None

    # =====================================================
    # VALIDATE ACTION
    # =====================================================

    def validate_action(self, item):

        if not isinstance(
            item,
            dict
        ):

            return False, (
                "Workflow item must be an object."
            )

        action = item.get(
            "action"
        )

        if not action:

            return False, (
                "Workflow action is missing."
            )

        action = str(
            action
        ).upper().strip()

        if action not in self.VALID_ACTIONS:

            return False, (
                f"Unsupported action: {action}"
            )

        # ---------------------------------------------
        # Desktop Sequence
        # ---------------------------------------------

        if action == "DESKTOP_SEQUENCE":

            steps = item.get(
                "steps"
            )

            if not isinstance(
                steps,
                list
            ):

                return False, (
                    "DESKTOP_SEQUENCE requires steps."
                )

            if not steps:

                return False, (
                    "DESKTOP_SEQUENCE cannot be empty."
                )

            for step in steps:

                valid, error = (
                    self.validate_desktop_step(
                        step
                    )
                )

                if not valid:

                    return False, error

            return True, None

        # ---------------------------------------------
        # Other actions require target
        # ---------------------------------------------

        target = item.get(
            "target"
        )

        if target is None or not str(
            target
        ).strip():

            return False, (
                f"{action} requires a target."
            )

        return True, None

    # =====================================================
    # CREATE PLAN
    # =====================================================

    def create_plan(self, ai_reply):

        if not isinstance(
            ai_reply,
            dict
        ):

            return {

                "success": False,

                "message": (
                    "AI response is not a valid object."
                ),

                "actions": []

            }

        actions = ai_reply.get(
            "actions"
        )

        # ---------------------------------------------
        # Single Action
        # ---------------------------------------------

        if not actions:

            action = ai_reply.get(
                "action"
            )

            target = ai_reply.get(
                "target"
            )

            if action:

                actions = [

                    {

                        "action": action,

                        "target": target

                    }

                ]

            else:

                actions = []

        # ---------------------------------------------
        # Validate
        # ---------------------------------------------

        plan = []

        for index, item in enumerate(

            actions,

            start=1

        ):

            valid, error = self.validate_action(
                item
            )

            if not valid:

                return {

                    "success": False,

                    "message": (
                        f"Invalid workflow step "
                        f"{index}: {error}"
                    ),

                    "actions": plan,

                    "failed_step": index

                }

            plan.append(
                item
            )

        return {

            "success": True,

            "actions": plan,

            "message": (
                "Workflow plan created successfully."
            )

        }


workflow_planner = WorkflowPlanner()
