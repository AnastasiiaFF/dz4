"""
Напишите функцию для транспонирования матрицы
"""

def matrix_transposition(matrix: list) -> list:
    """ Возвращает транспонированную матрицу"""
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]  # структура транспонированной матцы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(matrix)

    for row in matrix_transposition(matrix):
        print(row)
