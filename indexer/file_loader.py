from pathlib import Path


class FileLoader:

    def __init__(self):

        self.allowed_extensions = {

            ".py",
            ".txt",
            ".md",
            ".json",
            ".yaml",
            ".yml",
            ".toml",
            ".ini",
            ".html",
            ".css",
            ".js",
            ".ts"

        }

        self.ignore = {

            "__pycache__",
            ".git",
            ".venv",
            "node_modules",
            "dist",
            "build"

        }

    # ==========================================
    # VALID FILE
    # ==========================================

    def is_valid(self, path: Path):

        if path.suffix.lower() not in self.allowed_extensions:

            return False

        for part in path.parts:

            if part in self.ignore:

                return False

        return True

    # ==========================================
    # LOAD FILE
    # ==========================================

    def load_file(self, path):

        path = Path(path)

        try:

            text = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            return {

                "success": True,
                "path": str(path),
                "text": text

            }

        except Exception as e:

            return {

                "success": False,
                "path": str(path),
                "message": str(e)

            }

    # ==========================================
    # LOAD PROJECT
    # ==========================================

    def load_project(self, root):

        root = Path(root)

        files = []

        for file in root.rglob("*"):

            if file.is_file() and self.is_valid(file):

                files.append(

                    self.load_file(file)

                )

        return files


file_loader = FileLoader()