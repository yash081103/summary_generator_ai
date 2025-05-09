import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_overall_summary(text_list: List[str], llm_client) -> str:
    combined_text = " ".join(text.strip() for text in text_list if text.strip())
    if not combined_text:
        logging.warning("No valid text provided for summarization.")
        return "No content available to summarize."

    try:
        summary = llm_client.summarize(combined_text)
        return summary
    except Exception as e:
        logging.error(f"Failed to generate summary: {e}")
        return f"Error generating summary: {e}"