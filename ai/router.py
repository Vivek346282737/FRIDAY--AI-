from ai.intent import intent_detector, IntentType
from ai.skills import skills


class Router:

    def route(self, message: str):

        intent = intent_detector.detect(message)

        skill = skills.get_skill(intent)

        return {
            "intent": intent,
            "skill": skill
        }

    def is_chat(self, message: str):

        return (
            intent_detector.detect(message)
            == IntentType.CHAT
        )

    def is_browser(self, message: str):

        return (
            intent_detector.detect(message)
            == IntentType.BROWSER
        )

    def is_app_control(self, message: str):

        return (
            intent_detector.detect(message)
            == IntentType.APP_CONTROL
        )

    def is_memory(self, message: str):

        return (
            intent_detector.detect(message)
            == IntentType.MEMORY
        )

    def is_system(self, message: str):

        return (
            intent_detector.detect(message)
            == IntentType.SYSTEM
        )

    def is_file(self, message: str):

        return (
            intent_detector.detect(message)
            == IntentType.FILE
        )

    def is_coding(self, message: str):

        return (
            intent_detector.detect(message)
            == IntentType.CODING
        )


router = Router()