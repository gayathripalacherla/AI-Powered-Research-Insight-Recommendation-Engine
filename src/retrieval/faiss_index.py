import faiss
import numpy as np

def build_faiss_index(embeddings: np.ndarray):
    """
    Build a FAISS index from research paper embeddings.
    """
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_index(index, query_embedding, top_k: int = 5):
    """
    Search FAISS index for semantically similar papers.
    """
    distances, indices = index.search(query_embedding, top_k)
    return distances, indices
