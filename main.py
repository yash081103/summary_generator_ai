import os
import json
import logging
import datetime
from typing import List, Dict
import re

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
          

            
            summary = llm_client.summarize(text)
            summary=parse_json_string(summary)
            print(summary)
            summary["file_name"]= os.path.basename(filename)
            results.append(summary)
            print(results)
            

        

    except Exception as e:
        logging.error(f"Error processing files: {e}")
        return []

    
    return results


def append_to_json_file_with_timestamp(base_dir: str, data: dict):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"results_{timestamp}.json"
    file_path = os.path.join(base_dir, file_name)
    
    # Ensure the directory exists
    os.makedirs(base_dir, exist_ok=True)
    
    # Ensure the data is a list
    if not isinstance(data, list):
        data = [data]
    
    # Write the data to the new file
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"Data saved successfully to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")
def parse_json_string(raw_text: str) -> dict:
    """
    Cleans and parses a raw JSON string, removing code block markers.
    """
    # Remove triple backticks and optional 'json' label
    cleaned = raw_text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[len("```json"):].strip()
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3].strip()

    # Parse the cleaned JSON string
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        print("Offending text:", cleaned)
        return {}

def main(folder_path: str):
    results = process_text_files(folder_path)
    print(results)
    if results:
       append_to_json_file_with_timestamp("output",results)
    else:
        print("No results to display (or error occurred).")

if __name__ == "__main__":
    folder_path = "./input_files"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    main(folder_path)