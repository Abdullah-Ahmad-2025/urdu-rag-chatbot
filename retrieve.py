import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json

# Load model
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Load index and chunks
index = faiss.read_index("urdu_index.faiss")
with open('chunks.json', 'r', encoding='utf-8') as f:
    chunks = json.load(f)

queries = [
    "پاکستان کا دارالحکومت کیا ہے؟",
    "پاکستان کب ایٹمی طاقت بنا؟",
    "پاکستان کی سب سے بلند چوٹی کون سی ہے؟",
    "پاکستان کے پہلے وزیر اعظم کون تھے؟"
]

k = 3
for q in queries:
    q_emb = model.encode([q])
    distances, indices = index.search(q_emb.astype(np.float32), k)
    print(f"\nQuery: {q}")
    for i, idx in enumerate(indices[0]):
        if idx != -1 and idx < len(chunks):
            print(f"  {i+1}. {chunks[idx]} (distance: {distances[0][i]:.4f})")