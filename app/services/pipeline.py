from app.utils.pdf_loader import load_pdf
from app.utils.chunking import create_chunks
from app.core.vectordb import embed_and_store
from app.services.retrieval import retrieve_context
from app.services.reranker import rerank_chunks
from app.services.extractor import extract_json
from app.utils.logger import clear_log


def run_pipeline(file):

    clear_log()

    text = load_pdf(file)

    chunks = create_chunks(text)

    embed_and_store(chunks)

    context = retrieve_context()

    reranked_chunks = rerank_chunks(context)

    result = extract_json(reranked_chunks)

    return result