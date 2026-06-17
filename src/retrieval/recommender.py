def recommend_similar_papers(query: str, papers, top_k: int = 5) -> list:
    """
    Lightweight baseline recommender for similar papers.

    This returns the first top_k records as a simple baseline.
    FAISS-based semantic retrieval can be connected using embeddings.py and faiss_index.py.
    """
    if papers is None or len(papers) == 0:
        return []

    recommendations = []

    for _, row in papers.head(top_k).iterrows():
        recommendations.append({
            "title": row.get("title", "Unknown Title"),
            "authors": row.get("authors", "Unknown Authors"),
            "published": row.get("published", ""),
            "domain": row.get("domain", "Unknown Domain"),
            "subdomain": row.get("subdomain", "Unknown Subdomain"),
            "abstract": row.get("abstract", ""),
            "summary": row.get("summary", ""),
            "link": row.get("link", "")
        })

    return recommendations
