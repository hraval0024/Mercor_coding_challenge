from typing import List, Set
from .network import ReferralNetwork

def top_k_by_reach(network: ReferralNetwork, k: int) -> List[str]:
    users = set(network.parent) | set(network.children)
    reach = {u: len(network.all_referrals(u)) for u in users}
    return sorted(reach, key=lambda u: reach[u], reverse=True)[:k]

def _ancestors(network: ReferralNetwork, user: str) -> Set[str]:
    ancestors = set()
    curr = user
    while curr in network.parent:
        curr = network.parent[curr]
        ancestors.add(curr)
    return ancestors

def top_k_by_flow_centrality(network: ReferralNetwork, k: int) -> List[str]:
    users = set(network.parent) | set(network.children)
    descendants = {u: network.all_referrals(u) for u in users}
    ancestors = {u: _ancestors(network, u) for u in users}
    flow = {u: len(ancestors[u]) * len(descendants[u]) for u in users}
    return sorted(flow, key=lambda u: flow[u], reverse=True)[:k]
