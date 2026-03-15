from app.utils.pdf_loader import load_pdf
from app.utils.chunking import create_chunks
from app.core.vectordb import embed_and_store
from app.services.retrieval import retrieve_context
from app.services.extractor import extract_json


def run_pipeline(file):

    text = load_pdf(file)

    chunks = create_chunks(text)

    embed_and_store(chunks)

    context = retrieve_context()

    print(context)

    result = extract_json(context)

    print(result)

    return result