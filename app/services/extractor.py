from langchain_ollama import ChatOllama
import json

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)


def extract_json(context):

    prompt = f"""
You are an AI system that extracts structured information from research papers.

Extract the required information ONLY from the provided context.

Return the result STRICTLY in the following JSON format:

{{
 "datasets_used": [],
 "benchmark_dataset": [],
 "evaluation_metric": [],
 "method": []
}}

Rules:
- Each field MUST be a list of strings.
- If the information is not present in the context, return an empty list [].
- Do NOT guess information.
- Do NOT include explanations.
- Only return valid JSON.

CONTEXT:
{context}
"""

    response = llm.invoke(prompt)

    response = json.loads(response.content)
    
    print(type(response))
    print(response)    

    return response









    














"""prompt = f
You are analyzing an AI research paper.

Extract the following information from the provided context.

Return JSON in the following format:

{{
 "datasets_used": ["..."],
 "benchmark_dataset": ["...",
 "evaluation_metric": "...",
 "method": "..."
}}

Rules:
- If the information is not present, return null.
- Only return JSON.
- Do not explain anything.

CONTEXT:
{context}
"""