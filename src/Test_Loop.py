import numpy as np
from transport_problem import TransportProblem


if __name__ == '__main__':
    matrix1 = np.array([[10, None, None, None],
                        [None, 9, 3, None],
                        [None, None, 7, 6],
                        [8, None, None, None],
                        [3, 6, None, None]])
    tp1 = TransportProblem()
    tp1.basis_solution_matrix = matrix1
    tp1.new_basis_variable = np.array([0, 3])
    print(tp1.__dict__)

    tp1.loop_calculation()
    a1 = np.array([[1,2],
                   [3, 4],
                   [5, 6]])
    print([item for item in a1])
    print(([1, 2] == a1).all(1).any())

