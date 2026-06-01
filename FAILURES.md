# FAILURES.md – Urdu RAG Project



## Day 1



### Setup Status

- Successfully created Python virtual environment

- Installed required libraries: langchain, faiss-cpu, sentence-transformers, pymupdf

- Git repository initialized and connected to GitHub



### Observations

- SentenceTransformer model loaded without errors

- Urdu sentences successfully encoded into embeddings

- Cosine similarity test executed successfully



### Notes (Important)

- No major errors encountered during setup

- Installation process was smooth

- Urdu text is being processed correctly by the embedding model



### Learning

- Virtual environments help isolate project dependencies

- Embeddings convert sentences into numerical vectors

- Cosine similarity is used to measure semantic closeness between sentences

  ## Day 2

## RAG Testing Failures (Urdu QA Dataset)
1. Incorrect Chunking (Main Issue)
Data was split into sentences instead of full Q–A pairs.
This broke semantic meaning and context.

Result: retriever matched “similar questions” instead of correct Q→A mapping.

3. Dense Embeddings Overlapping for Short Urdu Facts
Short Urdu factual questions have very similar structure.
Embedding model failed to distinguish between different facts.

Result: many candidates had nearly identical distances.

5. No Hybrid Retrieval (Dense Only System)
System relied only on vector similarity.
No keyword-based matching to enforce exact question signals.

Result: semantically similar but incorrect answers ranked high.

