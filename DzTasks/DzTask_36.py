def print_operation_table(operation, num_rows, num_columns):
    a = list(j for j in range(1, num_columns + 1))
    b = a
    for i in range(num_rows):
        print(a)
        a = list(map(lambda i, j: i + j, a, b))
print(print_operation_table(lambda x, y: x * y, 6, 6))

