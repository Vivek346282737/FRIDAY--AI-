import easyocr
import numpy as np
from PIL import Image

from vision.vision_controller import vision


class OCR:

    def __init__(self):

        # Reader sirf ek baar load hoga
        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

    # ==================================================
    # Read text from PIL Image
    # ==================================================

    def read_image(self, image: Image.Image):

        image = np.array(image)

        results = self.reader.readtext(image)

        output = []

        for result in results:

            output.append({

                "text": result[1],

                "confidence": float(result[2]),

                "box": result[0]

            })

        return output

    # ==================================================
    # Read text from file
    # ==================================================

    def read_file(self, path):

        image = vision.load(path)

        return self.read_image(image)

    # ==================================================
    # Read current screen
    # ==================================================

    def read_screen(self):

        image = vision.capture()

        return self.read_image(image)

    # ==================================================
    # Plain text only
    # ==================================================

    def text_from_screen(self):

        data = self.read_screen()

        return "\n".join(

            item["text"]

            for item in data

        )

    def text_from_file(self, path):

        data = self.read_file(path)

        return "\n".join(

            item["text"]

            for item in data

        )


ocr = OCR()