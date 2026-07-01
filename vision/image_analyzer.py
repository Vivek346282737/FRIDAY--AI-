from PIL import Image

from vision.vision_controller import vision
from vision.ocr import ocr


class ImageAnalyzer:

    # ==========================================
    # Analyze PIL Image
    # ==========================================

    def analyze_image(self, image: Image.Image):

        text_data = ocr.read_image(image)

        return {

            "success": True,

            "text": text_data,

            "text_count": len(text_data),

            "width": image.width,

            "height": image.height
        }

    # ==========================================
    # Analyze Image File
    # ==========================================

    def analyze_file(self, path):

        image = vision.load(path)

        return self.analyze_image(image)

    # ==========================================
    # Analyze Current Screen
    # ==========================================

    def analyze_screen(self):

        image = vision.capture()

        return self.analyze_image(image)

    # ==========================================
    # Plain Text
    # ==========================================

    def text(self):

        data = self.analyze_screen()

        return "\n".join(

            item["text"]

            for item in data["text"]

        )

    # ==========================================
    # Summary
    # ==========================================

    def summary(self):

        data = self.analyze_screen()

        return {

            "resolution": f"{data['width']} x {data['height']}",

            "detected_items": data["text_count"],

            "text": self.text()
        }


image_analyzer = ImageAnalyzer()