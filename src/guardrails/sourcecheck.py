def check_paper_sources(recommendations: list) -> dict:
    """
    Check whether recommended papers include source links.
    """
    if not recommendations:
        return {
            "has_sources": False,
            "message": "No recommendations available for source verification."
        }

    source_count = sum(
        1 for paper in recommendations if paper.get("link")
    )

    return {
        "has_sources": source_count > 0,
        "source_count": source_count,
        "message": "Verify paper details using original publication links."
    }
