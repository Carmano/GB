import copy


def dublicate_elements(nums: list) -> list:
    my_dict = {}
    for i in set(nums):
        my_dict[i] = my_dict.setdefault(i, nums.count(i))
    return [i for i in my_dict if my_dict[i] >= 2]


def transport(matrix):
    trans_matrix = copy.deepcopy(matrix)
    m = n = len(matrix)
    for i in range(m):
        for j in range(n):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def composite_number():
    a = int(input('Введите число: '))
    result = ''
    if a == 1:
        return 'Число равно task1. А единица не простое и не составное число'
    if a in [2, 3, 5]:
        result = 'Число простое'
    else:
        if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
            result = 'Число составное'
        else:
            result = 'Число простое'
    return result
