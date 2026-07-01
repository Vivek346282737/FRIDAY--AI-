from services.process_service import open_app, close_app
from browser.browser_agent import browser_agent
from desktop.desktop_agent import desktop_agent
from vision.vision_agent import vision_agent


class Executor:

    def execute(self, ai_reply: str):

        if not ai_reply:
            return None

        ai_reply = ai_reply.strip()

        if not ai_reply.startswith("ACTION:"):
            return None

        try:

            parts = ai_reply.split(":", 2)

            if len(parts) != 3:
                return {
                    "success": False,
                    "message": "Invalid ACTION format."
                }

            _, action, target = parts

            action = action.upper().strip()
            target = target.strip()

            # ==================================
            # APP
            # ==================================

            if action == "OPEN":
                return open_app(target)

            if action == "CLOSE":
                return close_app(target)

            # ==================================
            # BROWSER
            # ==================================

            if action == "BROWSER":
                return browser_agent.execute(target)

            # ==================================
            # DESKTOP
            # ==================================

            if action == "DESKTOP":
                return desktop_agent.execute(target)

            # ==================================
            # VISION
            # ==================================

            if action == "VISION":
                return vision_agent.execute(target)

            # ==================================
            # FILE
            # ==================================

            if action == "FILE":
                return {
                    "success": True,
                    "type": "file",
                    "instruction": target
                }

            # ==================================
            # SYSTEM
            # ==================================

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


executor = Executor()