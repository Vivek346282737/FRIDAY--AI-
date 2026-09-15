from indexer.semantic_search import semantic_search


class CodeMemory:

    def search(self, query, k=5):
        return semantic_search.search(query, k)

    def context(self, query, k=5):

        results = self.search(query, k)

        text = []

        for r in results:

            text.append(
                f"""
FILE:
{r["path"]}

CHUNK:
{r["chunk"]+1}/{r["total_chunks"]}

CODE:
{r["text"]}
"""
            )

        return "\n\n".join(text)


code_memory = CodeMemory()