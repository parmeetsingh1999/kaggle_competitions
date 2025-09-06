from models import UserInput, InsightResponse
from zodiac_utils import infer_zodiac_sign
from llm_generator import generate_insight
from cache import get_cached_insight, store_insight

user = UserInput(
    name="Parmeet",
    birth_date="1999-02-12",
    birth_time="14:30",
    birth_place="Srinagar, India",
    language="en"
)

z = infer_zodiac_sign(user.birth_date)
ins = generate_insight(user.name, z)

from models import InsightResponse
resp = InsightResponse(zodiac=z, insight=ins, language=user.language)

store_insight(user, resp)
print(get_cached_insight(user).json())
