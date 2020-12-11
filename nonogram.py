##############################################################################
# FILE: nonogram.py
# EXERCISE: intro2cs1 ex8 2020
# DESCRIPTION: A program that solves nonogram puzzles
##############################################################################
from typing import List, Optional, Set

# Constants:
ROW_INDEX = 0
COL_INDEX = 1
COLORED_CELL = 1
EMPTY_CELL = 0
UNFILLED_CELL = -1
BOARD_TO_PRINT = [
    [
        [1, 1, 1, 1, 2, 1, 1, 1, 1],
        [2], [1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 1, 1, 6, 1, 1, 1],
        [1, 1, 1, 2, 1, 1, 1],
        [1, 1, 10, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 14, 1],
        [1, 2, 1],
        [18],
        [2],
        [1, 2],
        [5, 2, 1],
        [3, 4, 5],
        [1, 6, 3],
        [8, 1]
    ],
    [
        [1, 8, 1],
        [1, 2],
        [1, 6, 1, 4],
        [1, 1, 2],
        [1, 4, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 2, 1, 1, 1, 2],
        [1, 1, 1, 1, 3],
        [16],
        [16],
        [1, 1, 1, 1, 3],
        [1, 2, 1, 1, 1, 2],
        [1, 1, 1, 1],
        [1, 4, 1, 1, 1],
        [1, 1, 2],
        [1, 6, 1, 4],
        [1, 2],
        [1, 8, 1]
    ]
]


def constraint_satisfactions(n: int, blocks: List[int]) -> List[List[int]]:
    """
    this function returns a list of rows with length n,
                            that satisfacts all the constraints given.
    :param n: the length of the row - positive int.
    :param blocks: the constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of a row with the given constraints. doesn't
            matter the order.
    """
    all_opt = []
    if n > 0:
        _helper_constraint_satisfaction(n, blocks, 0, [], all_opt)
    return all_opt


def check_space(curr_block: int, blocks: List[int]) -> int:
    """
    this functions calculates the minimum number of cells
                                    needed to match the constraints left.
    :param curr_block: index in blocks representing the block
                        after the last block that was inserted to the row.
    :param blocks: all the constraints given.
    :return: the minimum number of cells needed to match the constraints left.
    """
    # not with sum() because its more efficient.
    summ = 0
    left_blocks_counter = 0

    for i in range(curr_block, len(blocks)):
        summ += blocks[i]
        left_blocks_counter += 1

    return summ + left_blocks_counter - 1


def _helper_constraint_satisfaction(n: int, blocks: List[int],
                                    curr_block: int, curr_row: List[int],
                                    all_opt: List[List[int]])\
                                    -> Optional[List[List[int]]]:
    """
    this is a recursive function that finds all the options to
     satisfact the constraints given in a row with length n.
    :param n: the length of the row.
    :param blocks: the constraints.
    :param curr_block: index in blocks needed to be inserted to curr_row.
    :param curr_row: the specific row being formed.
    :param all_opt: a list that will be filled by all the correct options.
    :return: all filling options of a row with the given constraints. doesn't
            matter the order.
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
        addition = [0] * i + blocks[curr_block] * [1]
        # add 0 after the block only if its not the end of the row:
        if len(curr_row + addition) < n:
            addition += [0]
        # recursive step:
        _helper_constraint_satisfaction(n, blocks, curr_block + 1,
                                        curr_row + addition, all_opt)

    return all_opt


def row_variations(row: List[int], blocks: List[int]) -> List[List[int]]:
    """
    this function gets a row that is partially filled, and finds all the ways
    to fill it still matching the constraints.
    :param row: a list of 1,0,-1 representing the state of the row.
    1 - filled cell.
    0 - empty cell.
    -1 - undefined cell.
    :param blocks: the constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of the undefined cells in the given row
                    with the given constraints.
    """
    all_variations = []

    if len(row) >= 0:
        _helper_row_variations(row, blocks, 0, [], all_variations, 0)
    return all_variations


#TODO: think if we can do it better with check_constraints function.
def _helper_row_variations(row: List[int], blocks: List[int], curr_block: int,
                           curr_row: List[int], all_opt: List[List[int]],
                           curr_index: int) -> Optional[List[List[int]]]:
    """

    :param row: a list of 1,0,-1 representing the state of the row.
    :param blocks: all constraints of the row needed to be formed.
    :param curr_block: the index of the current block needed to be
                                                    inserted to curr_row.
    :param curr_row: the current row being formed.
    :param all_opt: a list that will be filled by all the correct options.
    :param curr_index: the current index in row being inserted to curr_row.
    :return: all filling options of the undefined cells in the given row
                    with the given constraints.
    """
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
        if len(curr_row) > 0 and sum_of_remaining_blocks(curr_block, blocks) >\
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
    this function gets a list with 1 on the last cell,
    and returns the index of the first 1 in the sequence.
    :param curr_row: a row that has 1 in the last cell.
    :return: the index of the first 1 in the sequence.
    """
    pivot_index = len(curr_row)
    for i in range(len(curr_row) - 1, -1, -1):
        if curr_row[i] == 0:
            break
        pivot_index -= 1

    return pivot_index


def sum_of_remaining_blocks(curr_block: int, blocks: List[int]) -> int:
    """
    this function calculates the sum of the values in remaining blocks.
    :param curr_block: the index of the current block.
    :param blocks: a list of all constraints.
    :return: the sum of the values from curr_block to last index in blocks.
    """
    summ = 0

    for i in range(curr_block, len(blocks)):
        summ += blocks[i]

    return summ


def count_row_editable_cells(curr_index: int, row: List[int]) -> int:
    """
    this function counts the number of cells that contains -1 or 1.
    :param curr_index: the current index being filled in curr_row, from row.
    :param row: a list of 1,0,-1 representing the state of the row.
    :return: the number of cells that contain -1 or 1.
    """
    counter = 0

    for i in range(curr_index, len(row)):
        if row[i] != 0:
            counter += 1

    return counter


def find_1_in_row(row: List[int], curr_index: int) -> bool:
    """
    this function returns true if the row contains 1 in the section between
    curr_index till the end of the row.
    :param row: a list of 1,0,-1 representing the state of the row.
    :param curr_index: the current index being filled in curr_row, from row.
    :return: True if the row contains 1 in the section between curr_index
    till the end of the row.
    """

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

        for row in range(len(rows) - 1):
            # found rows with different values in the same column:
            if rows[row][cell] != rows[row + 1][cell]:
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
    """

    :param new_line:
    :param old_line:
    :return:
    """
    changed_cells = set()
    for index in range(len(new_line)):
        if new_line[index] != old_line[index]:
            changed_cells.add(index)
    return changed_cells


def solve_easy_nonogram(constraints: List[List[List[int]]]) -> \
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

    # switch rows with columns:
    board = transpose(board)
    lines_to_check = set(range(col_num))

    is_cols = True
    while True:
        new_lines_to_check = set()
        for line_index in lines_to_check:
            new_line = update_line(board[line_index],
                                   constraints[is_cols][line_index])
            # if there is a contradiction with the constraints,
            # no new line will be created:
            if not new_line:
                return
            # Find the indexes of the changed_cells:
            changed_cells = find_different_cells(new_line, board[line_index])
            # if changes were made, update the board and
            # the lines-to-check in the next iteration:
            if changed_cells:
                new_lines_to_check = new_lines_to_check.union(changed_cells)
                board[line_index] = new_line
        lines_to_check = new_lines_to_check
        # If no changes were made, we are done!
        if not lines_to_check:
            break
        # Flip the board:
        board = transpose(board)
        is_cols = not is_cols

    # If we finished with a transposed board - switch back rows and columns:
    if is_cols:
        board = transpose(board)
    return board


def solve_nonogram(constraints: List[List[List[int]]]) -> List[List[List[int]]]:
    """

    :param constraints:
    :return:
    """
    board: List[List[int]] = solve_easy_nonogram(constraints)
    all_solutions: List = []

    if board:
        _helper_solve_nonogram(board, constraints, [], 0, all_solutions)

    return all_solutions


def _helper_solve_nonogram(board, constraints, curr_sol, row_index, all_sol):
    """

    :param board:
    :param constraints:
    :param curr_sol:
    :param row_index:
    :param all_sol:
    :return:
    """
    if curr_sol and not check_constraints(curr_sol, constraints[COL_INDEX]):
        return
    # base case:
    if len(curr_sol) == len(board):
        all_sol.append(curr_sol)
        return

    # recursive step:
    for row_variation in row_variations(board[row_index],
                                        constraints[ROW_INDEX][row_index]):
        _helper_solve_nonogram(board, constraints, curr_sol + [row_variation],
                               row_index + 1, all_sol)

    return all_sol


def split_line_to_blocks(line: List[int]) -> List[int]:
    """

    :param line:
    :return:
    """
    blocks: List[int] = [0]
    block_index: int = 0

    for cell in line:
        blocks[block_index] += cell
        if cell == 0 and blocks[block_index]:
            blocks.append(0)
            block_index += 1

    return blocks if blocks[-1] != 0 else blocks[:-1]


def blocks_match(curr_block, col_block, compare_last_block=True):
    """

    :param curr_block:
    :param col_block:
    :param compare_last_block:
    :return:
    """
    if len(curr_block) > len(col_block):
        return False

    last_block_to_check = len(curr_block) - 1

    for block_index in range(last_block_to_check):
        if curr_block[block_index] != col_block[block_index]:
            return False

    if compare_last_block and curr_block[-1] != col_block[last_block_to_check]:
        return False

    elif not compare_last_block and curr_block[-1] >\
            col_block[last_block_to_check]:
        return False

    return True


def check_constraints(curr_solution, column_constraints):
    """
    This function checks if a given partial solution of the nonogram (given as
    rows) meets the column constraints
    :param curr_solution:
    :param column_constraints:
    :return:
    """
    transposed_solution: List[List[int]] = transpose(curr_solution)

    for col_index, column in enumerate(transposed_solution):
        blocks = split_line_to_blocks(column)
        if blocks and not blocks_match(blocks,
                                       column_constraints[col_index],
                                       column[-1] != 1):
            return False

    return True


def print_sol(boards: List[List[List[int]]]) -> None:
    """
    This function prints the solutions that were created by 'solve_nonogram'.
    :param boards: List of solved boards. Every board is a list of list of ints
    :return: None.
    """
    print("\n" + "-" * 65 + "\n")
    for board in boards:
        for row in board:
            str1 = ""
            for cell in row:
                if cell == 1:
                    str1 += "#  "
                else:
                    str1 += "   "
            print(str1)
    print("\n" + "-" * 65 + "\n")
