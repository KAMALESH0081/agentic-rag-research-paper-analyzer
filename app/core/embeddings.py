from sentence_transformers import SentenceTransformer, CrossEncoder

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

reranker_model = CrossEncoder("BAAI/bge-reranker-base")
