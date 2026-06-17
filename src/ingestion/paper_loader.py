import pandas as pd

def load_papers(file_path: str) -> pd.DataFrame:
    """
    Load arXiv research paper records from CSV.
    """
    df = pd.read_csv(file_path)

    required_columns = [
        "title",
        "abstract",
        "authors",
        "published",
        "link",
        "domain",
        "subdomain",
        "summary"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return df
