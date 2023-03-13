import numpy as np


def find_slau_solution(self):
    self.potential_u = np.zeros(self.basis_solution_matrix.shape[0])
    self.potential_v = np.zeros(self.basis_solution_matrix.shape[1])
    self.potential_u = np.full(self.basis_solution_matrix.shape[0], None)
    self.potential_v = np.full(self.basis_solution_matrix.shape[1], None)
    np.full([self.export_a.shape[0], self.import_b.shape[0]], None)
    for i in range(self.basis_solution_matrix.shape[0]):
        for j in range(self.basis_solution_matrix.shape[1]):
            if self.basis_solution_matrix[i, j] is not None:
                self.potential_u[i] = 0
                self.potential_v[j] = self.weight_matrix[i, j]

                find_in_col(self, j)
                find_in_line(self, i)
                return np.concatenate((self.potential_v, self.potential_u), axis=0)


def find_in_col(self, column: int):
    """I know v"""
    for i in range(self.basis_solution_matrix.shape[0]):
        if (self.basis_solution_matrix[i, column] is not None) & (self.potential_u[i] is None):
            self.potential_u[i] = self.potential_v[column] - self.weight_matrix[i, column]
            find_in_line(self, i)


def find_in_line(self, line: int):
    """I know u"""
    for j in range(self.basis_solution_matrix.shape[1]):
        if (self.basis_solution_matrix[line, j] is not None) & (self.potential_v[j] is None):
            self.potential_v[j] = self.potential_u[line] + self.weight_matrix[line, j]
            find_in_col(self, j)

