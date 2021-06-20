def p_func(S):
    n = len(S)
    P = [0] * n
    for i in range(1, n):
        P[i] = P[i - 1]
        while P[i] > 0 and S[i] != S[P[i]]:
            P[i] -= 1
        if S[i] == S[P[i]]:
            P[i] += 1
    return P
print(p_func('abcabcd'))