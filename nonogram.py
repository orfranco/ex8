##############################################################################
# FILE: nonogram.py
# EXERCISE: intro2cs1 ex8 2020
# DESCRIPTION:
##############################################################################
from typing import List, Optional
"""
def all_options_filtered(n):
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
COLORED_CELL = 1
EMPTY_CELL = 0
UNFILLED_CELL = -1

def constraint_satisfactions(n: int, blocks: List[int]) -> List[List[int]]:
    """
    :param n: the length of the row - positive int.
    :param blocks: the constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of a row with the given constraints. doesn't
            matter the order.
    """
    lst = []
    if blocks and n > 0:
        _helper_constraint_satisfaction(n,blocks, 0, [], lst)
    return lst


def check_space(curr_block, blocks):
    # not with sum because its more efficient.
    sum = 0
    left_blocks_counter = 0
    for i in range(curr_block, len(blocks)):
        sum += blocks[i]
        left_blocks_counter += 1
    return sum + left_blocks_counter-1


def _helper_constraint_satisfaction(n,blocks,curr_block,curr_row,all_opt):
    """

    :param n:
    :param blocks:
    :param curr_block:
    :param curr_row:
    :param all_opt:
    :return:
    """
    # base cases: all cells are filled:
    if len(curr_row) == n:
        all_opt.append(curr_row)
        return

    # check the minimum number of cells needed to match the constraints:
    space_needed = check_space(curr_block, blocks)
    space_to_fill = n - len(curr_row)  # the number of cells left to fill.

    # if all the required blocks were filled, fill the rest of the cells with 0
    if curr_block >= len(blocks):
        curr_row = curr_row + [0] * space_to_fill
        all_opt.append(curr_row)
        return

    # loop through all optional cells that from them
    # we can start filling all left blocks and still match the row length.
    for i in range(space_to_fill - space_needed + 1):
        addition = [0]*i + blocks[curr_block]*[1]
        # add 0 after the block only if its not the end of the row:
        if len(curr_row + addition) < n:
            addition += [0]
        # recursive step:
        _helper_constraint_satisfaction(n, blocks, curr_block+1
                                        , curr_row + addition, all_opt)

    return all_opt


def row_variations(row: List[int], blocks: List[int]) -> List[List[int]]:
    """
    :param row: a list of 1,0,-1 representing the state of the row.
    1 - filled cell.
    0 - empty cell.
    -1 - undefined cell.
    :param blocks: the constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of the undefined cells in the given row
                    with the given constraints.
    """
    lst = []
    # if check_space(0,blocks) > row.count(-1) + row.count(1):
    #     return []
    if blocks and len(row) > 0:
        _helper_row_variations(row, blocks, 0, [], lst,0)
    return lst


def _helper_row_variations(row, blocks, curr_block, curr_row, all_opt, curr_index):

    is_good_for_1 = True
    # will remain false as long as the current block is not done:
    is_good_for_0 = False
    # 1 INSERTED:
    if len(curr_row) > 0 and curr_row[-1]:  # not 0
        pivot_index = get_pivot(curr_row)
        # if current block is completed:
        if (curr_index - pivot_index) == blocks[curr_block]:
            # check if its the end of the row or
            # make sure there isn't an extra 1 after the block:
            if curr_index <= len(row) or row[curr_index] != 1:
                curr_block += 1
                # make sure we only add 0 after we finished a block:
                is_good_for_1 = False
                is_good_for_0 = True
            else:  # found extra 1, this solution is invalid:
                return
    # 0 INSERTED
    else:
        is_good_for_0 = True
        # if the total block size is bigger than the number of
        # remaining cells, the solution is invalid:
        if sum_of_remain_blocks(curr_block, blocks) > count_row_editable_cells(curr_index, row):
            return

    # check if all blocks were inserted:
    if curr_block >= len(blocks):
        # make sure there are no more 1's in the remaining cells,
        # if True the solution is invalid, if False fill rest of cells with 0:
        if find_1_in_row(row, curr_index):
            return
        else:
            curr_row += [0] * (len(row) - curr_index)

    # base case:
    if len(curr_row) == len(row):
        all_opt.append(curr_row)
        return

    # recursive steps:
    if row[curr_index] == UNFILLED_CELL:
        if is_good_for_1:
            _helper_row_variations(row, blocks, curr_block,
                                   curr_row + [COLORED_CELL],
                                   all_opt, curr_index + 1)
        if is_good_for_0:
            _helper_row_variations(row, blocks, curr_block,
                                   curr_row + [EMPTY_CELL],
                                   all_opt, curr_index + 1)
    elif row[curr_index] == COLORED_CELL:
        if is_good_for_1:
            _helper_row_variations(row, blocks, curr_block,
                                   curr_row + [COLORED_CELL],
                                   all_opt, curr_index + 1)
    else:  # if EMPTY_CELL
        if is_good_for_0:
            _helper_row_variations(row, blocks, curr_block,
                                   curr_row + [EMPTY_CELL],
                                   all_opt, curr_index + 1)

    return all_opt


def get_pivot(curr_row):
    pivot_index = len(curr_row)
    for i in range(len(curr_row)-1,-1,-1):
        if curr_row[i] == 0:
            break
        pivot_index -= 1

    return pivot_index


def sum_of_remain_blocks(curr_block, blocks):
    sum = 0

    for i in range(curr_block, len(blocks)):
        sum += blocks[i]
    return sum


def count_row_editable_cells(curr_index,row):
    counter = 0
    for i in range(curr_index,len(row)):
        if row[i] != 0:
            counter+=1
    return counter


def find_1_in_row(row,curr_index):
    for i in range(curr_index,len(row)):
        if row[i] == 1:
            return True
    return False


def intersection_row(rows: List[List[int]]) -> List[int]:
    """
    TODO: explain about the case when a row contains -1.
    :param rows: a List of rows containing 0,1,-1.
    :return: a list representing a row which slices all of the input rows.
    0 - if on all the rows, 0 was on this specific curr_index.
    1 - if on all the rows, 1 was on this specific curr_index.
    -1 - if it was undicisive.
    """
    intersected_row = len(rows[0])*[UNFILLED_CELL]
    for cell in range(len(rows[0])):
        curr_cell_value = rows[0][cell]
        for row in range(len(rows)-1):
            # found rows with different values in the same column:
            if rows[row][cell] != rows[row+1][cell]:
                curr_cell_value = UNFILLED_CELL
        intersected_row[cell] = curr_cell_value
    return intersected_row


def transpose(board):
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]


def solve_easy_nonogram(constraints: List[List[int]]) ->\
                                                Optional[List[List[int]]]:
    """
    possible_rows = constraint_satisfactions(row from constraints[ROW_INDEX]) for every row
    insert_row  = intersection_row(possible_rows)
    board.append(insert_row)
    TODO: think how to get columns from board.
    possible_cols = row_variations(col from board, constraints[COL_INDEX]) for every col
    TODO: think if its the only case where the board is unsolvable.
    """
    row_num = len(constraints[ROW_INDEX])
    col_num = len(constraints[COL_INDEX])
    board = []

    #  Generate raw board from row constraints:
    for block in constraints[ROW_INDEX]:
        possible_rows = constraint_satisfactions(row_num, block)
        board.append(intersection_row(possible_rows))
    print(board)
    board = transpose(board)
    print(board)
    for col_index,block in enumerate(constraints[COL_INDEX]):
        possible_cols = row_variations(board[col_index],block)
        board[col_index] = intersection_row(possible_cols)

    print(board)
    board = transpose(board)
    print(board)
    """
   
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


solve_easy_nonogram([[[2],[1],[2],[4],[4]],[[2],[3],[3],[2,2],[1]]])

