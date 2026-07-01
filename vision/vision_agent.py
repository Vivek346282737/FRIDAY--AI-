from vision.vision_controller import vision
from vision.ocr import ocr
from vision.screen_analyzer import screen
from vision.image_analyzer import image_analyzer


class VisionAgent:

    def execute(self, instruction: str):

        text = instruction.strip()
        lower = text.lower()

        # =====================================
        # Screenshot
        # =====================================

        if lower == "screenshot":

            return vision.screenshot()

        # =====================================
        # Read Screen
        # =====================================

        if lower == "read":

            return {

                "success": True,

                "text": ocr.text_from_screen()

            }

        # =====================================
        # Analyze Screen
        # =====================================

        if lower == "analyze":

            return screen.analyze()

        # =====================================
        # Summary
        # =====================================

        if lower == "summary":

            return {

                "success": True,

                "summary": screen.summary()

            }

        # =====================================
        # Resolution
        # =====================================

        if lower == "resolution":

            return {

                "success": True,

                "resolution": vision.resolution()

            }

        # =====================================
        # Image Analyzer
        # =====================================

        if lower == "image":

            return image_analyzer.summary()

        # =====================================
        # Find Text
        # Example:
        # find chrome
        # find login
        # =====================================

        if lower.startswith("find "):

            keyword = text[5:].lower()

            results = ocr.read_screen()

            found = []

            for item in results:

                if keyword in item["text"].lower():

                    found.append(item)

            return {

                "success": True,

                "keyword": keyword,

                "matches": found,

                "count": len(found)

            }

        return {

            "success": False,

            "message": "Unknown vision instruction."

        }


vision_agent = VisionAgent()