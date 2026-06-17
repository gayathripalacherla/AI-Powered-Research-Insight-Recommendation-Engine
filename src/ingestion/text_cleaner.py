def clean_text(text: str) -> str:
    """
    Basic text cleaning for research paper abstracts.
    """
    if not text:
        return ""

    text = str(text)
    text = " ".join(text.split())
    return text
