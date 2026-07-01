import cv2
import mss
import numpy as np
from PIL import Image
from pathlib import Path
from datetime import datetime


class VisionController:

    def __init__(self):

        self.sct = mss.mss()

    # ==========================================
    # Capture entire screen
    # ==========================================

    def capture(self):

        monitor = self.sct.monitors[1]

        screenshot = self.sct.grab(monitor)

        image = Image.frombytes(
            "RGB",
            screenshot.size,
            screenshot.rgb
        )

        return image

    # ==========================================
    # Save Screenshot
    # ==========================================

    def screenshot(self, filename=None):

        image = self.capture()

        if filename is None:

            filename = (
                "vision_"
                + datetime.now().strftime("%Y%m%d_%H%M%S")
                + ".png"
            )

        image.save(filename)

        return {
            "success": True,
            "file": filename
        }

    # ==========================================
    # PIL -> OpenCV
    # ==========================================

    def to_cv2(self, image):

        return cv2.cvtColor(
            np.array(image),
            cv2.COLOR_RGB2BGR
        )

    # ==========================================
    # Load Image
    # ==========================================

    def load(self, path):

        path = Path(path)

        if not path.exists():

            raise FileNotFoundError(path)

        image = Image.open(path)

        return image

    # ==========================================
    # Resolution
    # ==========================================

    def resolution(self):

        monitor = self.sct.monitors[1]

        return {

            "width": monitor["width"],

            "height": monitor["height"]
        }


vision = VisionController()