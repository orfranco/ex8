##############################################################################
# FILE: nonogram.py
# EXERCISE: intro2cs1 ex8 2020
# DESCRIPTION:
##############################################################################
from typing import List, Optional

# Constants:
ROW_INDEX = 0
COL_INDEX = 1
COLORED_CELL = 1
EMPTY_CELL = 0
UNFILLED_CELL = -1


def constraint_satisfactions(n: int, blocks: List[int]) -> List[List[int]]:
    """
    TODO: add general description
    :param n: the length of the row - positive int.
    :param blocks: the constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of a row with the given constraints. doesn't
            matter the order.
    """
    lst: List = []

    if n > 0:
        _helper_constraint_satisfaction(n,blocks, 0, [], lst)

    return lst


def check_space(curr_block: int, blocks: List[int]) -> int:
    # TODO: Add docstring
    # not with sum because its more efficient.
    summ: int = 0
    left_blocks_counter = 0

    for i in range(curr_block, len(blocks)):
        summ += blocks[i]
        left_blocks_counter += 1

    return summ + left_blocks_counter-1


def _helper_constraint_satisfaction(n, blocks, curr_block, curr_row, all_opt):
    """
    TODO: add general description
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
    TODO: add general description
    TODO: blocks contain [-1]?
    :param row: a list of 1,0,-1 representing the state of the row.
    1 - filled cell.
    0 - empty cell.
    -1 - undefined cell.
    :param blocks: the constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of the undefined cells in the given row
                    with the given constraints.
    """
    lst: List = []

    if len(row) > 0:
        _helper_row_variations(row, blocks, 0, [], lst, 0)

    return lst


def _helper_row_variations(row, blocks, curr_block, curr_row, all_opt, curr_index):
    # TODO: Add docstring.
    # TODO: Add type hints.
    is_good_for_1 = True
    # Will remain false as long as the current block is not done:
    is_good_for_0 = False

    # 1 was Inserted:
    if len(curr_row) > 0 and curr_row[-1]:  # not 0
        pivot_index = get_pivot(curr_row)
        # If current block is completed:
        if (curr_index - pivot_index) == blocks[curr_block]:
            # Check if its the end of the row,
            # Or make sure there isn't an extra 1 after the block:
            if curr_index <= len(row) or row[curr_index] != 1:
                curr_block += 1
                # Make sure we only add 0 after we finished a block:
                is_good_for_1 = False
                is_good_for_0 = True
            else:  # Found extra 1, this solution is invalid:
                return

    # 0 was Inserted
    else:
        is_good_for_0 = True
        # if the total block size is bigger than the number of
        # remaining cells, the solution is invalid:
        if sum_of_remaining_blocks(curr_block, blocks) >\
                count_row_editable_cells(curr_index, row):
            return

    # Check if all blocks were inserted:
    if curr_block >= len(blocks):
        # Make sure there are no more 1's in the remaining cells,
        # If True the solution is invalid, if False fill rest of cells with 0:
        if find_1_in_row(row, curr_index):
            return
        else:
            curr_row += [0] * (len(row) - curr_index)

    # Base case:
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


def get_pivot(curr_row: List[int]) -> int:
    """
    TODO: add general description
    :param curr_row:
    :return:
    """
    pivot_index = len(curr_row)

    for i in range(len(curr_row) - 1, -1, -1):
        if curr_row[i] == 0:
            break

        pivot_index -= 1

    return pivot_index


def sum_of_remaining_blocks(curr_block: int, blocks: List[int]) -> int:
    """
    TODO: add general description
    :param curr_block:
    :param blocks:
    :return:
    """
    summ: int = 0

    for i in range(curr_block, len(blocks)):
        summ += blocks[i]

    return summ


def count_row_editable_cells(curr_index: int, row: List[int]) -> int:
    """
    TODO: add general description
    :param curr_index:
    :param row:
    :return:
    """
    counter = 0

    for i in range(curr_index, len(row)):
        if row[i] != 0:
            counter += 1

    return counter


def find_1_in_row(row, curr_index):
    # TODO: Add docstring.
    # TODO: Add type hints.
    for i in range(curr_index, len(row)):
        if row[i] == 1:
            return True

    return False


def intersection_row(rows: List[List[int]]) -> List[int]:
    """
    TODO: explain about the case when a row contains -1.
    # TODO: Add general description.
    :param rows: a List of rows containing 0,1,-1.
    :return: a list representing a row which slices all of the input rows.
    0 - if on all the rows, 0 was on this specific curr_index.
    1 - if on all the rows, 1 was on this specific curr_index.
    -1 - if it was undicisive.
    """
    intersected_row = len(rows[0]) * [UNFILLED_CELL]

    for cell in range(len(rows[0])):
        curr_cell_value = rows[0][cell]

        for row in range(len(rows)-1):
            # found rows with different values in the same column:
            if rows[row][cell] != rows[row+1][cell]:
                curr_cell_value = UNFILLED_CELL

        intersected_row[cell] = curr_cell_value

    return intersected_row


def transpose(board: List[List[int]]) -> List[List[int]]:
    # TODO: Add docstring.
    return [[board[j][i] for j in range(len(board))]
            for i in range(len(board[0]))]

def update_line(line, blocks):
    possible_lines = row_variations(line, blocks)
    if possible_lines:
        updated_line = intersection_row(possible_lines)
        return updated_line
    return []


def find_different_cells(new_line, old_line):
    changed_cells = set()
    for index in range(len(new_line)):
        if new_line[index] != old_line[index]:
            changed_cells.add(index)
    return changed_cells


def solve_easy_nonogram(constraints: List[List[List[int]]]) ->\
                                                Optional[List[List[int]]]:
    """

    :param constraints:
    :return:
    """
    row_num = len(constraints[ROW_INDEX])
    col_num = len(constraints[COL_INDEX])
    board = []

    #  Generate raw board from row constraints:
    for block in constraints[ROW_INDEX]:
        possible_rows = constraint_satisfactions(col_num, block)
        # if there aren't any possibilities from the constraints:
        if not possible_rows:
            return
        board.append(intersection_row(possible_rows))


    # switch rows with cols:
    board = transpose(board)
    lines_to_check = set(range(col_num))

    is_cols = True
    while True:
        new_lines_to_check = set()
        for line_index in lines_to_check:
            new_line = update_line(board[line_index], constraints[is_cols][line_index])
            # if there is a contradiction with the constraints,
            # no new line will be created:
            if not new_line:
                return
            # find the indexes of the changed_cells:
            changed_cells = find_different_cells(new_line, board[line_index])
            # if changes were made, update the board and
            # the lines to check in the next iteration:
            if changed_cells:
                new_lines_to_check = new_lines_to_check.union(changed_cells)
                board[line_index] = new_line
        lines_to_check = new_lines_to_check
        # if no changes were made, we are done!
        if not lines_to_check:
            break
        # flip the board:
        board = transpose(board)
        is_cols = not is_cols

    if is_cols:
        board = transpose(board)
    return board

def solve_nonogram(constraints):
    board = solve_easy_nonogram(constraints)
    all_sol = []
    if board:
        _helper_solve_nonogram(board, constraints, [], 0 , all_sol)
    return all_sol

def _helper_solve_nonogram(board, constraints, curr_sol, row_index, all_sol):
    if curr_sol and not check_constraints(curr_sol, constraints[COL_INDEX]):
        return
    # base case:
    if len(curr_sol) == len(board):
        all_sol.append(curr_sol)
        return

    # recursive step:
    for row_variation in row_variations(board[row_index],constraints[ROW_INDEX][row_index]):
        _helper_solve_nonogram(board, constraints, curr_sol + [row_variation], row_index + 1, all_sol)

    return all_sol


def split_col_to_blocks(col):
    blocks = [0]
    block_index = 0
    for cell in col:
        blocks[block_index] += cell
        if cell == 0 and blocks[block_index]:
            blocks.append(0)
            block_index += 1
    return blocks if blocks[-1] != 0 else blocks[:-1]


def blocks_match(curr_block, col_block, compare_last_block = True):
    if len(curr_block) > len(col_block):
        return False
    last_block_to_check = len(curr_block)-1
    for block_index in range(last_block_to_check):
        if curr_block[block_index] != col_block[block_index]:
            return False
    if compare_last_block and curr_block[-1] != col_block[last_block_to_check]:
        return False
    elif not compare_last_block and curr_block[-1] > col_block[last_block_to_check]:
        return False

    return True

def check_constraints(curr_sol, col_constraints):
    transposed_sol = transpose(curr_sol)
    for col_index, col in enumerate(transposed_sol):
        blocks = split_col_to_blocks(col)
        if blocks and not blocks_match(blocks, col_constraints[col_index], col[-1] != 1):
            return False
    return True


const = [[[1], [1], [1], [1], [1]], [[1], [1], [1], [1], [1]]]

print(solve_nonogram(const))

