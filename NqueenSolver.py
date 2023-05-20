import time
import numpy as np
import random as rm
import math


def find_best_move(heuristic_table):
    return np.argmin(heuristic_table, 0)


def find_is_optimal(heuristic_table):
    return np.all(np.min(heuristic_table, 0) == False)


def show_rep_attr(repetition, random_restart_num, end_time, starting_time, chess_table, displacement_num):
    print(f"Random restart for {repetition} repetition:", random_restart_num)
    print("Completion time:", end_time - starting_time, "sn")
    print("Displacement number on the table:", displacement_num)
    print("------------------------------------------------")
    print(f"Solution\n{chess_table}\n")


class NQueenSolver:
    def __init__(self, table_size):
        self.table_size = table_size

    def random_start_table(self):
        table = np.zeros((self.table_size, self.table_size), dtype=int)
        for i in range(self.table_size):
            table[rm.randint(0, self.table_size - 1)][i] = 1

        return table

    def climb_hill(self):
        repetition, random_restart_num, displacement_num = 0, 0, 0
        starting_time = time.time()

        while repetition < 9:
            chess_table = self.random_start_table()
            for i in range(self.table_size):
                displacement_num += self.set_best_move(i, chess_table)

            if find_is_optimal(self.calculate_heuristic(chess_table)):
                repetition += 1
                show_rep_attr(repetition, random_restart_num, time.time(), starting_time, chess_table,
                                   displacement_num)
                random_restart_num, displacement_num = 0, 0
                starting_time = time.time()
            else:
                random_restart_num += 1
                displacement_num = 0

    def set_best_move(self, i, chess_table):
        heuristic_table = self.calculate_heuristic(chess_table)
        current_index = np.where(chess_table[:, i] == 1)
        best_move = find_best_move(heuristic_table[:self.table_size, i:i + 1])
        self.reset_column(i, chess_table)
        chess_table[best_move, i] = 1
        return abs(current_index - best_move)[0, 0]

    def reset_column(self, i, table):
        table[:self.table_size, i:i + 1] = 0

    def calculate_heuristic(self, chess_table):
        heuristic_table = self.create_heuristic_table()
        for i in range(self.table_size):
            copy_table = chess_table.copy()
            for j in range(self.table_size):
                heuristic = 0
                self.reset_column(i, copy_table)  # reset copy table
                copy_table[j, i] = 1  # move the queen along the column
                heuristic += self.check_verticals(
                    copy_table)  # add the value of queens that threat each other at vertical plane
                heuristic += self.check_diagonals(
                    copy_table)  # add the value of queens that threat each other at diagonal plane
                heuristic_table[j, i] = heuristic  # set heuristic value

        return heuristic_table

    def check_verticals(self, table):
        threat = 0
        for i in range(self.table_size):
            # find the value of queens that threat each other at vertical plane
            row_piece_num = np.count_nonzero(table[i] == 1)
            threat += math.comb(row_piece_num, 2)

        return threat

    def check_diagonals(self, table):
        reversed_table = np.flip(table, 1)  # reverse the axis x
        # check diagonals for threatening queens each other
        diagonal_heuristic = self.check_upper_diagonal(np.triu(table)) \
                             + self.check_lower_diagonal(np.tril(table, -1)) \
                             + self.check_upper_diagonal(np.triu(reversed_table)) \
                             + self.check_lower_diagonal(np.tril(reversed_table, -1))

        return diagonal_heuristic

    def check_upper_diagonal(self, table):
        threat = 0
        for i in range(self.table_size):
            piece_num = 0
            row = 0
            for j in range(i, self.table_size):
                piece_num += table[row, j]
                row += 1
            threat += math.comb(piece_num, 2)

        return threat

    def check_lower_diagonal(self, table):
        threat = 0
        for i in range(1, self.table_size):
            piece_num = 0
            row = i
            for j in range(self.table_size - i):
                piece_num += table[row, j]
                row += 1
            threat += math.comb(piece_num, 2)

        return threat

    def create_heuristic_table(self):
        heuristic_table = np.zeros((self.table_size, self.table_size), dtype=int)
        return heuristic_table
