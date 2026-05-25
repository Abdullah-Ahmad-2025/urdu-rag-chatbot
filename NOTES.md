# NOTES.md – Learning Journey

---


\## Day 1



\### Setup Status

\- Successfully created Python virtual environment

\- Installed required libraries: langchain, faiss-cpu, sentence-transformers, pymupdf

\- Git repository initialized and connected to GitHub



\### Observations

\- SentenceTransformer model loaded without errors

\- Urdu sentences successfully encoded into embeddings

\- Cosine similarity test executed successfully



\### Notes (Important)

\- No major errors encountered during setup

\- Installation process was smooth

\- Urdu text is being processed correctly by the embedding model



\### Learning

\- Virtual environments help isolate project dependencies

\- Embeddings convert sentences into numerical vectors

\- Cosine similarity is used to measure semantic closeness between sentences



## Day 2 – First Real Understanding of RAG

Today I started properly understanding what Retrieval-Augmented Generation (RAG) actually is.

At first, I thought it was just “chatbot + database,” but after reading more, I realized it’s more structured than that.

---

### My Current Understanding

RAG has two main parts:

**1. Retriever**
This part searches through stored documents and finds relevant information.

**2. Generator**
This part uses the retrieved information to generate an answer.

So instead of an LLM answering purely from its training, it first looks up information and then responds using that context.

That clicked for me today.

---

## Important thing I realized

The retriever is what makes the chatbot grounded in real data.

Without retrieval:
- The model can guess
- It can hallucinate
- It may confidently give wrong answers

With retrieval:
- It answers from actual documents
- Responses become more trustworthy
- It can work on domain-specific information

This helped me understand *why RAG exists in the first place.*

---

## Dense Retrieval (Still Learning)

I learned that many modern systems use embeddings for retrieval.

My understanding right now:

Text is converted into vectors (numbers), and similar meanings should be close together in vector space.

This connects directly to what I tested on Day 1 with cosine similarity.

I’m starting to see how that small experiment fits into the bigger system.

---

## Connecting This to My Urdu Project

I think my Urdu chatbot will roughly work like this:

User asks question
↓
Question gets converted into embedding
↓
FAISS searches similar Urdu text chunks
↓
Relevant chunks are retrieved
↓
LLM generates answer using those chunks

Seeing this pipeline written out made the project feel more real.

---

## Things I’m Still Confused About

- How FAISS efficiently searches huge vector databases
- How many chunks should ideally be retrieved (k value)
- How chunk size affects answer quality
- How retrieval quality is actually evaluated

I’ll understand these better as I build.

---

## Biggest takeaway today

Day 1 taught me *how embeddings work.*

Day 2 helped me understand *why embeddings matter in a real AI system.*

That feels like an actual step forward.
