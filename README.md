# StudyPack AI 📚

**Team:** PromptForge  
**Project ID:** C2 - Lecture Notes to Study Pack

## About

StudyPack AI is a prompt-engineered application that converts lecture notes into structured study material using Google Gemini.

Users can upload PDF lecture notes or paste text directly into the application.

## Features

- PDF upload and text extraction.
- Direct text input.
- Automatic summary generation.
- Key concept extraction.
- Multiple-choice and short-answer questions.
- Answer keys with explanations.
- Two-stage AI workflow involving generation and review.
- Downloadable study packs in Markdown format.

## Technologies

- Python
- Streamlit
- Google Gemini API
- PyMuPDF
- python-dotenv

## Installation

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

4. Run the application:

```bash
streamlit run app.py
```

## Project Structure

```text
Study Pack AI/
├── app.py
├── app_v3_backup.py
├── requirements.txt
├── .gitignore
├── README.md
├── prompts/
├── experiments/
├── tests/
└── documentation/
```

## Prompt Engineering Experiments

The project includes four prompt iterations:

- V1: Baseline generation.
- V2: Structured generation and improved formatting.
- V3: Terminology preservation and distractor constraints.
- V4: Two-stage generation and independent review.

## Testing

The application has been tested using Machine Learning and Computer Networks lecture notes, along with PDF input.

See the `documentation` folder for the architecture, testing and evaluation details, and project synopsis.

## Security

API keys are stored in environment variables and must not be committed to the public repository.

## Project Status

Milestone 2 development and evaluation.