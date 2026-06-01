import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Load from text file and pair Questions with Answers
with open('50 Facts.txt', 'r', encoding='utf-8') as f:
    raw_lines = [line.strip() for line in f if line.strip()]

chunks = []
for i in range(0, len(raw_lines), 2):
    if i + 1 < len(raw_lines):
        question = raw_lines[i]
        answer = raw_lines[i+1]
        # Combine question and answer into a single chunk
        paired_chunk = f"سوال: {question}\nجواب: {answer}"
        chunks.append(paired_chunk)

print(f"Loaded and paired {len(chunks)} QA chunks")

if len(chunks) == 0:
    print("No QA chunks created. Check 50 Facts.txt.")
    exit(1)

# Generate embeddings
embeddings = model.encode(chunks)
print(f"Embeddings shape: {embeddings.shape}")

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings.astype(np.float32))
print(f"Index size: {index.ntotal}")

# Save index
faiss.write_index(index, "urdu_index.faiss")
print("Index saved to urdu_index.faiss")

# Also save chunks list for retrieval later
import json
with open('chunks.json', 'w', encoding='utf-8') as f:
    json.dump(chunks, f, ensure_ascii=False, indent=2)
print("Chunks saved to chunks.json")