from ai.brain import ask_ai

from agent.coordinator import coordinator

from vision.screen_analyzer import screen


class AgentLoop:

    def run(
        self,
        message: str,
        memory: str = "",
        conversation: str = "",
        max_steps: int = 10
    ):

        history = []

        current_message = message

        for step in range(max_steps):

            print("\n" + "=" * 70)
            print(f"STEP {step + 1}")
            print("=" * 70)

            # =====================================
            # THINK
            # =====================================

            reply = ask_ai(
                current_message,
                memory,
                conversation
            )

            print("\nAI REPLY\n")
            print(reply)

            history.append({
                "step": step + 1,
                "reply": reply
            })

            # =====================================
            # FINAL ANSWER
            # =====================================

            if not reply.startswith("ACTION:"):

                print("\nFINAL RESPONSE\n")

                return {
                    "success": True,
                    "reply": reply,
                    "history": history
                }

            # =====================================
            # EXECUTE USING COORDINATOR
            # =====================================

            execution = coordinator.execute(reply)

            print("\nEXECUTION\n")
            print(execution)

            history.append({
                "step": step + 1,
                "execution": execution
            })

            if not execution:

                return {
                    "success": False,
                    "message": "Execution failed.",
                    "history": history
                }

            # =====================================
            # OBSERVE
            # =====================================

            print("\nOBSERVING SCREEN...\n")

            try:

                observation = screen.summary()

            except Exception as e:

                observation = f"Vision Error: {e}"

            print(observation)

            history.append({
                "step": step + 1,
                "observation": observation
            })

            # =====================================
            # THINK AGAIN
            # =====================================

            current_message = f"""
The previous action has finished.

Original user request:

{message}

Previous action:

{reply}

Execution result:

{execution}

Current screen:

{observation}

Decide what to do next.

Rules:

1. If the user's request is fully complete,
respond naturally.

2. If another action is needed,
return ONLY another ACTION.

3. Never repeat the exact same ACTION unless absolutely necessary.

4. Use the current screen to decide.

5. Use Browser, Desktop, Vision and Coding tools whenever appropriate.

6. Think like Tony Stark's FRIDAY.
"""

            print("\nNEXT PROMPT\n")
            print(current_message)

        return {
            "success": False,
            "message": "Maximum reasoning steps reached.",
            "history": history
        }


agent_loop = AgentLoop()