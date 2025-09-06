from fastapi import FastAPI
from models import UserInput, InsightResponse
from zodiac_utils import infer_zodiac_sign
from llm_generator import generate_insight
from translation_stub import translate_to_hindi
from cache import get_cached_insight, store_insight

app = FastAPI(title="Astrological Insight Generator")

@app.post("/predict", response_model=InsightResponse)
def get_astrological_insight(user_input: UserInput):
    # Check cache to avoid redundant LLM calls
    cached = get_cached_insight(user_input)
    if cached:
        return cached

    # Infer zodiac from birth date
    zodiac_sign = infer_zodiac_sign(user_input.birth_date)

    # Generate English insight from pseudo-LLM
    english_insight = generate_insight(user_input.name, zodiac_sign)

    # Translate if language is Hindi
    final_insight = (
        translate_to_hindi(english_insight) if user_input.language == "hi" else english_insight
    )

    response = InsightResponse(
        zodiac=zodiac_sign,
        insight=final_insight,
        language=user_input.language
    )

    # Cache response for reuse
    store_insight(user_input, response)
    return response
