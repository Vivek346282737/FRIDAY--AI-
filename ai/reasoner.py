from typing import Dict, List


class Reasoner:

    def analyze(self, plan: Dict) -> List[str]:

        reasoning = []

        intent = str(plan.get("intent", "")).split(".")[-1]

        reasoning.append(
            f"Detected intent: {intent}"
        )

        for index, step in enumerate(
            plan["steps"],
            start=1
        ):

            reasoning.append(
                f"Step {index}: {step}"
            )

        reasoning.append(
            "Choose the safest and most efficient execution path."
        )

        return reasoning

    def summarize(self, reasoning: List[str]) -> str:

        return "\n".join(reasoning)


reasoner = Reasoner()