def choice_sort(A):
    '''Осуществляет сортировку массива A методом выбора'''
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A

test_massive = ['1', '2', '12', '5', '4', '31', '31', '32']
print(*test_massive)
print(*choice_sort(test_massive))