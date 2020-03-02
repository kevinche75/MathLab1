import math
import numpy as np
import os

def read_file_matrix(path: str):

    if not os.path.isfile(path): 
        print("Файла с именем {0} не существует или это не файл".format(path))
        return

    origin_array = np.fromfile(path, sep=" ")

    if origin_array.shape[0] == 0:
        print("Неправильный формат данных")
        return

    matrix_size = int(origin_array[0])
    origin_array = origin_array[1:]

    try:
        origin_array = reshape_array(origin_array, matrix_size)
    except AssertionError as inst:
        print(inst.args[0])
        return

    return origin_array

def reshape_array(origin_array: np.ndarray, matrix_size: int):

    assert matrix_size**2+matrix_size == len(origin_array), "Неправильный формат данных"
    origin_array = np.reshape(origin_array, newshape = (matrix_size, matrix_size + 1))

    return origin_array

def read_console_matrix():

    print("Введите размер матрицы")

    try:
        matrix_size = int(input())
        
        if matrix_size < 1:
            print("Размер матрицы должен быть > 0")
            return
        
        origin_array = np.array([])

        print("Введите {0} строк по {1} элементов, разделённых пробелом".format(matrix_size, matrix_size+1))

        for i in range(matrix_size):

            while(True):
                try:
                    readen_row = np.array(input().split(" "), dtype=float)
                    if readen_row.shape[0] == matrix_size + 1:
                        break
                except ValueError:
                    pass
                print("Неправильный формат строки, строка должна состоять из {0} элементов, разделенных пробелом".format(matrix_size+1))

            origin_array = np.append(origin_array, readen_row)
        origin_array = reshape_array(origin_array, matrix_size)

    except AssertionError as inst:
        print(inst.args[0])
        return
    except ValueError:
        print("Неправильный формат данных")
        return
    return origin_array

def create_random_matrix():

    try:
        print("Введите размер матрицы")
        matrix_size = int(input())
        if matrix_size < 1:
            print("Размер матрицы должен быть > 0")
            return
        print("Введите границу")
        border_value = float(input())
    except ValueError:
        print("Неправильный формат данных")
        return
        
        
    border_value = np.abs(border_value)
    random_matrix = np.random.rand(matrix_size, matrix_size + 1)
    random_matrix = random_matrix * border_value * 2 - border_value
    
    return random_matrix