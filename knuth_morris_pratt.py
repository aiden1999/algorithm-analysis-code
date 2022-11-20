def compute_knp_next(x: str, m: int):
    k = 0
    kmp_next = [0] * (m + 1)
    kmp_next[0] = -1
    for i in range(1, m):
        if x[i] == x[k]:
            kmp_next[i] = kmp_next[k]
        else:
            kmp_next[i] = k
            while (k >= 0) and (x[i] != x[k]):
                k = kmp_next[k]
        k = k + 1
    kmp_next[m] = k
    return kmp_next

# For workshop 7, ex 3
strings = ["ababa", "abcacabb", "abcacababc", "abacabacab"]
for i in strings:
    print(compute_knp_next(i, len(i)))