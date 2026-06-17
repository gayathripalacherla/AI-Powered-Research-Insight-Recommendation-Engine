# AI-Powered Research Insight & Recommendation Engine

A production-oriented **Research AI / RAG recommendation system** for semantic academic paper search, contextual paper recommendation, and structured research summarization.

This project uses **SentenceTransformers**, **FAISS**, and **T5-style summarization workflows** to help students, researchers, and data scientists accelerate literature reviews and discover related papers from an arXiv-based research dataset.

---

## Problem Statement

Academic literature review is time-consuming because researchers must search across large paper collections, read long abstracts, identify key ideas, compare related work, and trace sources manually.

This project demonstrates how AI-powered research retrieval and summarization can support literature discovery by combining:

- Semantic search
- Vector-based paper retrieval
- Research paper recommendation
- Structured summarization
- Source-link verification
- Modular NLP pipeline design

---

## Dataset

The project uses an arXiv research paper dataset containing **1,200 paper records**.

Key dataset fields include:

- Title
- Abstract
- Authors
- Published date
- Source link
- Domain
- Subdomain
- Summary

---

## Key Features

- **Semantic paper search** using SentenceTransformers embeddings
- **FAISS-powered vector retrieval** for similar paper recommendation
- **T5-style summarization workflow** with chunking for long text
- **Structured research summaries** covering problem, method, findings, and limitations
- **Domain and subdomain filtering** for topic-specific discovery
- **Source-link checks** for research traceability
- **Notebook prototype** for experimentation and model testing
- Modular Python structure for future API or UI deployment

---

## Tech Stack

- Python
- Pandas
- NumPy
- SentenceTransformers
- FAISS
- Hugging Face Transformers
- T5 summarization
- Gradio / Streamlit prototype
- Docker
- Git/GitHub

---

## System Architecture

```text
arXiv Paper Dataset
    ↓
Data Cleaning + Preprocessing
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Index
    ↓
Semantic Paper Retrieval
    ↓
Research Recommendation Engine
    ↓
Structured Summarization
    ↓
Source Verification
    ↓
Research Insight Output
