import os
import logging
import google.generativeai as genai
import re
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLMClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_flash__API_KEY")
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-2.0-flash")

    def summarize(self, text: str) -> str:
        try:
            prompt = f"""
You are a text analysis system. Read the given text and respond ONLY in strict JSON format without any commentary or formatting. Do not include markdown.

Expected JSON format:
{{
  "word_count": <int>,
  "summary": "<summary in 90 to 110 words>",
  "reading_level": "high" or "low"
}}

Text:
\"\"\"{text}\"\"\"
"""
   

            response = self.model.generate_content(prompt)
            print(response.candidates[0].content.parts[0].text.strip())
            return response.candidates[0].content.parts[0].text.strip()
        except Exception as e:
            logging.error(f"Error during summarization: {e}")
            return "Error generating summary"

    # def get_reading_level(self, text: str) -> str:
    #     try:
    #         prompt = f"Classify the reading difficulty of this text as 'high' or 'low'if only return in high low or intermediate do not add any other things give one word response\n\n{text}"
    #         response = self.model.generate_content(prompt)
    #         return response.text.strip().lower()
    #     except Exception as e:
    #         logging.error(f"Error during reading level classification: {e}")
    #         return "Error determining reading level"
