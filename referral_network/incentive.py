from functools import lru_cache
from typing import Optional
from .growth import expected_network_size

def min_bonus_for_target(days: int, target_network_size: int, adoption_prob) -> Optional[int]:
    @lru_cache(None)
    def expected_size_for_bonus(bonus: int) -> float:
        return expected_network_size(adoption_prob(bonus), days)

    lo, hi = 0, 10_000
    answer = None
    while lo <= hi:
        mid = ((lo + hi) // 20) * 10
        if expected_size_for_bonus(mid) >= target_network_size:
            answer = mid
            hi = mid - 10
        else:
            lo = mid + 10
    return answer
