from unstructured.partition.pdf import partition_pdf


def load_pdf(file_path: str):
    """Extract text elements from PDF (simple RAG version)"""
    
    print(f"Partitioning document: {file_path}")

    elements = partition_pdf(
        filename=file_path,
        strategy="fast",
    )

    print(f"✅ Extracted {len(elements)} elements")

    # convert elements to plain text
    texts = [el.text for el in elements if hasattr(el, "text") and el.text]

    return texts