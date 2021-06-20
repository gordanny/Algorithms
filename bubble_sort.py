def bubble_sort(A):
    '''Осуществляет сортировку массива A методом пузырька'''
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]
    return A

test_massive = ['1', '2', '12', '5', '4', '31', '31', '32']
print(*test_massive)
print(*bubble_sort(test_massive))