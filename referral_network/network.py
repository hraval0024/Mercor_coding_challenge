from collections import defaultdict
from typing import Iterable, Dict, Set

class ReferralError(ValueError):
    """Custom exception for invalid referrals."""
    pass

class ReferralNetwork:
    """Represents a referral network as a DAG."""

    def __init__(self):
        self.parent: Dict[str, str] = {}
        self.children: Dict[str, Set[str]] = defaultdict(set)

    def add_referral(self, referrer: str, candidate: str) -> None:
        if referrer == candidate:
            raise ReferralError("Self-referrals are not allowed.")
        if candidate in self.parent:
            raise ReferralError("Candidate already has a referrer.")
        curr = referrer
        while curr in self.parent:
            curr = self.parent[curr]
            if curr == candidate:
                raise ReferralError("Cycle detected.")
        self.parent[candidate] = referrer
        self.children[referrer].add(candidate)

    def direct_referrals(self, user: str) -> Iterable[str]:
        return iter(self.children.get(user, set()))

    def all_referrals(self, user: str) -> Iterable[str]:
        result = set()
        stack = list(self.children.get(user, []))
        while stack:
            node = stack.pop()
            if node not in result:
                result.add(node)
                stack.extend(self.children.get(node, []))
        return result
