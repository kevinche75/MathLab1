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
    try:
        matrix_size = int(input())
        if matrix_size < 1:
            print("Размер матрицы должен быть > 0")
            return
        origin_array = np.array([])
        print(matrix_size)
        for i in range(matrix_size):
            a = np.array(input().split(" "), dtype=float)
            print(a)
            origin_array = np.append(origin_array, a)
        origin_array = reshape_array(origin_array, matrix_size)
    except AssertionError as inst:
        print(inst.args[0])
        return
    except ValueError as inst:
        print("Неправильный формат данных")
        return
    return origin_array