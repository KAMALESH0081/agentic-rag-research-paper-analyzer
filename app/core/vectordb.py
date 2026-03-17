import chromadb
import uuid
from app.core.embeddings import embedding_model
from app.utils.logger import log, log_section

client = chromadb.PersistentClient(
    path="data/chroma_db"
)
try:
    client.delete_collection(name="rag_collection")
except:
    pass

collection = client.get_or_create_collection(
    name="rag_collection"
)

def embed_and_store(chunks):

    log_section("EMBEDDING + STORAGE")

    log(f"Total chunks received: {len(chunks)}")

    log_section("SAMPLE CHUNKS BEFORE EMBEDDING")
    for i, chunk in enumerate(chunks[:5]):
        log(f"\nChunk {i+1}:\n{chunk[:300]}")

    embeddings = embedding_model.encode(chunks)

    log(f"Generated embeddings shape: {len(embeddings)} x {len(embeddings[0])}")

    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    log(f"Stored {len(chunks)} chunks in ChromaDB")