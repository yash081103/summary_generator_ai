import os
import json
import logging
from typing import List, Dict

from src.file_processor import FileProcessor
from src.llm_client import LLMClient
from src.summary_generator import generate_overall_summary

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_word_count(text: str) -> int:
    return len(text.strip().split())

def process_text_files(folder_path: str) -> List[Dict]:
    results = []
    all_text_list = []
    file_processor = FileProcessor(folder_path)
    llm_client = LLMClient()

    try:
        for filename in file_processor.get_files():
            text = file_processor.read_file(filename)
            if not text:
                logging.warning(f"Skipping empty or unreadable file: {filename}")
                continue

            word_count = get_word_count(text)
            summary = llm_client.summarize(text)
            reading_level = llm_client.get_reading_level(text)
            all_text_list.append(text)

            results.append({
                "filename": filename,
                "word_count": word_count,
                "summary": summary,
                "reading_level": reading_level,
            })

    except Exception as e:
        logging.error(f"Error processing files: {e}")
        return []

    overall_summary = generate_overall_summary(all_text_list, llm_client)
    results.append({"overall_summary": overall_summary})
    return results

def main(folder_path: str):
    results = process_text_files(folder_path)
    if results:
        print(json.dumps(results, indent=2))
    else:
        print("No results to display (or error occurred).")

if __name__ == "__main__":
    folder_path = "./input_files"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    main(folder_path)
