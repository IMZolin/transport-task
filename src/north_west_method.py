import numpy as np

from src.transport_problem import TransportProblem


def north_west_problem(task: TransportProblem):
    north_west = np.array([0, 0])  # начальное положение(1-ый строка, 2-ой столбец)
    # while north_west[0] <= len(task.export_a) - 1 and north_west[1] <= len(task.import_b) - 1:

    print("Hello")


if __name__ == '__main__':
    weight_matrix = np.matrix([[14, 7, 4, 8, 3], [9, 2, 2, 12, 10], [17, 7, 9, 11, 10], [13, 7, 12, 14, 5]])
    export_a = np.array([23, 25, 5, 8])
    import_b = np.array([20, 10, 12, 7, 12])
    my_task = TransportProblem()
    my_task.weight_matrix = weight_matrix
    print(my_task.weight_matrix)
    print(my_task)
    north_west_problem(my_task)
