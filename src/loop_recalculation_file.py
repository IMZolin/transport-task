import numpy as np


def find_new_turn_in_line(self, line: int) -> bool:
    """
    looking for new variable (in line), in which we can make turn, while loop building
    :param line: line to search
    :param self:   TransportProblem
    :return bool - flag, - signals, that loop is found
    """

    for j in range(len(self.basis_solution_matrix[line, :])):  # бежим по строке line и ищем не None
        node = self.basis_solution_matrix[line, j]
        if node is not None:  # если нашел непусту переменную
            if not ([line, j] == self.loop_recalculation).all(1).any():  # и её еще нет в массиве
                self.loop_recalculation = np.append(self.loop_recalculation, [[line, j]], axis=0)
                is_solution_found = find_new_turn_in_column(self, column=j)
                if is_solution_found:
                    return True
        if ([line, j] == self.loop_recalculation[0]).all() & (len(self.loop_recalculation) >= 3):  # проверка на ответ
            return True
    self.loop_recalculation = np.delete(self.loop_recalculation, [-1], axis=0)
    return False


def find_new_turn_in_column(self, column: int) -> bool:
    """
    looking for new variable (in column), in which we can make turn, while loop building
    :param column: column to search
    :param self:   TransportProblem
    :return bool - flag, - signals, that loop is found
    """

    for i in range(len(self.basis_solution_matrix[:, column])):  # бежим по колонке column и ищем не None
        node = self.basis_solution_matrix[i, column]
        if node is not None:  # если нашел непустую переменную
            if not ([i, column] == self.loop_recalculation).all(1).any():  # и её еще нет в массиве
                self.loop_recalculation = np.append(self.loop_recalculation, [[i, column]], axis=0)
                is_solution_found = find_new_turn_in_line(self, line=i)
                if is_solution_found:
                    return True
        if ([i, column] == self.loop_recalculation[0]).all() & (len(self.loop_recalculation) >= 3):  # проверка на ответ
            return True
    self.loop_recalculation = np.delete(self.loop_recalculation, [-1], axis=0)
    return False


def loop_calculation(self):
    self.loop_recalculation = np.array([[self.new_basis_variable[0], self.new_basis_variable[1]]])
    is_found = find_new_turn_in_column(self, self.new_basis_variable[1])
    if not is_found:
        find_new_turn_in_line(self, self.new_basis_variable[1])


