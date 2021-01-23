# Класс Матрица
class Matrix:
    def __init__(self, list_matrix: list):
        self.list_matrix = list_matrix

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.list_matrix)

    @staticmethod
    def init_zero_matrix(self):
        zero_matrix = []
        for i in range(len(self.list_matrix)):
            row = []
            for j in range(len(self.list_matrix)):
                row.append(0)
            zero_matrix.append(row)

        return zero_matrix

    def __add__(self, other):

        if len(self.list_matrix) != len(other.list_matrix):
            raise ValueError('Размеры матриц отличаются; сложение невозможно')

        result = self.init_zero_matrix(self)

        for i in range(len(self.list_matrix)):
            for j in range(len(self.list_matrix[0])):
                result[i][j] = self.list_matrix[i][j] + other.list_matrix[i][j]
        return Matrix(result)

matrix_1 = Matrix([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
matrix_2 = Matrix([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
matrix_3 = Matrix([[0, 0, 1], [0, 0, 1], [0, 0, 1]])

print(matrix_1)
print('----------------------------')
print(matrix_2)
print('----------------------------')
print(matrix_3)
print('------------Сумма матриц----------------')
print(matrix_1 + matrix_2 + matrix_3)



