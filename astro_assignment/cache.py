from typing import Dict
from models import UserInput, InsightResponse

# In-memory cache
_cache: Dict[str, InsightResponse] = {}

def _make_key(user_input: UserInput) -> str:
    return f"{user_input.name}-{user_input.birth_date}-{user_input.language}"

def get_cached_insight(user_input: UserInput):
    return _cache.get(_make_key(user_input))

def store_insight(user_input: UserInput, response: InsightResponse):
    _cache[_make_key(user_input)] = response
