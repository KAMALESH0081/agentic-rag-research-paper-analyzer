from langchain_ollama import ChatOllama
from app.utils.logger import log, log_section
import json

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)


def extract_json(reranked_chunks):

    context_parts = []

    for query, chunks in reranked_chunks.items():
        joined_chunks = "\n".join([f"- {chunk}" for chunk in chunks])
        context_parts.append(f"Query: {query}\nChunks:\n{joined_chunks}")

    context = "\n\n".join(context_parts)


    prompt = f"""
You are an AI system that extracts structured information from research papers.

Carefully read the provided context from a research paper and extract the required information.

Return the result STRICTLY in the following JSON format:

{{
 "datasets_used": [],
 "benchmark_dataset": [],
 "evaluation_metric": [],
 "method": []
}}

Rules:
- Each field MUST be a list of strings.
- Extract only information that appears explicitly in the context.
- Do NOT guess or invent information.
- If information is not present, return an empty list [].
- Do NOT include explanations or extra text.
- Do NOT output anything other than valid JSON.

Definitions:
- datasets_used → datasets used to train the model.
- benchmark_dataset → datasets used for evaluation or comparison.
- evaluation_metric → metrics used to measure performance (accuracy, F1-score, BLEU, etc.).
- method → the proposed model, architecture, or method introduced in the paper.

Context:
{context}
"""
    log_section("full prompt with context")
    log(prompt)

    response = llm.invoke(prompt)

    log_section("model response")
    log(response.content)

    response = json.loads(response.content)
     

    return response


