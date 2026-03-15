import chromadb
import uuid
from app.core.embeddings import model

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="rag_collection"
)

def embed_and_store(chunks):

    #collection.delete()  # clear previous PDF

    embeddings = model.encode(chunks)

    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    print(f"✅ Stored {len(chunks)} chunks in ChromaDB")