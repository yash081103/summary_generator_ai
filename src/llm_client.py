import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLMClient:
    def __init__(self):
        # api_key = os.getenv("GEMINI_API_KEY")
        api_key= "AIzaSyCtZ39IwuZ6iDrVVS8Ng2MBFhmYCcXCiFg"
        print(api_key)
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-2.0-flash")

    def summarize(self, text: str) -> str:
        try:
            prompt = f"Summarize the following text in exactly 100 words:\n\n{text}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logging.error(f"Error during summarization: {e}")
            return "Error generating summary"

    def get_reading_level(self, text: str) -> str:
        try:
            prompt = f"Classify the reading difficulty of this text as 'high' or 'low'if only return in high low or intermediate do not add any other things give one word response\n\n{text}"
            response = self.model.generate_content(prompt)
            return response.text.strip().lower()
        except Exception as e:
            logging.error(f"Error during reading level classification: {e}")
            return "Error determining reading level"
