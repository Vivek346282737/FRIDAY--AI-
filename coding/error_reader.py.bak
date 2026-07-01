import re


class ErrorReader:

    def analyze(self, result: dict):

        if not result:

            return {
                "success": False,
                "message": "No command result provided."
            }

        stdout = result.get("stdout", "")
        stderr = result.get("stderr", "")

        text = (stdout + "\n" + stderr).strip()

        analysis = {
            "success": result.get("success", False),
            "command": result.get("command", ""),
            "return_code": result.get("return_code", 0),
            "error_type": None,
            "file": None,
            "line": None,
            "message": text
        }

        # =====================================
        # Python Traceback
        # =====================================

        file_match = re.search(
            r'File "(.+?)", line (\d+)',
            text
        )

        if file_match:

            analysis["file"] = file_match.group(1)
            analysis["line"] = int(file_match.group(2))

        # =====================================
        # Common Python Errors
        # =====================================

        errors = [

            "AttributeError",
            "NameError",
            "ImportError",
            "ModuleNotFoundError",
            "SyntaxError",
            "TypeError",
            "ValueError",
            "KeyError",
            "IndexError",
            "RuntimeError",
            "AssertionError",
            "IndentationError",
            "FileNotFoundError",
            "PermissionError"

        ]

        for error in errors:

            if error in text:

                analysis["error_type"] = error
                break

        # =====================================
        # Command / OS Errors
        # =====================================

        if analysis["error_type"] is None:

            lower = text.lower()

            if (
                "can't open file" in lower
                or "no such file or directory" in lower
            ):

                analysis["error_type"] = "FileNotFoundError"

            elif "is not recognized" in lower:

                analysis["error_type"] = "CommandNotFound"

            elif "permission denied" in lower:

                analysis["error_type"] = "PermissionError"

            elif "timed out" in lower:

                analysis["error_type"] = "Timeout"

        # =====================================
        # Human Friendly Summary
        # =====================================

        analysis["summary"] = self.summary(analysis)

        return analysis

    # =====================================
    # Human Readable Summary
    # =====================================

    def summary(self, analysis: dict):

        if analysis["success"]:

            return "Command executed successfully."

        parts = []

        if analysis["error_type"]:

            parts.append(
                f"Error Type: {analysis['error_type']}"
            )

        if analysis["file"]:

            parts.append(
                f"File: {analysis['file']}"
            )

        if analysis["line"]:

            parts.append(
                f"Line: {analysis['line']}"
            )

        if analysis["message"]:

            parts.append(
                f"Message: {analysis['message']}"
            )

        return "\n".join(parts)


error_reader = ErrorReader()