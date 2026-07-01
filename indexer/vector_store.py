import os
import pickle

import faiss
import numpy as np

from indexer.embeddings import embeddings


class VectorStore:

    def __init__(self):

        self.dimension = 384

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

        self.metadata = []

    # ======================================
    # ADD DOCUMENTS
    # ======================================

    def add(self, chunks):

        vectors = []

        for chunk in chunks:

            vector = embeddings.encode(
                chunk["text"]
            )

            vectors.append(vector)
            self.metadata.append(chunk)

        vectors = np.array(
            vectors,
            dtype="float32"
        )

        self.index.add(vectors)

        return {
            "success": True,
            "chunks": len(chunks)
        }

    # ======================================
    # SEARCH
    # ======================================

    def search(
        self,
        query,
        top_k=5
    ):

        vector = embeddings.encode(query)

        vector = np.array(
            [vector],
            dtype="float32"
        )

        distances, indices = self.index.search(
            vector,
            top_k
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index == -1:
                continue

            item = dict(
                self.metadata[index]
            )

            item["score"] = float(distance)

            results.append(item)

        return results

    # ======================================
    # SAVE
    # ======================================

    def save(
        self,
        folder="memory"
    ):

        os.makedirs(
            folder,
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            os.path.join(
                folder,
                "vectors.faiss"
            )
        )

        with open(
            os.path.join(
                folder,
                "metadata.pkl"
            ),
            "wb"
        ) as f:

            pickle.dump(
                self.metadata,
                f
            )

        return {
            "success": True
        }

    # ======================================
    # LOAD
    # ======================================

    def load(
        self,
        folder="memory"
    ):

        index_file = os.path.join(
            folder,
            "vectors.faiss"
        )

        metadata_file = os.path.join(
            folder,
            "metadata.pkl"
        )

        if not os.path.exists(index_file):

            return {
                "success": False,
                "message": "No vector index found."
            }

        self.index = faiss.read_index(
            index_file
        )

        with open(
            metadata_file,
            "rb"
        ) as f:

            self.metadata = pickle.load(f)

        return {
            "success": True,
            "chunks": len(self.metadata)
        }

    # ======================================
    # INFO
    # ======================================

    def info(self):

        return {
            "dimension": self.dimension,
            "vectors": self.index.ntotal
        }


vector_store = VectorStore()