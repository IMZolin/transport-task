import numpy as np

from src.transport_problem import TransportProblem


def north_west_method(self):
    i = 0  # начальное положение(1-ый строка, 2-ой столбец)
    j = 0
    while i != len(self.export_a) and j != len(self.import_b):
        min_a_b = min(self.export_a[i], self.import_b[j])
        self.export_a[i] -= min_a_b
        self.import_b[j] -= min_a_b
        self.basis_solution_matrix[i, j] = min_a_b
        if self.export_a[i] > self.import_b[j]:
            j += 1
        elif self.export_a[i] < self.import_b[j]:
            i += 1
        else:
            i += 1
            j += 1


if __name__ == '__main__':
    my_task = TransportProblem()
    my_task.weight_matrix = np.matrix([[14, 7, 4, 8, 3], [9, 2, 2, 12, 10], [17, 7, 9, 11, 10], [13, 7, 12, 14, 5]])
    my_task.export_a = np.array([23, 25, 5, 8])
    my_task.import_b = np.array([20, 10, 12, 7, 12])
    my_task.basis_solution_matrix = np.full([my_task.export_a.shape[0], my_task.import_b.shape[0]], None)
    north_west_method(my_task)
    print(my_task)

