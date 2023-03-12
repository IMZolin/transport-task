from prettytable import PrettyTable


def answer_calculation(self):
    tp_result = 0
    for i in range(self.basis_solution_matrix.shape[0]):
        for j in range(self.basis_solution_matrix.shape[1]):
            if self.basis_solution_matrix[i][j] is not None:
                tp_result += self.basis_solution_matrix[i][j] * self.weight_matrix[i][j]
    print('Текущие затраты:', tp_result)


def steps_visualisation(self):
    # Color
    R = "\033[0;31;40m"  # RED
    G = "\033[0;32;40m"  # GREEN
    Y = "\033[0;33;40m"  # Yellow
    B = "\033[0;34;40m"  # Blue
    N = "\033[0m"  # Reset
    N = R + G + B

    self.answer_calculation()

    table = PrettyTable()
    table.header = False
    table.add_rows(self.basis_solution_matrix)
    print('Матрица базисных элементов:')
    print(table)

    loop_matrix = self.basis_solution_matrix.copy()
    for i in range(len(self.loop_recalculation)):
        x = self.loop_recalculation[i][0]
        y = self.loop_recalculation[i][1]
        loop_matrix[x][y] = Y + f'{loop_matrix[x][y]}' + N
        if i == 0:
            loop_matrix[x][y] = R + 'NEW' + N
        try:  # try для последнего элемента нужен, чтобы не выходить за границы
            x_next = self.loop_recalculation[i+1][0]
            y_next = self.loop_recalculation[i+1][1]
        except:  # для последнего элемента
            x_next = self.loop_recalculation[0][0]
            y_next = self.loop_recalculation[0][1]

        if x_next == x:  # если переход по строке
            if y_next > y + 1:  # вправо
                for j in range(y + 1, y_next, 1):
                    loop_matrix[x][j] = G + '*' + N
            elif y > y_next + 1:
                for j in range(y_next + 1, y, 1):
                    loop_matrix[x][j] = G + '*' + N
        elif y_next == y:
            if x_next > x + 1:  # вправо
                for j in range(x + 1, x_next, 1):
                    loop_matrix[j][y] = G + '*' + N
            elif x > x_next + 1:
                for j in range(x_next + 1, x, 1):
                    loop_matrix[j][y] = G + '*' + N

    print('Пересчет цикла:')
    table2 = PrettyTable()
    table2.header = False
    table2.add_rows(loop_matrix)
    print(table2)
    print('\n\n')
