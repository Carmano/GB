import copy


def transport(matrix):
    trans_matrix = copy.deepcopy(matrix)
    m = n = len(matrix)
    for i in range(m):
        for j in range(n):
            trans_matrix[j][i] = matrix[i][j]
    show(trans_matrix)


def show(matrix):
    m = n = len(matrix)
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    show(matrix)
    transport(matrix)
    print()
    # show(matrix)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
