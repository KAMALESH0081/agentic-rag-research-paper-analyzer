from unstructured.partition.pdf import partition_pdf
from app.utils.logger import log, log_section

def load_pdf(file_path: str):
    """Extract text elements from PDF (simple RAG version)"""

    log_section("PDF LOADING")

    log(f"Partitioning document: {file_path}")

    elements = partition_pdf(
        filename=file_path,
        strategy="fast",
    )

    log(f"Total elements extracted: {len(elements)}")

    # convert elements to plain text
    texts = [el.text for el in elements if hasattr(el, "text") and el.text]

    log(f"Total text elements after filtering: {len(texts)}")

    # 🔥 Log first few elements (VERY IMPORTANT)
    log_section("SAMPLE EXTRACTED TEXT")

    for i, text in enumerate(texts[:10]):
        log(f"\nElement {i+1}:\n{text}")

    return texts