from indexer.vector_store import vector_store


class SemanticSearch:

    def __init__(self):

        loaded = vector_store.load()

        if not loaded["success"]:
            print("No vector database found.")

    # =====================================
    # Search
    # =====================================

    def search(
        self,
        query,
        top_k=5
    ):

        return vector_store.search(
            query=query,
            top_k=top_k
        )

    # =====================================
    # Pretty Print
    # =====================================

    def pretty(
        self,
        query,
        top_k=5
    ):

        results = self.search(
            query,
            top_k
        )

        print("\n" + "=" * 60)
        print("QUERY :", query)
        print("=" * 60)

        for i, item in enumerate(results, 1):

            print(f"\nResult {i}")

            print("Path :", item["path"])

            print(
                f"Chunk : {item['chunk'] + 1}/{item['total_chunks']}"
            )

            print("Score :", round(item["score"], 4))

            print("-" * 60)

            print(item["text"][:500])

        return results


semantic_search = SemanticSearch()