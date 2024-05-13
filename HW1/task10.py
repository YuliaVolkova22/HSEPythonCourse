import numpy as np
import scipy.spatial as ss

example = np.array([[12, 3, 8], [9, 3, 1], [2, 2, 2], [3, 10, 1]])

def task10(matrix: np.ndarray) -> np.ndarray:
    dist_matrix = ss.distance_matrix(matrix, matrix)

    print(dist_matrix)

# Пример

task10(example)