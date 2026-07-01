from indexer.file_loader import file_loader
from indexer.chunker import chunker


class ProjectIndexer:

    def __init__(self):

        self.project_path = None
        self.files = []
        self.chunks = []

    # ==========================================
    # Build Index
    # ==========================================

    def build(self, project_path="."):

        self.project_path = project_path

        self.files = file_loader.load_project(
            project_path
        )

        self.chunks = chunker.split_project(
            self.files
        )

        return {

            "success": True,

            "project": project_path,

            "files": len(self.files),

            "chunks": len(self.chunks)

        }

    # ==========================================
    # Refresh
    # ==========================================

    def refresh(self):

        if self.project_path is None:

            return {

                "success": False,

                "message": "No project indexed."

            }

        return self.build(
            self.project_path
        )

    # ==========================================
    # Files
    # ==========================================

    def get_files(self):

        return self.files

    # ==========================================
    # Chunks
    # ==========================================

    def get_chunks(self):

        return self.chunks

    # ==========================================
    # Stats
    # ==========================================

    def statistics(self):

        return {

            "project": self.project_path,

            "files": len(self.files),

            "chunks": len(self.chunks),

            "chunk_statistics": chunker.statistics(
                self.chunks
            )

        }

    # ==========================================
    # Find File
    # ==========================================

    def find_file(
        self,
        name
    ):

        matches = []

        lower = name.lower()

        for file in self.files:

            if lower in file["path"].lower():

                matches.append(file)

        return matches

    # ==========================================
    # Find Text
    # ==========================================

    def find_text(
        self,
        keyword
    ):

        keyword = keyword.lower()

        matches = []

        for chunk in self.chunks:

            if keyword in chunk["text"].lower():

                matches.append(chunk)

        return matches

    # ==========================================
    # Summary
    # ==========================================

    def summary(self):

        return {

            "project": self.project_path,

            "files": len(self.files),

            "chunks": len(self.chunks)

        }


project_indexer = ProjectIndexer()