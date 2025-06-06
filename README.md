                                       Text LLM Pipeline
Objective
This project provides a minimal, production-ready Python pipeline that processes text documents using a Large Language Model (LLM) API such as Google's Gemini. It is designed for ease of use, scalability, and clarity, and can be easily extended or adapted for other LLM providers.

Features
Supports single or batch processing of .txt files.

Extracts the following for each text file:

Exact word count.

A 100-word summary (strictly between 90–110 words).

Reading level classification (high or low or intermidiate).

Generates a single, combined 100-word overall summary across all text documents.

Outputs structured results in a JSON file.

Logs pipeline activity and errors to a dedicated log file.

Modular code with clear separation of concerns (file I/O, LLM interaction, summary generation).



Directory Structure
bash
Copy
Edit
text-llm-pipeline/
│
├── input_files/        # Place your .txt files here
├── output/             # Generated output JSON files
├── logs/               # Logs from the pipeline
├── src/
│   ├── file_processor.py
│   ├── llm_client.py
│   └── summary_generator.py
├── .env                # Stores your environment variables (e.g., API keys)
├── main.py             # Entry point to run the pipeline
├── requirements.txt
└── README.md



Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/text-llm-pipeline.git
cd text-llm-pipeline
2. Create and Activate a Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the project root with the following content:

ini
Copy
Edit
GEMINI_API_KEY=your_actual_gemini_api_key
Replace your_actual_gemini_api_key with your valid API key from Google Gemini or the LLM provider you're using.

Usage
Step 1: Place Your Text Files
Put all .txt files you want to process in the input_files/ directory.

Step 2: Run the Pipeline
bash
Copy
Edit
python main.py
Step 3: View the Results
Output JSON: Located in the output/ folder (timestamped).

Logs: Located in the logs/ folder (pipeline.log).

Example Output (JSON)
json
Copy
Edit
[
  {
    "filename": "example.txt",
    "word_count": 253,
    "summary": "This document discusses...",
    "reading_level": "high"
  },
  {
    "overall_summary": "Across the files, common themes include..."
  }
]



Code Quality & Standards
Modular architecture with separation of concerns.

Type hints and docstrings for maintainability.

Logging integrated for transparency and debugging.

Robust error handling to skip invalid files and handle API failures gracefully.

Validates output format (e.g., word count bounds for summaries).

Contributing-
Contributions, feature requests, and bug reports are welcome. Please ensure that all code contributions adhere to the modular structure and include clear commit messages.

