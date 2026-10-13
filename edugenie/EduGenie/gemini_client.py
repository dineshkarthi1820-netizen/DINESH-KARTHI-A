import os
from functools import lru_cache
from google import genai
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
MODEL_CANDIDATES = [
    DEFAULT_MODEL,
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-3.5-flash",
]
MODEL = DEFAULT_MODEL


@lru_cache(maxsize=1)
def get_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key.startswith("PASTE_"):
        raise RuntimeError(
            "GEMINI_API_KEY is missing or still contains the placeholder value. Add your real key to the .env file."
        )
    return genai.Client(api_key=api_key)


def generate_text(prompt: str, system_instruction: str | None = None) -> str:
    client = get_client()

    config = None
    if system_instruction:
        from google.genai import types
        config = types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.4,
        )

    last_error = None
    for model_name in MODEL_CANDIDATES:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=config,
            )
            text = getattr(response, "text", None)
            if not text:
                raise RuntimeError("Gemini returned an empty response.")
            return text.strip()
        except Exception as exc:
            last_error = exc
            message = str(exc).lower()
            if "model" not in message and "404" not in message and "not found" not in message:
                raise RuntimeError(f"Gemini request failed: {exc}") from exc

    raise RuntimeError(
        "The configured Gemini model is unavailable. Set GEMINI_MODEL to a model supported by your account, such as gemini-2.5-flash, gemini-2.0-flash, or gemini-1.5-flash."
    ) from last_error
