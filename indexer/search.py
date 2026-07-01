from indexer.project_indexer import project_indexer


class ProjectSearch:

    # ==========================================
    # Keyword Search
    # ==========================================

    def keyword(
        self,
        keyword
    ):

        matches = project_indexer.find_text(
            keyword
        )

        return {

            "success": True,

            "keyword": keyword,

            "matches": matches,

            "count": len(matches)

        }

    # ==========================================
    # File Search
    # ==========================================

    def files(
        self,
        keyword
    ):

        matches = project_indexer.find_file(
            keyword
        )

        return {

            "success": True,

            "keyword": keyword,

            "matches": matches,

            "count": len(matches)

        }

    # ==========================================
    # First Match
    # ==========================================

    def first(
        self,
        keyword
    ):

        results = project_indexer.find_text(
            keyword
        )

        if not results:

            return {

                "success": False,

                "message": "No matches found."

            }

        return {

            "success": True,

            "match": results[0]

        }

    # ==========================================
    # Context Search
    # ==========================================

    def context(
        self,
        keyword,
        before=0,
        after=2
    ):

        matches = project_indexer.find_text(
            keyword
        )

        if not matches:

            return {

                "success": False,

                "message": "No matches."

            }

        chunks = project_indexer.get_chunks()

        output = []

        for match in matches:

            index = chunks.index(match)

            start = max(
                0,
                index - before
            )

            end = min(
                len(chunks),
                index + after + 1
            )

            output.append(

                {

                    "path": match["path"],

                    "context": chunks[start:end]

                }

            )

        return {

            "success": True,

            "results": output,

            "count": len(output)

        }

    # ==========================================
    # Statistics
    # ==========================================

    def statistics(self):

        return project_indexer.statistics()


search = ProjectSearch()