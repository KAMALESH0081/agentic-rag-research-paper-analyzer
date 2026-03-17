from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.utils.logger import log, log_section

def create_chunks(texts):

    log_section("CHUNKING")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    combined_text = "\n".join(texts)

    log(f"Total input text length: {len(combined_text)} characters")

    chunks = text_splitter.split_text(combined_text)

    log(f"Total chunks created: {len(chunks)}")

    log_section("SAMPLE CHUNKS")

    for i, chunk in enumerate(chunks[:10]):
        log(f"\nChunk {i+1} (len={len(chunk)}):\n{chunk}")

    return chunks