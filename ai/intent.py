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

    def __init__(self):

        self.keywords = {

            IntentType.CODING: [
                "python",
                "java",
                "javascript",
                "typescript",
                "react",
                "next",
                "node",
                "django",
                "flask",
                "fastapi",
                "api",
                "bug",
                "error",
                "exception",
                "fix",
                "debug",
                "code",
                "program",
                "compile",
                "function",
                "class",
                "method",
                "module",
                "library",
                "package",
                "git",
                "github",
                "sql",
                "database",
                "planner",
                "executor",
                "reasoner",
                "router"
            ],

            IntentType.BROWSER: [
                "browser",
                "website",
                "google",
                "youtube",
                "bing",
                "duckduckgo",
                "search",
                "tab",
                "url",
                "google.com",
                "youtube.com"
            ],

            IntentType.APP_CONTROL: [
                "open",
                "launch",
                "start",
                "run",
                "close",
                "exit",
                "kill",
                "stop"
            ],

            IntentType.FILE: [
                "file",
                "folder",
                "directory",
                "copy",
                "move",
                "rename",
                "delete",
                "pdf",
                "excel",
                "word",
                "ppt",
                "csv"
            ],

            IntentType.SYSTEM: [
                "cpu",
                "ram",
                "battery",
                "system",
                "performance",
                "storage",
                "disk",
                "network",
                "wifi",
                "gpu",
                "temperature"
            ],

            IntentType.MEMORY: [
                "remember",
                "memorize",
                "my name",
                "i like",
                "my favourite",
                "my favorite"
            ]

        }

    # =====================================================
    # Keyword Score
    # =====================================================

    def _score(self, text: str, words):

        score = 0

        for word in words:

            if word in text:
                score += 1

        return score

    # =====================================================
    # Intent Detection
    # =====================================================

    def detect(self, message: str) -> IntentType:

        text = message.lower().strip()

        # =====================================================
        # Special Rule : Open Installed Applications
        # =====================================================

        launch_words = [
            "open",
            "launch",
            "start",
            "run"
        ]

        installed_apps = [
            "chrome",
            "edge",
            "firefox",
            "notepad",
            "calculator",
            "paint",
            "cmd",
            "terminal",
            "powershell",
            "vscode",
            "visual studio code",
            "spotify",
            "discord",
            "steam",
            "explorer"
        ]

        website_words = [
            ".com",
            ".org",
            ".net",
            ".io",
            "website",
            "google.com",
            "youtube.com"
        ]

        if any(word in text for word in launch_words):

            if any(site in text for site in website_words):
                pass

            elif any(app in text for app in installed_apps):
                return IntentType.APP_CONTROL

        # =====================================================
        # Score Based Detection
        # =====================================================

        scores = {}

        for intent, words in self.keywords.items():

            scores[intent] = self._score(
                text,
                words
            )

        # =====================================================
        # Priority Bonus
        # =====================================================

        if scores[IntentType.CODING]:
            scores[IntentType.CODING] += 3

        if scores[IntentType.MEMORY]:
            scores[IntentType.MEMORY] += 2

        best_intent = max(
            scores,
            key=scores.get
        )

        if scores[best_intent] == 0:
            return IntentType.CHAT

        return best_intent


intent_detector = IntentDetector()