from app.core.vectordb import collection
from app.core.embeddings import embedding_model
from app.utils.logger import log, log_section

QUERIES = [
    "What datasets were used to train the model?",
    "What benchmark datasets were used for evaluation?",
    "What evaluation metrics were used?",
    "What model architecture or method is proposed?"
]

def retrieve_context():

    log_section("RETRIEVAL STAGE")

    retrieval_results = {}

    for query in QUERIES:

        log_section(f"QUERY: {query}")

        query_embedding = embedding_model.encode([query])[0]

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5,
            include=["documents", "distances"]  
        )

        chunks = results["documents"][0]
        distances = results["distances"][0]

        retrieval_results[query] = chunks

        for i, (chunk, distance) in enumerate(zip(chunks, distances)):

            log(f"\nTop {i+1}")
            log(f"Chunk:\n{chunk[:500]}")

    return retrieval_results