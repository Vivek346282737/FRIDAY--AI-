from memory.conversation_db import ConversationDB


class Conversation:

    def add_user(self, text):

        ConversationDB.add(
            "user",
            text
        )

    def add_ai(self, text):

        ConversationDB.add(
            "assistant",
            text
        )

    def clear(self):

        ConversationDB.clear()

    def get_history(self):

        rows = ConversationDB.get()

        history = []

        for row in rows:

            role = row["role"]

            if role == "user":
                history.append(
                    f"User: {row['message']}"
                )

            else:
                history.append(
                    f"FRIDAY: {row['message']}"
                )

        return "\n".join(history)


conversation = Conversation()