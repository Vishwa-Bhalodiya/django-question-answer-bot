import os
from pypdf import PdfReader
from unstructured.partition.docx import partition_docx
from langchain_openai import AzureChatOpenAI

# ---------------------------
# Load file
# ---------------------------
def load_file(file_path: str):
    ext = file_path.split(".")[-1].lower()

    if ext == "txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return [f.read()]

    elif ext == "pdf":
        reader = PdfReader(file_path)
        return [page.extract_text() for page in reader.pages if page.extract_text()]

    elif ext in ["docx", "doc"]:
        return [p.text for p in partition_docx(filename=file_path)]

    else:
        raise ValueError(f"Unsupported file type: {ext}")

# ---------------------------
# Split text (manual)
# ---------------------------
def split_text(docs, chunk_size=1000, chunk_overlap=100):
    chunks = []
    for text in docs:
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start = end - chunk_overlap
    return chunks

# ---------------------------
# Azure Chat (SAFE init)
# ---------------------------
def get_chat_model():
    return AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1-mini"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
        temperature=0,
    )

# ---------------------------
# Ask question
# ---------------------------
def ask_question(chunks, question):
    chat_model = get_chat_model()  # ✅ defined above
    context_text = "\n\n".join(chunks)

    response = chat_model.invoke([
        {
            "role": "user",
            "content": (
                "Answer using only the following context.\n\n"
                f"{context_text}\n\n"
                f"Question: {question}"
            )
        }
    ])

    return response.content
