import subprocess
from typing import Optional


class TerminalAgent:

    def run(
        self,
        command: str,
        cwd: Optional[str] = None,
        timeout: int = 120
    ):

        try:

            process = subprocess.run(
                command,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            return {
                "success": process.returncode == 0,
                "command": command,
                "return_code": process.returncode,
                "stdout": process.stdout.strip(),
                "stderr": process.stderr.strip()
            }

        except subprocess.TimeoutExpired:

            return {
                "success": False,
                "command": command,
                "message": "Command timed out."
            }

        except Exception as e:

            return {
                "success": False,
                "command": command,
                "message": str(e)
            }

    def python(self, args: str = ""):
        return self.run(f"python {args}")

    def pip(self, args: str = ""):
        return self.run(f"pip {args}")

    def git(self, args: str = ""):
        return self.run(f"git {args}")

    def npm(self, args: str = ""):
        return self.run(f"npm {args}")

    def uvicorn(self, args: str = ""):
        return self.run(f"python -m uvicorn {args}")


terminal_agent = TerminalAgent()