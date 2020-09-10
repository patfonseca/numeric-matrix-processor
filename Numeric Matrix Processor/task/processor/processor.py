import numpy as np


def list_to_array(list):
    for n in range(len(list)):
        for m in range(len(list[0])):
            list[n][m] = float(list[n][m])
    return np.array(list)


def print_result(array):
    print('The result is:')
    for n in range(len(array)):
        row = ''
        for m in range(len(array[0])):
            if array[n][m] != int(array[n][m]):
                row = row + str(array[n][m]) + ' '
            else:
                row = row + str(int(array[n][m])) + ' '
        print(row)


while True:

    print()
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    choice = int(input('Your choice:'))

    if choice in [2, 5, 6]:

        size_a = input('Enter size of matrix:').split()
        matrix_a = []
        print('Enter matrix')
        for n in range(int(size_a[0])):
            matrix_a.append(input().split())

        if choice == 2:  # 2. Multiply matrix by a constant

            constant = float(input('Enter constant:'))
            result = constant * list_to_array(matrix_a)
            print_result(result)

        elif choice == 5:  # 5. Calculate a determinant

            print('The result is:')
            print(round(np.linalg.det(list_to_array(matrix_a)), 2))

        elif choice == 6:  # 6. Inverse matrix

            try:
                result = np.linalg.inv(list_to_array(matrix_a))
                print_result(result)
            except:
                print("This matrix doesn't have an inverse.")


    elif choice == 4:  # 4. Transpose matrix

        print()
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        choice_transpose = int(input('Your choice:'))

        size_a = input('Enter matrix size:').split()
        matrix_a = []
        print('Enter matrix')
        for n in range(int(size_a[0])):
            matrix_a.append(input().split())

        if choice_transpose == 1:  # Main diagonal
            result = list_to_array(matrix_a).transpose()

        elif choice_transpose == 2:  # Side diagonal
            result = np.flipud(np.fliplr(list_to_array(matrix_a).transpose()))

        elif choice_transpose == 3:  # Vertical
            result = np.fliplr(list_to_array(matrix_a))

        elif choice_transpose == 4:  # Horizontal
            result = np.flipud(list_to_array(matrix_a))

        print_result(result)

    elif choice in [1, 3]:  # 1. Add matrices / 3. Multiply matrices

        size_a = input('Enter size of first matrix:').split()
        matrix_a = []
        print('Enter first matrix:')
        for n in range(int(size_a[0])):
            matrix_a.append(input().split())

        size_b = input('Enter size of second matrix:').split()
        matrix_b = []
        print('Enter second matrix:')
        for n in range(int(size_b[0])):
            matrix_b.append(input().split())

        if (choice == 1 and size_a != size_b) or (choice == 3 and size_a[1] != size_b[0]):
            print('The operation cannot be performed.')

        elif choice == 1:
            result = list_to_array(matrix_a) + list_to_array(matrix_b)
            print_result(result)

        elif choice == 3:
            result = list_to_array(matrix_a).dot(list_to_array(matrix_b))
            print_result(result)

    elif choice == 0:  # break
        break
