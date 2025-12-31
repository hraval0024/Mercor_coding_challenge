from collections import defaultdict
from typing import Iterable, Dict, Set

class ReferralError(ValueError):
    """Invalid Referrals Exception."""
    pass

class ReferralNetwork:
    """creating DAG of referrals"""

    def __init__(self):
        self.parent: Dict[str, str] = {}
        self.children: Dict[str, Set[str]] = defaultdict(set)

    def add_referral(self, referrer: str, candidate: str) -> None:
        # check for self referral
        if referrer == candidate:
            raise ReferralError("Self-referrals are not allowed.")

        # check for existing referral
        if candidate in self.parent:
            raise ReferralError("Candidate already been referred.")
        
        # check for cycles
        curr = referrer
        while curr in self.parent:
            curr = self.parent[curr]
            if curr == candidate:
                raise ReferralError("Cycle detected.")

        # if no rule violation, add the referral
        self.parent[candidate] = referrer
        self.children[referrer].add(candidate)

    def direct_referrals(self, user: str) -> Iterable[str]:
        # get all the values associated with the user key in children dictionary
        return iter(self.children.get(user, set()))

    def all_referrals(self, user: str) -> Iterable[str]:
        # using dfs to get all referrals
        result = set()
        stack = list(self.children.get(user, []))
        while stack:
            node = stack.pop()
            if node not in result:
                result.add(node)
                stack.extend(self.children.get(node, []))
        return result
