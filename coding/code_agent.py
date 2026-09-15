from ai.brain import brain
from ai.planner import planner
from ai.reasoner import reasoner

from coding.code_memory import code_memory

from coding.terminal_agent import terminal_agent
from coding.error_reader import error_reader
from coding.patcher import patcher
from coding.verifier import verifier
from coding.vscode_agent import vscode_agent


class CodeAgent:

    def __init__(self):

        self.max_iterations = 5

        self.history = []

        self.last_prompt = ""

        self.last_fix = ""

        self.last_analysis = None

    # ====================================================
    # History
    # ====================================================

    def reset(self):

        self.history = []

    def add_history(
        self,
        title,
        data
    ):

        self.history.append(
            {
                "title": title,
                "data": data
            }
        )
            # ====================================================
    # Terminal
    # ====================================================

    def run_command(
        self,
        command,
        cwd=None
    ):

        result = terminal_agent.run(
            command,
            cwd
        )

        self.add_history(
            "command",
            result
        )

        return result

    # ====================================================
    # Verify
    # ====================================================

    def verify(
        self,
        command,
        cwd=None
    ):

        result = verifier.verify(
            command,
            cwd
        )

        self.add_history(
            "verification",
            result
        )

        return result

    # ====================================================
    # Read File
    # ====================================================

    def read(
        self,
        file
    ):

        result = patcher.read(file)

        self.add_history(
            "read",
            result
        )

        return result

    # ====================================================
    # Write File
    # ====================================================

    def write(
        self,
        file,
        content
    ):

        result = patcher.write(
            file,
            content
        )

        self.add_history(
            "write",
            result
        )

        return result

    # ====================================================
    # Replace Text
    # ====================================================

    def replace(
        self,
        file,
        old,
        new
    ):

        result = patcher.replace_text(
            file,
            old,
            new
        )

        self.add_history(
            "replace",
            result
        )

        return result

    # ====================================================
    # Replace Line
    # ====================================================

    def replace_line(
        self,
        file,
        line,
        text
    ):

        result = patcher.replace_line(
            file,
            line,
            text
        )

        self.add_history(
            "replace_line",
            result
        )

        return result
        # ====================================================
    # Insert Line
    # ====================================================

    def insert_line(
        self,
        file,
        line,
        text
    ):

        result = patcher.insert_line(
            file,
            line,
            text
        )

        self.add_history(
            "insert_line",
            result
        )

        return result

    # ====================================================
    # Delete Line
    # ====================================================

    def delete_line(
        self,
        file,
        line
    ):

        result = patcher.delete_line(
            file,
            line
        )

        self.add_history(
            "delete_line",
            result
        )

        return result

    # ====================================================
    # VS Code
    # ====================================================

    def open_file(
        self,
        file
    ):

        result = vscode_agent.open_file(
            file
        )

        self.add_history(
            "open_file",
            result
        )

        return result

    # ====================================================
    # Error Analysis
    # ====================================================

    def analyze(
        self,
        execution
    ):

        result = error_reader.analyze(
            execution
        )

        self.last_analysis = result

        self.add_history(
            "analysis",
            result
        )

        return result

    # ====================================================
    # Ask Brain
    # ====================================================

    def ask(
        self,
        prompt
    ):

        answer = brain.ask(
            prompt
        )

        self.last_prompt = prompt

        self.last_fix = answer

        self.add_history(
            "llm",
            answer
        )

        return answer
        # ====================================================
    # Insert Line
    # ====================================================

    def insert_line(
        self,
        file,
        line,
        text
    ):

        result = patcher.insert_line(
            file,
            line,
            text
        )

        self.add_history(
            "insert_line",
            result
        )

        return result

    # ====================================================
    # Delete Line
    # ====================================================

    def delete_line(
        self,
        file,
        line
    ):

        result = patcher.delete_line(
            file,
            line
        )

        self.add_history(
            "delete_line",
            result
        )

        return result

    # ====================================================
    # VS Code
    # ====================================================

    def open_file(
        self,
        file
    ):

        result = vscode_agent.open_file(
            file
        )

        self.add_history(
            "open_file",
            result
        )

        return result

    # ====================================================
    # Error Analysis
    # ====================================================

    def analyze(
        self,
        execution
    ):

        result = error_reader.analyze(
            execution
        )

        self.last_analysis = result

        self.add_history(
            "analysis",
            result
        )

        return result

    # ====================================================
    # Ask Brain
    # ====================================================

    def ask(
        self,
        prompt
    ):

        answer = brain.ask(
            prompt
        )

        self.last_prompt = prompt

        self.last_fix = answer

        self.add_history(
            "llm",
            answer
        )

        return answer
        # ====================================================
    # Clean AI Output
    # ====================================================

    def clean_code(
        self,
        code: str
    ):

        if not code:
            return ""

        code = code.strip()

        if code.startswith("```python"):
            code = code[9:]

        elif code.startswith("```"):
            code = code[3:]

        if code.endswith("```"):
            code = code[:-3]

        return code.strip()

    # ====================================================
    # Auto Repair
    # ====================================================

    def auto_fix(
        self,
        file,
        verify_command
    ):

        self.reset()

        for attempt in range(
            1,
            self.max_iterations + 1
        ):

            verification = self.verify(
                verify_command
            )

            if verification["success"]:

                return {
                    "success": True,
                    "attempts": attempt,
                    "history": self.history
                }

            analysis = self.analyze(
                verification
            )

            source = self.read(
                file
            )

            if not source["success"]:

                return source

            prompt = self.build_prompt(

                file=file,

                code=source["content"],

                analysis=analysis["summary"]

            )

            fixed_code = self.ask(
                prompt
            )

            fixed_code = self.clean_code(
                fixed_code
            )

            if not fixed_code:

                return {

                    "success": False,

                    "message": "AI returned empty code.",

                    "history": self.history

                }

            backup = patcher.backup(
                file
            )

            self.add_history(
                "backup",
                backup
            )

            write_result = self.write(
                file,
                fixed_code
            )

            if not write_result["success"]:

                return write_result

            self.add_history(
                "patched",
                {
                    "attempt": attempt,
                    "file": file
                }
            )

            verify_after_patch = self.verify(
                verify_command
            )

            self.add_history(
                "post_verify",
                verify_after_patch
            )

            if verify_after_patch["success"]:

                return {

                    "success": True,

                    "attempts": attempt,

                    "history": self.history

                }

        return {

            "success": False,

            "message": "Maximum repair attempts reached.",

            "history": self.history

        }
        # ====================================================
    # Simple Compile
    # ====================================================

    def compile_python(
        self,
        file
    ):

        return self.verify(
            f"python -m py_compile {file}"
        )

    # ====================================================
    # Execute Python
    # ====================================================

    def execute_python(
        self,
        file
    ):

        return self.run_command(
            f"python {file}"
        )

    # ====================================================
    # Fix Python File
    # ====================================================

    def fix_python_file(
        self,
        file
    ):

        return self.auto_fix(

            file=file,

            verify_command=f"python -m py_compile {file}"

        )

    # ====================================================
    # Run And Fix
    # ====================================================

    def run_and_fix(
        self,
        file
    ):

        self.reset()

        execution = self.execute_python(
            file
        )

        if execution["success"]:

            return {

                "success": True,

                "message": "Program executed successfully.",

                "history": self.history

            }

        return self.auto_fix(

            file=file,

            verify_command=f"python {file}"

        )

    # ====================================================
    # Repair Project
    # ====================================================

    def repair_project(
        self,
        files
    ):

        results = []

        for file in files:

            result = self.fix_python_file(
                file
            )

            results.append(

                {

                    "file": file,

                    "result": result

                }

            )

        return {

            "success": True,

            "results": results

        }

    # ====================================================
    # History
    # ====================================================

    def get_history(self):

        return self.history


code_agent = CodeAgent()