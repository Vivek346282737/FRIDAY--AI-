from pathlib import Path
import shutil


class Patcher:

    # =====================================
    # Read File
    # =====================================

    def read(self, file_path: str):

        try:

            path = Path(file_path)

            if not path.exists():

                return {
                    "success": False,
                    "message": "File does not exist."
                }

            return {
                "success": True,
                "file": str(path),
                "content": path.read_text(
                    encoding="utf-8"
                )
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }

    # =====================================
    # Write File
    # =====================================

    def write(
        self,
        file_path: str,
        content: str
    ):

        try:

            path = Path(file_path)

            path.write_text(
                content,
                encoding="utf-8"
            )

            return {
                "success": True,
                "file": str(path)
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }

    # =====================================
    # Backup
    # =====================================

    def backup(self, file_path: str):

        try:

            path = Path(file_path)

            if not path.exists():

                return {
                    "success": False,
                    "message": "File not found."
                }

            backup_path = path.with_suffix(
                path.suffix + ".bak"
            )

            shutil.copy2(
                path,
                backup_path
            )

            return {
                "success": True,
                "backup": str(backup_path)
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }

    # =====================================
    # Replace Text
    # =====================================

    def replace_text(
        self,
        file_path: str,
        old: str,
        new: str
    ):

        data = self.read(file_path)

        if not data["success"]:

            return data

        self.backup(file_path)

        content = data["content"]

        content = content.replace(
            old,
            new
        )

        return self.write(
            file_path,
            content
        )

    # =====================================
    # Replace Line
    # =====================================

    def replace_line(
        self,
        file_path: str,
        line_number: int,
        new_line: str
    ):

        data = self.read(file_path)

        if not data["success"]:

            return data

        self.backup(file_path)

        lines = data["content"].splitlines()

        if line_number < 1:

            return {
                "success": False,
                "message": "Invalid line."
            }

        if line_number > len(lines):

            return {
                "success": False,
                "message": "Line out of range."
            }

        lines[line_number - 1] = new_line

        return self.write(
            file_path,
            "\n".join(lines)
        )

    # =====================================
    # Insert Line
    # =====================================

    def insert_line(
        self,
        file_path: str,
        line_number: int,
        new_line: str
    ):

        data = self.read(file_path)

        if not data["success"]:

            return data

        self.backup(file_path)

        lines = data["content"].splitlines()

        if line_number < 1:

            line_number = 1

        if line_number > len(lines):

            lines.append(new_line)

        else:

            lines.insert(
                line_number - 1,
                new_line
            )

        return self.write(
            file_path,
            "\n".join(lines)
        )

    # =====================================
    # Delete Line
    # =====================================

    def delete_line(
        self,
        file_path: str,
        line_number: int
    ):

        data = self.read(file_path)

        if not data["success"]:

            return data

        self.backup(file_path)

        lines = data["content"].splitlines()

        if (
            line_number < 1
            or line_number > len(lines)
        ):

            return {
                "success": False,
                "message": "Invalid line."
            }

        del lines[line_number - 1]

        return self.write(
            file_path,
            "\n".join(lines)
        )


patcher = Patcher()