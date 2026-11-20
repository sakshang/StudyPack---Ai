# STUDYPACK AI
## Project Synopsis

**Team Name:** PromptForge  
**Project ID:** C2 - Lecture Notes to Study Pack  
**Project Category:** Prompt Engineering

### 1. Introduction

Students often work with lengthy lecture notes when preparing for examinations. Manually extracting important concepts, preparing summaries and creating practice questions can be time-consuming.

StudyPack AI is a prompt-engineered application designed to transform lecture notes into structured study material.

### 2. Problem Statement

Students need an efficient way to convert lecture notes into concise and organized revision material. Generic AI-generated content may also introduce unsupported information or alter technical terminology.

### 3. Proposed Solution

StudyPack AI accepts lecture notes through PDF uploads or pasted text. It uses carefully designed prompts to generate:

- Concise summaries.
- Important concepts and definitions.
- Multiple-choice questions.
- Short-answer questions.
- Answer keys with explanations and supporting information.

The V4 implementation uses a two-stage Gemini workflow. The first stage generates the study pack, while the second reviews the generated content against the original notes and produces a corrected version.

### 4. Technologies Used

- Python - Application development.
- Streamlit - User interface.
- Google Gemini API - AI-powered generation and review.
- PyMuPDF - PDF text extraction.
- python-dotenv - Environment variable management.

### 5. Prompt Engineering Approach

The project follows an iterative prompt-engineering process involving four versions:

- V1: Baseline generation.
- V2: Improved structure and question formatting.
- V3: Stronger terminology and source-grounding constraints.
- V4: Two-stage generation and review workflow.

The versions were tested using consistent Machine Learning notes, followed by additional testing with Computer Networks notes.

### 6. Testing and Evaluation

The application was tested using two academic subjects and PDF input.

Evaluation focused on summary quality, concept extraction, question formatting, answer correctness, source grounding and terminology preservation.

### 7. Expected Outcome

The expected outcome is a working application that helps students convert lecture notes into organized revision material while encouraging source-grounded AI generation and review.

### 8. Future Scope

Potential improvements include:
- Testing with larger and more diverse lecture documents.
- Improving question diversity.
- Strengthening independent answer verification.
- Adding more customizable study-pack formats.
- Improving the user interface and document handling.

### 9. Conclusion

StudyPack AI demonstrates how iterative prompt engineering and a separate AI review stage can be combined to build an educational application. The project emphasizes structured generation, source grounding and continuous evaluation.