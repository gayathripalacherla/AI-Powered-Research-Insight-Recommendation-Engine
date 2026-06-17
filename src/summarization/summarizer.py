from summarization.chunker import chunk_text

def summarize_paper(text: str) -> dict:
    """
    Create a structured research paper summary.
    """
    chunks = chunk_text(text)

    if not chunks:
        return {
            "problem": "No abstract or paper text available.",
            "method": "Insufficient context.",
            "findings": "Unable to summarize without text.",
            "limitations": "Human review required."
        }

    preview = chunks[0][:500]

    return {
        "problem": "The paper addresses a research problem described in the provided abstract.",
        "method": "Method details should be extracted from the full paper or abstract context.",
        "findings": preview,
        "limitations": "Generated summary should be reviewed against the original paper."
    }
