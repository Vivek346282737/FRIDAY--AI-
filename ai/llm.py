import os
from typing import List, Dict

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLM:

    def __init__(self):

        self.provider = os.getenv(
            "AI_PROVIDER",
            "openai"
        ).lower()

        self.model = os.getenv(
            "MODEL",
            "gpt-5.5"
        )

        self.client = None

        self.initialize()

    def initialize(self):

        if self.provider == "openai":

            self.client = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY")
            )

        else:

            raise Exception(
                f"Unsupported AI Provider: {self.provider}"
            )

    def chat(
        self,
        messages: List[Dict]
    ) -> str:

        if self.provider == "openai":

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )

            return response.choices[0].message.content

        raise Exception(
            "Provider not supported."
        )


llm = LLM()