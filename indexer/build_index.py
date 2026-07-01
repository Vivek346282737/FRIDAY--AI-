from indexer.file_loader import file_loader
from indexer.chunker import chunker
from indexer.vector_store import vector_store


def build(project="."):

    print("=" * 60)
    print("FRIDAY PROJECT INDEXER")
    print("=" * 60)

    print("\nLoading project...")

    files = file_loader.load_project(project)

    print(f"Files Loaded : {len(files)}")

    print("\nSplitting into chunks...")

    chunks = chunker.split_project(files)

    print(f"Chunks Created : {len(chunks)}")

    print("\nGenerating embeddings...")
    print("This may take a few minutes on first run...\n")

    vector_store.add(chunks)

    print("Saving FAISS index...")

    vector_store.save()

    print("\nIndex Complete!")

    print(vector_store.info())

    print("\nMemory folder created successfully.")


if __name__ == "__main__":

    build()