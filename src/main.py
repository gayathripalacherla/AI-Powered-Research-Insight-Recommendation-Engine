from ingestion.paper_loader import load_papers
from retrieval.recommender import recommend_similar_papers
from summarization.summarizer import summarize_paper
from guardrails.validation import validate_query
from utils.logger import log_step

def main():
    query = "Find recent research papers related to retrieval augmented generation and summarize the most relevant paper."

    validate_query(query)

    log_step("Loading arXiv research paper dataset")
    papers = load_papers("data/arxiv_1200_papers.csv")

    log_step("Retrieving similar research papers")
    recommendations = recommend_similar_papers(query, papers)

    log_step("Generating summary for top paper")
    top_paper = recommendations[0] if recommendations else {}
    summary = summarize_paper(top_paper.get("abstract", ""))

    output = {
        "query": query,
        "top_recommendations": recommendations,
        "top_paper_summary": summary
    }

    print(output)

if __name__ == "__main__":
    main()
