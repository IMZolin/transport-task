import numpy as np

def north_west_method(self):
    i = 0  # начальное положение(1-ый строка, 2-ой столбец)
    j = 0
    self.basis_solution_matrix = np.full([self.export_a.shape[0], self.import_b.shape[0]], None)
    exp_a_copy = self.export_a.copy()
    imp_b_copy = self.import_b.copy()
    while i != len(self.export_a) and j != len(self.import_b):
        min_a_b = min(self.export_a[i], self.import_b[j])
        exp_a_copy[i] -= min_a_b
        imp_b_copy[j] -= min_a_b
        self.basis_solution_matrix[i, j] = min_a_b
        if exp_a_copy[i] > imp_b_copy[j]:
            j += 1
        elif exp_a_copy[i] < imp_b_copy[j]:
            i += 1
        else:
            try:
                self.basis_solution_matrix[i + 1, j] = 0
            except:
                pass
            i += 1
            j += 1


