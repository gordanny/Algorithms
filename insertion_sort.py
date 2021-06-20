def insertion_sort(A):
    '''Осуществляет сортировку массива A методом вставки'''
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k - 1], A[k] = A[k], A[k - 1]
            k -= 1

    return A

test_massive = ['1', '2', '12', '5', '4', '31', '31', '32']
print(*test_massive)
print(*insertion_sort(test_massive))