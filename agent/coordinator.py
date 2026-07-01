from services.process_service import open_app, close_app

from browser.browser_agent import browser_agent
from desktop.desktop_agent import desktop_agent
from vision.vision_agent import vision_agent

from coding.code_agent import code_agent

from ai.executor import executor


class Coordinator:

    def execute(self, instruction: str):

        if not instruction:

            return None

        text = instruction.strip()

        upper = text.upper()

        # ==========================================
        # ACTION PREFIX
        # ==========================================

        if upper.startswith("ACTION:"):

            payload = text[7:].strip()

        else:

            payload = text

        # ==========================================
        # BROWSER
        # ==========================================

        if payload.upper().startswith("BROWSER:"):

            return browser_agent.execute(
                payload[8:].strip()
            )

        # ==========================================
        # DESKTOP
        # ==========================================

        if payload.upper().startswith("DESKTOP:"):

            return desktop_agent.execute(
                payload[8:].strip()
            )

        # ==========================================
        # VISION
        # ==========================================

        if payload.upper().startswith("VISION:"):

            return vision_agent.execute(
                payload[7:].strip()
            )

        # ==========================================
        # CODE
        # ==========================================

        if payload.upper().startswith("CODE:"):

            command = payload[5:].strip()

            if command.lower().startswith("compile "):

                file = command[8:].strip()

                return code_agent.compile_python(file)

            if command.lower().startswith("run "):

                file = command[4:].strip()

                return code_agent.execute_python(file)

            if command.lower().startswith("fix "):

                file = command[4:].strip()

                return code_agent.fix_python_file(file)

            return {
                "success": False,
                "message": "Unknown CODE action."
            }

        # ==========================================
        # OPEN
        # ==========================================

        if payload.upper().startswith("OPEN:"):

            app = payload[5:].strip()

            return open_app(app)

        # ==========================================
        # CLOSE
        # ==========================================

        if payload.upper().startswith("CLOSE:"):

            app = payload[6:].strip()

            return close_app(app)

        # ==========================================
        # FALLBACK
        # ==========================================

        return executor.execute(text)


coordinator = Coordinator()