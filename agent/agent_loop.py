from agent.coordinator import coordinator


class AgentLoop:

    def __init__(self):

        self.max_iterations = 5

    # =====================================================
    # Run
    # =====================================================

    def run(

        self,

        message: str,

        memory: str = "",

        conversation: str = ""

    ):

        return coordinator.process(

            message,

            memory,

            conversation

        )

    # =====================================================
    # Future Voice Mode
    # =====================================================

    def run_forever(self):

        while True:

            try:

                message = input(

                    "You: "

                )

                if message.lower() in [

                    "exit",

                    "quit",

                    "bye"

                ]:

                    print(

                        "FRIDAY: Goodbye, Vivek."

                    )

                    break

                result = self.run(

                    message

                )

                print()

                print(

                    "FRIDAY:"

                )

                print(

                    result.get(

                        "message",

                        ""

                    )

                )

                print()

            except KeyboardInterrupt:

                print(

                    "\nStopping FRIDAY..."

                )

                break


agent_loop = AgentLoop()
