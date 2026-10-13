import json
import re
from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str):
    passage = passage.strip()
    if not passage:
        return {"error": "Please enter a topic or passage."}

    prompt = f"""
Create exactly 3 multiple-choice questions from the educational text below.

TEXT:
{passage}

Return ONLY valid JSON with this exact structure:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

The answer must exactly match one of the four option strings.
Make the questions relevant to the supplied text and make the distractors plausible.
"""
    try:
        raw = generate_text(
            prompt,
            system_instruction="You create clear educational quizzes and must follow JSON formatting exactly.",
        )
        data = json.loads(clean_json_block(raw))

        if not isinstance(data, list) or len(data) != 3:
            raise ValueError("The model did not return exactly 3 questions.")

        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Invalid question object.")
            if not all(k in item for k in ("question", "options", "answer")):
                raise ValueError("Missing question fields.")
            if len(item["options"]) != 4:
                raise ValueError("Each question must have 4 options.")
            if item["answer"] not in item["options"]:
                raise ValueError("Answer must be one of the options.")

        return data
    except Exception as exc:
        return {"error": f"Quiz generation failed: {exc}"}
