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


