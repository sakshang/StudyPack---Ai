# Testing and Evaluation – StudyPack AI

## 1. Testing Overview

StudyPack AI was tested to evaluate its ability to generate structured study material from lecture notes provided as text and PDF files.

The testing covered:
- Different academic subjects and note lengths.
- Preservation of technical terminology.
- Generation of summaries, key concepts, and practice questions.
- PDF text extraction.
- Edge cases such as empty input, short input, and scanned PDFs.
- The reliability of the final prompt's review stage.

A total of 10 test cases were conducted.

## 2. Test Cases and Results

| Test ID | Test Input / Scenario | Expected Result | Observed Result | Status |
|---|---|---|---|---|
| 01 | Machine Learning notes | Generate a relevant study pack based on the supplied notes. | The generated study pack was reviewed and found satisfactory. | Pass |
| 02 | Computer Networks notes | Generate structured study material based on the supplied notes. | The output was reviewed and found satisfactory. The experiment evidence is stored in `experiment_5_computer_networks`. | Pass |
| 03 | DBMS notes – longer input | Generate a summary, key concepts, and 10 practice questions. | The output covered the main DBMS concepts and generated 10 questions. The content was largely grounded in the notes. | Pass |
| 04 | Operating Systems notes – technical terminology | Preserve technical terms and their meanings accurately. | Most terminology was retained, but the summary incorrectly stated that system blocks are referred to as deadlocks. | Pass with issue |
| 05 | SDLC notes – definitions and lists | Preserve the SDLC phases and distinguish functional and non-functional requirements. | The output covered all six SDLC phases and generated the expected 10 questions. | Pass |
| 06 | PDF containing selectable lecture text | Extract PDF text and generate a study pack. | PDF text extraction worked and the application generated the study pack successfully. | Pass |
| 07 | Empty input | Display a warning instead of generating a study pack. | The application displayed: `Please provide lecture notes first.` | Pass |
| 08 | Very short input | Reject input that does not contain sufficient lecture content. | The application displayed: `Please provide more lecture content.` | Pass |
| 09 | Scanned/image-only PDF | Handle a PDF with no extractable text without generating fabricated content. | No text was extracted. The application displayed the empty-input warning. OCR is not currently supported. | Safely handled |
| 10 | Cloud Computing notes – insufficient information | Generate a study pack while following the required question count and source-grounding rules. | The output was generated, but it contained only 8 questions instead of the required 10. Some answer-key entries were also marked N/A despite answers being present. | Partial pass |

## 3. Edge-Case Testing

Three important edge cases were tested:

1. **Empty input:** The application displayed a warning and did not attempt to generate a study pack.
2. **Very short input:** The application rejected insufficiently long text with an appropriate warning.
3. **Scanned PDF:** The application safely handled a PDF from which no text could be extracted. However, scanned PDFs are not supported because OCR has not been implemented.

These tests demonstrate that the application handles invalid or unsupported input without proceeding as if valid lecture notes had been supplied.

## 4. Evaluation of Results

The tests demonstrate that StudyPack AI can process lecture notes from different academic subjects and generate structured study material.

The application successfully handled both pasted text and PDFs containing selectable text. It also correctly rejected empty and very short inputs.

However, testing identified some limitations:

- The generated content can occasionally contain unsupported or inaccurate statements, as observed in the Operating Systems test.
- The final review stage does not always identify every issue in the generated study pack.
- The application may generate fewer than the required 10 questions when the source material is limited.
- Scanned PDFs cannot currently be processed because OCR support is not implemented.

The results show that the two-stage generation and review workflow improves the structure and review of generated material, but it does not guarantee complete factual accuracy or strict compliance with every output requirement.

## 5. Conclusion

Overall, the testing confirms that StudyPack AI is a functional prototype capable of converting lecture notes into structured study material.

The application successfully processes supported text and PDF inputs, generates study packs, and handles several invalid-input scenarios. The issues identified during testing provide clear areas for further improvement, particularly in source-grounding, question-count consistency, review reliability, and scanned PDF support.

Further testing and prompt refinement will be carried out in subsequent project milestones.