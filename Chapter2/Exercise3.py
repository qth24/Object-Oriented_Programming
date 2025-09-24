def input_matrix(r, c):
    m = []
    for i in range(r):
        row = list(map(int, input().split()))
        m.append(row)
    return m

def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def sub_matrix(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mul_matrix(a, b):
    r, c, k = len(a), len(b[0]), len(b)
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(c)] for i in range(r)]

r1, c1 = map(int, input("Enter rows, cols of matrix A: ").split())
a = input_matrix(r1, c1)
r2, c2 = map(int, input("Enter rows, cols of matrix B: ").split())
b = input_matrix(r2, c2)

if r1 == r2 and c1 == c2:
    print("Sum: ", add_matrix(a, b))
    print("Difference: ", sub_matrix(a, b))
else:
    print("Sum/Diff not possible")

if c1 == r2:
    print("Product: ", mul_matrix(a, b))
else:
    print("Product not possible")
