from vision.vision_controller import vision
from vision.ocr import ocr


class ScreenAnalyzer:

    # ==========================================
    # Analyze current screen
    # ==========================================

    def analyze(self):

        screenshot = vision.screenshot()

        text = ocr.text_from_screen()

        resolution = vision.resolution()

        lines = []

        if text:

            for line in text.splitlines():

                line = line.strip()

                if line:

                    lines.append(line)

        return {

            "success": True,

            "resolution": resolution,

            "screenshot": screenshot["file"],

            "text": text,

            "text_count": len(lines),

            "lines": lines
        }

    # ==========================================
    # Human readable summary
    # ==========================================

    def summary(self):

        data = self.analyze()

        summary = []

        summary.append(
            f"Resolution : "
            f"{data['resolution']['width']} x "
            f"{data['resolution']['height']}"
        )

        summary.append(
            f"Screenshot : {data['screenshot']}"
        )

        summary.append(
            f"Detected Lines : {data['text_count']}"
        )

        summary.append("")

        if data["lines"]:

            summary.append("Visible Text:")

            summary.append("")

            summary.extend(data["lines"])

        else:

            summary.append("No readable text found.")

        return "\n".join(summary)

    # ==========================================
    # Read only text
    # ==========================================

    def read(self):

        return ocr.text_from_screen()

    # ==========================================
    # Screen Resolution
    # ==========================================

    def resolution(self):

        return vision.resolution()


screen = ScreenAnalyzer()