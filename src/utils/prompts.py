RESEARCH_SUMMARY_PROMPT = """
You are a research assistant.
Summarize the paper into:
- Problem
- Method
- Key findings
- Limitations

Do not invent claims not supported by the abstract or retrieved context.
"""

RECOMMENDATION_PROMPT = """
Recommend similar papers based on semantic similarity, domain, subdomain, and research topic.
"""

SOURCE_CHECK_PROMPT = """
Check whether recommended papers include traceable source links.
Flag unsupported or missing citation details for review.
"""
