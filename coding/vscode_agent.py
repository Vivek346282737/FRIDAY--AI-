import subprocess
from pathlib import Path


class VSCodeAgent:

    # =====================================
    # Run VS Code Command
    # =====================================

    def run(self, args: str):

        command = f'code {args}'

        try:

            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            return {
                "success": result.returncode == 0,
                "command": command,
                "return_code": result.returncode,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip()
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }

    # =====================================
    # Open Current Folder
    # =====================================

    def open_workspace(self, folder="."):

        return self.run(f'"{folder}"')

    # =====================================
    # Open File
    # =====================================

    def open_file(self, file_path: str):

        path = Path(file_path)

        return self.run(f'"{path}"')

    # =====================================
    # Open File At Line
    # =====================================

    def goto_line(
        self,
        file_path: str,
        line: int
    ):

        path = Path(file_path)

        return self.run(
            f'--goto "{path}:{line}"'
        )

    # =====================================
    # New Window
    # =====================================

    def new_window(self):

        return self.run("--new-window")

    # =====================================
    # Reuse Window
    # =====================================

    def reuse_window(self):

        return self.run("--reuse-window")

    # =====================================
    # Install Extension
    # =====================================

    def install_extension(
        self,
        extension: str
    ):

        return self.run(
            f'--install-extension {extension}'
        )

    # =====================================
    # List Extensions
    # =====================================

    def list_extensions(self):

        return self.run(
            "--list-extensions"
        )

    # =====================================
    # Version
    # =====================================

    def version(self):

        return self.run("--version")


vscode_agent = VSCodeAgent()