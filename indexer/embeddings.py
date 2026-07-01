from sentence_transformers import SentenceTransformer


class Embeddings:

    def __init__(self):

        self.model_name = "all-MiniLM-L6-v2"
        self.model = None

    # ==========================================
    # LOAD MODEL
    # ==========================================

    def load(self):

        if self.model is None:

            self.model = SentenceTransformer(
                self.model_name
            )

        return self.model

    # ==========================================
    # EMBED SINGLE TEXT
    # ==========================================

    def encode(self, text: str):

        model = self.load()

        vector = model.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return vector

    # ==========================================
    # EMBED MULTIPLE TEXTS
    # ==========================================

    def encode_many(self, texts):

        if not texts:

            return []

        model = self.load()

        vectors = model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        return vectors

    # ==========================================
    # EMBED PROJECT CHUNKS
    # ==========================================

    def embed_chunks(self, chunks):

        if not chunks:

            return []

        texts = []

        for chunk in chunks:

            texts.append(
                chunk["text"]
            )

        vectors = self.encode_many(texts)

        results = []

        for chunk, vector in zip(chunks, vectors):

            item = dict(chunk)

            item["embedding"] = vector

            results.append(item)

        return results

    # ==========================================
    # MODEL INFO
    # ==========================================

    def info(self):

        return {
            "model": self.model_name,
            "loaded": self.model is not None
        }


embeddings = Embeddings()