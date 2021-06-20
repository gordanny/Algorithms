def z_func(A):
    n = len(A)
    Z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and A[Z[i]] == A[i + Z[i]]:
            Z[i] += 1
        l = i
        r = i + Z[i] - 1

    return Z

print(z_func('abcabcd'))