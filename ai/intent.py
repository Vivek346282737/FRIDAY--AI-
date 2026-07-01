from enum import Enum


class IntentType(str, Enum):
    CHAT = "chat"
    APP_CONTROL = "app_control"
    BROWSER = "browser"
    FILE = "file"
    MEMORY = "memory"
    SYSTEM = "system"
    CODING = "coding"
    UNKNOWN = "unknown"


class IntentDetector:

    def detect(self, message: str) -> IntentType:

        text = message.lower().strip()

        # ------------------------
        # App Control
        # ------------------------

        app_keywords = [
            "open",
            "launch",
            "start",
            "close",
            "kill",
            "exit"
        ]

        if any(word in text for word in app_keywords):
            return IntentType.APP_CONTROL

        # ------------------------
        # Browser
        # ------------------------

        browser_keywords = [
            "google",
            "search",
            "youtube",
            "website",
            "browser",
            "chrome",
            "edge"
        ]

        if any(word in text for word in browser_keywords):
            return IntentType.BROWSER

        # ------------------------
        # File
        # ------------------------

        file_keywords = [
            "file",
            "folder",
            "copy",
            "move",
            "delete",
            "rename",
            "excel",
            "pdf"
        ]

        if any(word in text for word in file_keywords):
            return IntentType.FILE

        # ------------------------
        # Memory
        # ------------------------

        memory_keywords = [
            "remember",
            "my name",
            "i like",
            "my favourite",
            "my favorite"
        ]

        if any(word in text for word in memory_keywords):
            return IntentType.MEMORY

        # ------------------------
        # Coding
        # ------------------------

        coding_keywords = [
            "python",
            "java",
            "javascript",
            "react",
            "bug",
            "code",
            "program",
            "api"
        ]

        if any(word in text for word in coding_keywords):
            return IntentType.CODING

        # ------------------------
        # System
        # ------------------------

        system_keywords = [
            "cpu",
            "ram",
            "battery",
            "system",
            "performance",
            "optimize",
            "storage"
        ]

        if any(word in text for word in system_keywords):
            return IntentType.SYSTEM

        return IntentType.CHAT


intent_detector = IntentDetector()