from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        return "Please enter a topic."

    prompt = f"""
Create a structured learning path for: {topic}

Organize it from beginner to advanced.

Include:
1. Prerequisites
2. Beginner concepts
3. Intermediate concepts
4. Advanced concepts
5. A suggested 4-week timeline
6. Practice/project ideas
7. Recommended resource types (videos, articles, books, documentation)

Keep the plan practical and easy to follow.
"""
    return generate_text(
        prompt,
        system_instruction=(
            "You are EduGenie, a personalized learning-path assistant. "
            "Adapt the sequence to a learner who is starting from the basics."
        ),
    )
