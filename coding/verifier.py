from coding.terminal_agent import terminal_agent
from coding.error_reader import error_reader


class Verifier:

    # =====================================
    # Verify Any Command
    # =====================================

    def verify(
        self,
        command: str,
        cwd: str = None
    ):

        result = terminal_agent.run(
            command,
            cwd=cwd
        )

        analysis = error_reader.analyze(result)

        return {

            "success": analysis["success"],

            "command": command,

            "execution": result,

            "analysis": analysis
        }

    # =====================================
    # Verify Python
    # =====================================

    def python(
        self,
        args: str,
        cwd: str = None
    ):

        return self.verify(
            f"python {args}",
            cwd
        )

    # =====================================
    # Verify Pip
    # =====================================

    def pip(
        self,
        args: str,
        cwd: str = None
    ):

        return self.verify(
            f"pip {args}",
            cwd
        )

    # =====================================
    # Verify Git
    # =====================================

    def git(
        self,
        args: str,
        cwd: str = None
    ):

        return self.verify(
            f"git {args}",
            cwd
        )

    # =====================================
    # Verify NPM
    # =====================================

    def npm(
        self,
        args: str,
        cwd: str = None
    ):

        return self.verify(
            f"npm {args}",
            cwd
        )

    # =====================================
    # Verify Uvicorn
    # =====================================

    def uvicorn(
        self,
        args: str,
        cwd: str = None
    ):

        return self.verify(
            f"python -m uvicorn {args}",
            cwd
        )


verifier = Verifier()