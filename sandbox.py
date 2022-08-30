# matrix mul

a = [[1, 2],
     [4, 5],
     [7, 8]]

b = [[1, 2, 3],
     [4, 5, 6]]

print(len(b))
print(len(b[0]))

def get_col(matrix, col_num):
    col = []
    for i in range(len(matrix)):
        col.append(matrix[i][col_num])
    return col


def get_row(matrix, row_num):
    return matrix[row_num]


def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        print("length don't match")

    result = 0
    for i in range(len(vec1)):
        result = result + vec1[i] * vec2[i]


# def matrix_product(m1, m2):


if __name__ == "__main__":
    product = [ [0]*3 for i in range(3)]
