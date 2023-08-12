# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])

    def __eq__(self, other):
        """
        Сравниваем длину и ширину матриц, если они разные выводим False, в ином случая сравниваем элементы матриц,
        и если хоть один элемент матрицы 1 отличается от элемента матрицы 2 выводить False. Если все элементы равны вернуть True
        """
        if self.height == other.height and self.width == other.width:
            for i in range(self.height):
                for j in range(self.width):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        if self.height == other.height and self.width == other.width:
            new_matrix = []
            for i in range(self.height):
                row = []
                for j in range(self.width):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                new_matrix.append(row)
            return Matrix(new_matrix)
        else:
            raise ValueError('Длинны не соответсвуют')

    def show_matrix(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.matrix[i][j], end=' ')
            print()
        print()

    def __mul__(self, other):
        # if self.width != other.height:
        #     raise ValueError("Матрицы имеют некорректные размеры для умножения")

        matrix = []
        for i in range(self.height):
            row = []
            for j in range(other.width):
                element = 0
                for k in range(other.height):
                    element += self.matrix[i][k] * other.matrix[k][j]
                row.append(element)
            matrix.append(row)

        return Matrix(matrix)


data1 = [[1, 2], [3, 4]]
data2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data3 = [[1, 2], [3, 4], [5, 6]]
data4 = [[1, 2], [3, 4]]

matrix1 = Matrix(data1)
matrix1.show_matrix()

matrix2 = Matrix(data2)
matrix2.show_matrix()

# matrix3 = matrix1 + matrix2
# matrix3.show_matrix()
#
# if matrix1 == matrix2:
#     print('equal')
# else:
#     print('not equal')

matrix4 = matrix1 * matrix2

matrix4.show_matrix()
