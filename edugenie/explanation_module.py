from gemini_client import generate_text


def explain_topic(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        return "Please enter a topic to explain."

    prompt = f"""
Explain the following educational topic for a beginner:

Topic: {topic}

Requirements:
- Start with a simple definition.
- Explain the main idea using short sections.
- Give one simple real-world example.
- Mention important terms.
- Keep the language clear and concise.
"""
    return generate_text(
        prompt,
        system_instruction=(
            "You are EduGenie, a patient educational assistant. "
            "Explain difficult concepts in simple, accurate language."
        ),
    )
