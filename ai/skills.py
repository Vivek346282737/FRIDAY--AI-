from typing import Dict

from ai.intent import IntentType


class Skills:

    def __init__(self):

        self.skills: Dict[IntentType, str] = {

            IntentType.CHAT: "Conversation",

            IntentType.APP_CONTROL: "Desktop Control",

            IntentType.BROWSER: "Browser Automation",

            IntentType.FILE: "File Management",

            IntentType.MEMORY: "Memory System",

            IntentType.SYSTEM: "System Control",

            IntentType.CODING: "Coding Assistant",

            IntentType.UNKNOWN: "Unknown"
        }

    def get_skill(self, intent: IntentType) -> str:

        return self.skills.get(
            intent,
            "Conversation"
        )

    def register_skill(
        self,
        intent: IntentType,
        name: str
    ):

        self.skills[intent] = name

    def all_skills(self):

        return self.skills


skills = Skills()