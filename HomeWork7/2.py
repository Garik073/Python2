def print_operation_table(operation, num_rows, num_columns):
     for i in range(1, num_rows + 1):
        answer = []
        for j in range(1, num_columns + 1):
           answer.append(str(operation(i, j)))
        print(''.join(f'{e:<4}' for e in answer))

num_rows = int(input("Введите число num_rows: "))
num_columns = int(input("Введите число num_columns: "))
print_operation_table(lambda x, y: x * y,num_rows,num_columns)