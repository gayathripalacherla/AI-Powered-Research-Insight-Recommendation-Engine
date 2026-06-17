# Architecture

This project follows a modular Research RAG and recommendation architecture.

## Pipeline Flow

arXiv Paper Dataset  
→ Data Loading  
→ Text Cleaning  
→ Embedding Generation  
→ FAISS Vector Index  
→ Semantic Retrieval  
→ Paper Recommendation  
→ Structured Summarization  
→ Source Verification  
→ Final Research Insight Output  

## Main Components

### Dataset Layer
Stores arXiv paper metadata including title, abstract, authors, domain, subdomain, publication date, summary, and source link.

### Retrieval Layer
Uses SentenceTransformers and FAISS to support semantic similarity search across research papers.

### Recommendation Layer
Ranks and returns contextually similar papers based on query relevance.

### Summarization Layer
Uses chunking and summarization logic to generate structured research summaries.

### Guardrail Layer
Validates user queries, checks source availability, and discourages unsupported claims.
