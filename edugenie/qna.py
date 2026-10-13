from gemini_client import generate_text


def answer_question(question: str) -> str:
    question = question.strip()
    if not question:
        return "Please enter a question."

    prompt = f"""
Answer this student's question:

{question}

Rules:
- Give the direct answer first.
- Explain the reasoning briefly when useful.
- Use simple language.
- If the question is ambiguous, state the assumption you are making.
- Do not invent sources or facts.
"""
    return generate_text(
        prompt,
        system_instruction=(
            "You are EduGenie, an educational Q&A assistant. "
            "Be accurate, concise, and useful for students."
        ),
    )
