import random

# Zodiac-based dummy insights
ZODIAC_INSIGHTS = {
    "Aries": [
        "Your energy is contagious today. Take the lead in group settings.",
        "Unexpected opportunities await; be bold and seize the moment."
    ],
    "Taurus": [
        "Stability is your strength. Focus on long-term goals and avoid impulsive decisions.",
        "Your patience will bring success in both personal and professional matters."
    ],
    "Gemini": [
        "Communication is your superpower today. Speak your truth clearly.",
        "Stay curious—new information will help you solve an ongoing problem."
    ],
    "Cancer": [
        "Emotional awareness is key. Connect with family and nurture your space.",
        "Take time for self-care. You may need to recharge emotionally today."
    ],
    "Leo": [
        "Your innate leadership and warmth will shine today. Embrace spontaneity.",
        "Take time to express appreciation to loved ones. Your charm is magnetic."
    ],
    "Virgo": [
        "Details matter—focus on precision and organization today.",
        "Your analytical mind will help others. Offer your support generously."
    ],
    "Libra": [
        "Harmony is within reach. Mediate tensions and restore balance.",
        "Make time for beauty—art, music, or a walk may bring clarity today."
    ],
    "Scorpio": [
        "Trust your instincts. A hidden truth may surface—be ready to face it.",
        "Your intensity is powerful today. Channel it towards creative goals."
    ],
    "Sagittarius": [
        "Adventure is calling. Step outside your routine for inspiration.",
        "An optimistic mindset will attract new opportunities. Stay open."
    ],
    "Capricorn": [
        "Discipline leads to progress. Your efforts will be recognized today.",
        "Set clear goals and take the first step—momentum will follow."
    ],
    "Aquarius": [
        "Innovation is your ally today. Share your ideas boldly.",
        "Be the change-maker in your circle. Your vision can inspire others."
    ],
    "Pisces": [
        "Creativity flows easily now. Express yourself through art or writing.",
        "Empathy will be your guide. Help someone in need today."
    ],
}

def generate_insight(name: str, zodiac: str) -> str:
    """Generate personalized insight using dummy LLM logic."""
    base_insight = random.choice(ZODIAC_INSIGHTS.get(zodiac, ["Embrace the unknown today."]))
    return f"{name}, {base_insight}"
