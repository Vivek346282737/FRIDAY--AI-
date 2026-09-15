from agent.agent_loop import agent_loop


class TaskEngine:

    def __init__(self):

        self.tasks = []

    def execute(

        self,

        goal: str,

        memory: str = "",

        conversation: str = ""

    ):

        result = agent_loop.run(

            goal,

            memory,

            conversation

        )

        self.tasks.append({

            "goal": goal,

            "result": result

        })

        return result

    def history(self):

        return self.tasks

    def clear(self):

        self.tasks.clear()

        return {

            "success": True,

            "message": "Task history cleared."

        }


task_engine = TaskEngine()