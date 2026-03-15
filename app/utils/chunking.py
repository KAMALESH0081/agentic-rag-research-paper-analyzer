from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(texts):
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,       # max characters per chunk
        chunk_overlap=100     # overlap for context continuity
    )

    chunks = text_splitter.split_text("\n".join(texts))

    print(f"✅ Created {len(chunks)} chunks")

    return chunks