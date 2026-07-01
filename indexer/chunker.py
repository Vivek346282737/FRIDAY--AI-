import math


class Chunker:

    def __init__(self):

        self.chunk_size = 1200
        self.overlap = 200

    # ==========================================
    # Split Text
    # ==========================================

    def split_text(
        self,
        text,
        chunk_size=None,
        overlap=None
    ):

        if chunk_size is None:
            chunk_size = self.chunk_size

        if overlap is None:
            overlap = self.overlap

        if not text:

            return []

        chunks = []

        start = 0
        length = len(text)

        while start < length:

            end = min(
                start + chunk_size,
                length
            )

            chunks.append(
                text[start:end]
            )

            if end == length:
                break

            start = end - overlap

        return chunks

    # ==========================================
    # Split File
    # ==========================================

    def split_file(
        self,
        file_data
    ):

        if not file_data["success"]:

            return []

        text = file_data["text"]

        pieces = self.split_text(text)

        results = []

        total = len(pieces)

        for index, chunk in enumerate(pieces):

            results.append(

                {
                    "path": file_data["path"],
                    "chunk": index,
                    "total_chunks": total,
                    "text": chunk
                }

            )

        return results

    # ==========================================
    # Split Project
    # ==========================================

    def split_project(
        self,
        files
    ):

        project_chunks = []

        for file in files:

            project_chunks.extend(

                self.split_file(file)

            )

        return project_chunks

    # ==========================================
    # Statistics
    # ==========================================

    def statistics(
        self,
        chunks
    ):

        if not chunks:

            return {

                "chunks": 0,
                "characters": 0,
                "average": 0

            }

        characters = sum(

            len(c["text"])

            for c in chunks

        )

        return {

            "chunks": len(chunks),

            "characters": characters,

            "average": math.ceil(

                characters / len(chunks)

            )

        }


chunker = Chunker()