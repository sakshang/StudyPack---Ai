import os
import streamlit as st
import fitz  # PyMuPDF
from dotenv import load_dotenv
from google import genai

# -----------------------------
# 1. CONFIGURATION
# -----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-3.1-flash-lite"

st.set_page_config(
    page_title="StudyPack AI",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# 2. GEMINI CONNECTION
# -----------------------------

@st.cache_resource
def get_gemini_client():
    if not API_KEY:
        raise ValueError(
            "Gemini API key not found. Check your .env file."
        )

    return genai.Client(api_key=API_KEY)


# -----------------------------
# 3. PDF TEXT EXTRACTION
# -----------------------------

def extract_pdf_text(pdf_file):
    document = fitz.open(
        stream=pdf_file.getvalue(),
        filetype="pdf"
    )

    pages = []

    for page in document:
        pages.append(page.get_text())

    document.close()

    return "\n".join(pages)


# -----------------------------
# 4. STUDY PACK GENERATION (V3)
# -----------------------------

def create_study_pack(notes):

    prompt = f"""
You are StudyPack AI, an academic study assistant.

Your task is to transform the supplied lecture notes into an accurate,
structured study pack for university students.

STRICT SOURCE AND TERMINOLOGY RULES:
1. Use only information contained in the supplied lecture notes.
2. Preserve the original technical terminology.
3. Do not introduce external facts, examples, definitions, or assumptions.
4. Do not invent information to fill gaps.
5. If information is unavailable, state:
   "Not covered in the supplied notes."
6. Simplify sentence structure without changing the original meaning.

SECTION 1: SUMMARY
- Write a concise summary covering all major topics.
- Preserve the terminology used in the notes.
- Do not add unsupported information.

SECTION 2: KEY CONCEPTS
- Identify important concepts.
- Explain each using only the supplied notes.
- Retain original technical terms.
- Do not invent examples.

SECTION 3: PRACTICE QUESTIONS

Generate exactly 10 questions:
- Questions 1–5: Multiple-choice questions.
- Questions 6–10: Short-answer questions.

For every MCQ:
- Provide exactly four options (A, B, C, D).
- Ensure exactly one option is correct.
- Base the correct answer on the notes.
- Use distractors derived from concepts or information in the notes.
- Do not introduce unrelated technical terms or external facts.
- Avoid ambiguous wording.

For short-answer questions:
- Ask questions answerable directly from the notes.
- Do not ask for information absent from the notes.

SECTION 4: ANSWER KEY
- Provide answers to all 10 questions.
- Include brief explanations.
- Identify supporting information from the notes.
- Do not provide unsupported answers.

SECTION 5: QUALITY CHECK

Verify before responding:
1. Are all major topics covered?
2. Is the original terminology preserved?
3. Are there exactly 10 questions?
4. Does every MCQ have four options?
5. Is there exactly one correct answer per MCQ?
6. Are distractors relevant to the notes?
7. Are all answers supported?
8. Have external facts or unsupported examples been introduced?

Correct any issues identified before presenting the final response.

LECTURE NOTES:

{notes}
"""

    client = get_gemini_client()

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text


# -----------------------------
# 5. APPLICATION INTERFACE
# -----------------------------

st.title("📚 StudyPack AI")

st.write(
    "Transform your lecture notes into organized "
    "study material using AI."
)

st.divider()

st.subheader("Upload or enter your lecture notes")

input_method = st.radio(
    "Choose your input method:",
    ["Upload PDF", "Paste Text"],
    horizontal=True
)

notes = ""

if input_method == "Upload PDF":

    uploaded_file = st.file_uploader(
        "Upload your lecture notes",
        type=["pdf"]
    )

    if uploaded_file is not None:
        try:
            notes = extract_pdf_text(uploaded_file)

            st.success("PDF uploaded successfully!")

            with st.expander("Preview extracted text"):
                st.text(notes[:5000])

        except Exception as error:
            st.error(f"Could not read the PDF: {error}")

else:

    notes = st.text_area(
        "Paste your lecture notes here:",
        height=250,
        placeholder="Paste your lecture notes..."
    )

st.divider()

if st.button(
    "✨ Generate Study Pack",
    type="primary",
    use_container_width=True
):

    if not notes or not notes.strip():

        st.warning("Please provide lecture notes first.")

    elif len(notes.strip()) < 50:

        st.warning("Please provide more lecture content.")

    elif len(notes) > 30000:

        st.warning(
            "Your notes are too long for this initial version. "
            "Please use a shorter document."
        )

    else:

        try:
            with st.spinner(
                "StudyPack AI is generating your study material..."
            ):

                result = create_study_pack(notes)

            st.session_state["study_pack"] = result

            st.success("Your study pack is ready!")

        except Exception as error:

            st.error(f"Something went wrong: {error}")


# -----------------------------
# 6. DISPLAY GENERATED OUTPUT
# -----------------------------

if "study_pack" in st.session_state:

    st.divider()

    st.header("Your Generated Study Pack")

    st.markdown(st.session_state["study_pack"])

    st.download_button(
        label="⬇️ Download Study Pack",
        data=st.session_state["study_pack"],
        file_name="StudyPack.md",
        mime="text/markdown",
        use_container_width=True
    )

    if st.button("Clear Study Pack"):

        del st.session_state["study_pack"]

        st.rerun()

