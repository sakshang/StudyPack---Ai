# StudyPack AI - Testing and Evaluation

## 1. Testing Objective

The objective of testing was to evaluate whether StudyPack AI could transform lecture notes into structured study material while maintaining source accuracy and following the instructions provided in its prompts.

## 2. Test Cases

### Test Case 1: Machine Learning Notes

- Input: Machine Learning lecture notes.
- Prompt versions tested: V1, V2, V3 and V4.
- Expected result: Summary, key concepts, five MCQs, five short-answer questions and an answer key.
- Observed result: All four versions generated study packs, with improvements in structure and source grounding across iterations.
- Outcome: Completed.

### Test Case 2: Computer Networks Notes

- Input: Computer Networks lecture notes covering networks, protocols and the seven OSI layers.
- Prompt version: V4.
- Expected result: A structured study pack based on the supplied notes.
- Observed result: Relevant summary, key concepts, five MCQs, five short-answer questions and supported answers were generated.
- Outcome: Completed.

### Test Case 3: PDF Input

- Input: PDF lecture notes.
- Expected result: Extract text from the PDF and generate a study pack.
- Observed result: PDF upload, text extraction and study-pack generation worked successfully.
- Outcome: Completed.

## 3. Evaluation Criteria

The generated study packs were reviewed using the following criteria:

1. Accuracy of summaries.
2. Completeness of key concepts.
3. Correct question count and formatting.
4. Correctness of answer keys.
5. Source grounding and prevention of unsupported information.
6. Preservation of technical terminology.
7. Effectiveness of the review stage.

## 4. Limitations Identified

- Generated questions can occasionally be repetitive.
- The AI reviewer may overlook errors.
- The reviewer may report corrections that cannot be verified from the final output alone.
- Testing has been performed on a limited number of sample inputs.
- Further testing with longer and more varied lecture notes is required.

## 5. Conclusion

Testing demonstrated that StudyPack AI can generate structured study material from both pasted text and PDF lecture notes.

The V4 workflow introduced a separate generation and review stage, improving the process of checking generated content against the original notes.

Further testing is necessary before making broader claims about the accuracy and reliability of the application.