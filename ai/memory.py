import re

from memory.manager import memory_manager


def extract_memory(text: str):

    text = text.strip()

    patterns = [

        (r"my name is (.+)", "profile", "name"),

        (r"i am (.+)", "profile", "name"),

        (r"i live in (.+)", "profile", "city"),

        (r"my favourite language is (.+)", "preferences", "language"),

        (r"my favorite language is (.+)", "preferences", "language"),

        (r"my favourite color is (.+)", "preferences", "color"),

        (r"my favorite color is (.+)", "preferences", "color"),

        (r"i like (.+)", "preferences", "likes"),
    ]

    lower = text.lower()

    for pattern, category, key in patterns:

        match = re.search(pattern, lower)

        if match:

            value = match.group(1).strip()

            memory_manager.remember(
                category,
                key,
                value
            )

            return True

    return False