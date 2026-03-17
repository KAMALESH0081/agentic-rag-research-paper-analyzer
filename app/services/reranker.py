from app.core.embeddings import reranker_model
from app.utils.logger import log, log_section

def rerank_chunks(retrieval_results, top_k=2):

    log_section("RERANKER STAGE")

    reranked_results = {}

    for query, chunks in retrieval_results.items():

        pairs = [[query, chunk] for chunk in chunks]

        scores = reranker_model.predict(pairs)

        scored_chunks = list(zip(chunks, scores))

        scored_chunks.sort(key=lambda x: x[1], reverse=True)

        top_chunks = [chunk for chunk, score in scored_chunks[:top_k]]

        reranked_results[query] = top_chunks

    log(str(reranked_results))

    return reranked_results