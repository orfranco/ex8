##############################################################################
# FILE: nonogram.py
# EXERCISE: intro2cs1 ex8 2020
# DESCRIPTION:
##############################################################################
from typing import List, Optional
"""def all_options_filtered(n):
    if n == 0:
        return []
    if n == 1:
        return ['0','1']

    options = []
    for opt in all_options_filtered(n-1):
        if opt[-1] != '1':
            options.append(opt+'1')
        options.append(opt+'0')
    return options

"""
ROW_INDEX = 0
COL_INDEX = 1


def constraint_satisfactions(n: int, blocks: List[int]) -> List[List[int]]:
    """
    TODO: remember not to change the blocks List.
    TODO: what to do when blocks is empty?
    :param n: the length of the row - positive int.
    :param blocks: the constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of a row with the given constraints. doesn't
            matter the order.
    """


def row_variations(row: List[int], blocks: List[int]) -> List[List[int]]:
    """
    TODO: remember not to change the blocks and row Lists.
    TODO: return [] when there aren't any options.
    TODO: what to do when row or blocks is empty?
    TODO: how to be efficient has possible?
    :param row: a list of 1,0,-1 representing the state of the row.
    1 - filled cell.
    0 - empty cell.
    -1 - undefined cell.
    :param blocks: the constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of the undefined cells in the given row
                    with the given constraints.
    """


def intersection_row(rows: List[List[int]]) -> List[int]:
    """
    TODO: think about the case when a row contains -1. on our implementation, doesn't suppose to happen.
    TODO: do not change rows.
    TODO: assume that all rows with the same length.
    :param rows: a List of rows containing 0,1,-1.
    :return: a list representing a row which slices all of the input rows.
    0 - if on all the rows, 0 was on this specific index.
    1 - if on all the rows, 1 was on this specific index.
    -1 - if it was undicisive.
    """


def solve_easy_nonogram(constraints: List[List[int], List[int]]) ->\
                                                Optional[List[List[int]]]:
    """
    possible_rows = constraint_satisfactions(row from constraints[ROW_INDEX]) for every row
    insert_row  = intersection_row(possible_rows)
    board.append(insert_row)
    TODO: think how to get columns from board.

    possible_cols = row_variations(col from board, constraints[COL_INDEX]) for every col
    TODO: think if its the only case where the board is unsolvable.
    if possible_cols == []:
        return None
    else:
        insert_col  = intersection_row(possible_cols)
    board2.append(insert_col)
    TODO: insert as rows.
    TODO: think about an efficient way to update the board.
    bool is_changed = False
    possible_rows = row_variations(row from board, constraints[ROW_INDEX]) for every row
    if possible_rows == []:
        return None
    else:
        insert_row  = intersection_row(possible_rows)
    if insert_row != row from board:
        is_changed = True
    board3.append(insert_col)
    TODO: the same for columns until the row that is returned is the same as the given, for all rows and columns.
    :param constraints:
    :return:
    """




