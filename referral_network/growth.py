def expected_network_size(p: float, days: int) -> float:
    A = {c: 0.0 for c in range(1, 11)}
    A[10] = 100.0
    expected_successes = 0.0
    for _ in range(days + 1):
        total_active = sum(A.values())
        daily_successes = p * total_active
        expected_successes += daily_successes
        A_next = {c: 0.0 for c in range(1, 11)}
        for c in range(2, 11):
            A_next[c] += A[c] * (1 - p)
            A_next[c - 1] += A[c] * p
        A_next[1] += A[1] * (1 - p)
        A_next[10] += daily_successes
        A = A_next
    return 100 + expected_successes
