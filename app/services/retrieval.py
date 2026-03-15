from app.core.vectordb import collection
from app.core.embeddings import model

QUERIES = [
    "What datasets were used to train the model?",
    "What benchmark datasets were used for evaluation?",
    "What evaluation metrics were used?",
    "What model architecture or method is proposed?"
]

def retrieve_context():

    all_chunks = []

    for query in QUERIES:

        query_embedding = model.encode([query])[0]

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=2
        )

        all_chunks.extend(results["documents"][0])

    return "\n".join(all_chunks)