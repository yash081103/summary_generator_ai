import os
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileProcessor:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logging.info(f"Created input folder: {folder_path}")

    def read_file(self, filename: str) -> str:
        file_path = os.path.join(self.folder_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            return ""
        except Exception as e:
            logging.error(f"Error reading file {file_path}: {e}")
            return ""

    def get_files(self) -> List[str]:
        files = [filename for filename in os.listdir(self.folder_path) if filename.endswith(".txt")]
        if not files:
            logging.warning(f"No .txt files found in: {self.folder_path}")
        return files