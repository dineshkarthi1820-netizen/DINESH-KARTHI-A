from gemini_client import generate_text


def summarize_text(text: str) -> str:
    text = text.strip()
    if not text:
        return "Please enter text to summarize."

    prompt = f"""
Summarize the following educational passage.

PASSAGE:
{text}

Requirements:
- Keep the core facts and meaning.
- Remove repetition and unnecessary detail.
- Use short paragraphs or bullet points.
- Make it suitable for quick revision.
"""
    return generate_text(
        prompt,
        system_instruction="You are an educational summarization assistant. Preserve important meaning and context.",
    )
