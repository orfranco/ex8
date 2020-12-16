##############################################################################
# FILE: nonogram.py
# EXERCISE: intro2cs1 ex8 2020
# DESCRIPTION: A program that solves nonogram puzzles
##############################################################################

# About intersection_row():
#   If on a specific index on of the given rows to intersect has -1, we chose
#   to fill the corresponding cell in the intersection with -1 as well.
#   This choice makes more sense in our opinion and it makes it easier to use
#   the output of this function in different parts of the code.


from typing import List, Optional, Set, Tuple

# Constants:
ROW_INDEX = 0
COL_INDEX = 1
COLORED_CELL = 1
EMPTY_CELL = 0
UNFILLED_CELL = -1


def constraint_satisfactions(n: int, blocks: List[int]) -> List[List[int]]:
    """
    This function returns a list of rows with length n,
                            that meets all of the given line_constraints.
    :param n: the length of the row - positive int.
    :param blocks: the line_constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of a row with the given line_constraints,
                doesn't matter the order.
    """
    all_opt: List[List[int]] = []

    if n > 0:
        _helper_constraint_satisfaction(n, blocks, 0, [], all_opt)

    return all_opt


def row_variations(row: List[int], blocks: List[int]) -> List[List[int]]:
    """
    this function gets a row that is partially filled, and finds all the ways
    to fill it according to the given line_constraints,
    by using a helper function: '_helper_row_variations'.
    :param row: a list of 1,0,-1 representing the state of the row.
    1 - filled cell.
    0 - empty cell.
    -1 - undefined cell.
    :param blocks: the line_constraints on a row. every number in the list is a
                    sequence of cells to be filled.
    :return: all filling options of the undefined cells in the given row
                    with the given line_constraints.
    """
    all_variations: List[List[int]] = []

    if len(row) > 0:
        _helper_row_variations(row, blocks, [], all_variations, 0)
    elif len(row) == 0:
        if len(blocks):
            return []
        return [[]]
    return all_variations


def intersection_row(rows: List[List[int]]) -> List[int]:
    """
    This function compares the given rows (list of ints) index by index,
    and creates a new row that slices all of them.
    In index i the sliced row will be:
    0 - if all rows was 0 in index i.
    1 - if all rows was 1 in index i.
    -1 - if the value in index i wasn't the same in all rows.
    :param rows: A List of rows containing 0,1,-1.
    :return: A list representing a row which slices all of the input rows.
    """
    intersected_row: List[int] = len(rows[0]) * [UNFILLED_CELL]

    for cell in range(len(rows[0])):
        curr_cell_value: int = rows[0][cell]

        for row in range(len(rows) - 1):
            # found rows with different values in the same column:
            if rows[row][cell] != rows[row + 1][cell]:
                curr_cell_value = UNFILLED_CELL

        intersected_row[cell] = curr_cell_value

    return intersected_row


def solve_easy_nonogram(constraints: List[List[List[int]]]) -> \
        Optional[List[List[int]]]:
    """
    This function uses a human-like method to solve the given nonogram puzzle,
    as best as possible:
    Intersects all possibilities to fill each row according to the constrains,
    intersects all possibilities to fill each columns,
    and repeats this process until:
    1. The board is solved, or
    2. All options were exhausted (The board isn't solved completely).
    3. A contradiction was reached (The board can't be solved under the given
    line_constraints).
    :param constraints:
    :return:
    """
    # row_num = len(line_constraints[ROW_INDEX])
    num_of_columns: int = len(constraints[COL_INDEX])
    board: List[List[int]] = []

    #  Generate raw board from row line_constraints:
    for block in constraints[ROW_INDEX]:
        possible_rows = constraint_satisfactions(num_of_columns, block)
        # if there aren't any possibilities from the line_constraints:
        if not possible_rows:
            return None
        board.append(intersection_row(possible_rows))

    # switch rows with columns:
    board = transpose(board)
    lines_to_check: Set[int] = set(range(num_of_columns))

    is_cols: bool = True
    while True:
        new_lines_to_check: Set[int] = set()
        for line_index in lines_to_check:
            new_line = update_line(board[line_index],
                                   constraints[is_cols][line_index])
            # if there is a contradiction with the line_constraints,
            # no new line will be created:
            if not new_line:
                return None
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


def solve_nonogram(constraints: List[List[List[int]]]) \
        -> List[List[List[int]]]:
    """
    This function finds all possible solutions to the given nonogram puzzle,
    by using the helper function - '_helper_solve_nonogram()'.
    :param constraints: A list with the constrains on the rows of the nonogram
                        and constrains on the columns of the nonogram.
    :return: All possible solutions.
    """
    #  Start by filling as many cells as possible using the 'easy' method:
    board: Optional[List[List[int]]] = solve_easy_nonogram(constraints)
    all_solutions: List[List[List[int]]] = []

    #  If the board is solvable, continue solving using backtracking:
    if board:
        _helper_solve_nonogram(board, constraints, [], 0, all_solutions)

    return all_solutions


# ########### Main Functions Helpers - backtracking functions ###########
def _helper_constraint_satisfaction(n: int, blocks: List[int],
                                    curr_block: int, curr_row: List[int],
                                    all_options: List[List[int]]) \
        -> Optional[List[List[int]]]:
    """
    This is a recursive function that finds all the options to
    meet the line_constraints given in a row with length n.
    :param n: the length of the row.
    :param blocks: the line_constraints.
    :param curr_block: index in blocks needed to be inserted to curr_row.
    :param curr_row: the specific row being formed.
    :param all_options: a list that will be filled by all the correct options.
    :return: all filling options of a row with the given line_constraints,
            doesn't matter the order.
    """
    # base cases: all cells are filled:
    if len(curr_row) == n:
        all_options.append(curr_row)
        return None

    # check the minimum number of cells needed to match the line_constraints:
    space_needed = check_space(curr_block, blocks)
    space_to_fill = n - len(curr_row)  # the number of cells left to fill.

    # if all the required blocks were filled, fill the rest of the cells with 0
    if curr_block >= len(blocks):
        curr_row = curr_row + [0] * space_to_fill
        all_options.append(curr_row)
        return None

    # loop through all optional cells that from them
    # we can start filling all remaining blocks and still match the row length.
    for i in range(space_to_fill - space_needed + 1):
        addition = [0] * i + blocks[curr_block] * [1]
        # add 0 after the block only if its not the end of the row:
        if len(curr_row + addition) < n:
            addition += [0]
        # recursive step:
        _helper_constraint_satisfaction(n, blocks, curr_block + 1,
                                        curr_row + addition, all_options)

    return all_options


def _helper_row_variations(row: List[int], blocks: List[int],
                           curr_row: List[int],
                           all_opt: List[List[int]],
                           curr_index: int) -> Optional[List[List[int]]]:
    """
    This function uses recursion in order to help 'row_variations()'
    accomplish its task.
    :param row: a list of 1,0,-1 representing the state of the row.
    :param blocks: all line_constraints of the row needed to be formed.
    :param blocks: all line_constraints on the row needed to be met.
    :param curr_row: the current row being formed.
    :param all_opt: a list that will be filled by all the correct options.
    :param curr_index: the current index in row being inserted to curr_row.
    :return: all filling options of the undefined cells in the given row
                    with the given line_constraints.
    """

    is_blocks_matching, filled_blocks = \
        check_constraint_for_line(curr_row, blocks)
    # validates the last fill:
    if not is_blocks_matching:
        return None
    # if all the blocks were filled:
    if filled_blocks == blocks:
        # if an extra 1 was found, the solution is invalid.
        if is_1_in_row(row, curr_index):
            return None
        # fill the rest of the row with 0's
        else:
            curr_row += [0] * (len(row) - len(curr_row))
        # Base case:
        if len(curr_row) == len(row):
            all_opt.append(curr_row)
            return None
    # if curr_row is at full length but the
    # blocks aren't filled, solution is invalid.
    if curr_index >= len(row):
        return None

    # recursive steps:
    if row[curr_index] == UNFILLED_CELL:
        _helper_row_variations(row, blocks,
                               curr_row + [COLORED_CELL],
                               all_opt, curr_index + 1)
        _helper_row_variations(row, blocks,
                               curr_row + [EMPTY_CELL],
                               all_opt, curr_index + 1)
    elif row[curr_index] == COLORED_CELL:
        _helper_row_variations(row, blocks,
                               curr_row + [COLORED_CELL],
                               all_opt, curr_index + 1)
    else:  # if EMPTY_CELL
        _helper_row_variations(row, blocks,
                               curr_row + [EMPTY_CELL],
                               all_opt, curr_index + 1)

    return all_opt


def _helper_solve_nonogram(board: List[List[int]],
                           constraints: List[List[List[int]]],
                           curr_sol: List[List[int]],
                           row_index: int,
                           all_sol: List[List[List[int]]]) -> \
        Optional[List[List[List[int]]]]:
    """
    This function uses recursion to help 'solve_nonogram()' accomplish its task
    :param board: A partially solved nonogram board (list of rows).
    :param constraints: The constraints on the rows and columns of the board.
    :param curr_sol: The current solution, which is built recursively.
    :param row_index: The index of the row that will be added to the solution.
    :param all_sol: A list of valid solutions that were found.
    :return: A list of all possible solutions of the nonogram puzzle.
    """
    #  If the line_constraints were violated, the solution isn't valid. Quit:
    if curr_sol and not check_constraints(curr_sol, constraints[COL_INDEX]):
        return None

    # base case:
    if len(curr_sol) == len(board):
        all_sol.append(curr_sol)
        return None

    # Recursive step - try every row variation in order to find a solution:
    for row_variation in row_variations(board[row_index],
                                        constraints[ROW_INDEX][row_index]):
        _helper_solve_nonogram(board, constraints, curr_sol + [row_variation],
                               row_index + 1, all_sol)

    return all_sol


# ########### More Helper Functions ###########
def check_space(curr_block: int, blocks: List[int]) -> int:
    """
    This functions calculates the minimum number of cells
                                    needed to match the line_constraints left.
    :param curr_block: Index in blocks representing the block
                        after the last block that was inserted to the row.
    :param blocks: All the line_constraints given.
    :return: The minimum number of cells needed to match the constraints left.
    """
    # not with sum() because its more efficient.
    summ = 0
    left_blocks_counter = 0

    for i in range(curr_block, len(blocks)):
        summ += blocks[i]
        left_blocks_counter += 1

    return summ + left_blocks_counter - 1


def is_1_in_row(row: List[int], curr_index: int) -> bool:
    """
      this function returns true if the row contains 1 in the section between
      curr_index till the end of the row.
      this function returns true if the given row contains 1 at indexes bigger
      than the given index (curr_index).
      :param row: a list of 1,0,-1 representing the state of the row.
      :param curr_index: the current index being filled in curr_row, from row.
      :return: True if the row contains 1 in the section between curr_index
      till the end of the row.
      """
    for i in range(curr_index, len(row)):
        if row[i] == 1:
            return True
    return False


def transpose(board: List[List[int]]) -> List[List[int]]:
    """
    This function transposes the given board (a 2 dimensional list)
    by switching the rows with the columns or vise versa.
    :param board: A list of lists of ints (2 dimensional list)
    :return: A transposed board.
    """
    return [[board[j][i] for j in range(len(board))]
            for i in range(len(board[0]))]


def update_line(line: List[int], blocks: List[int]) -> List[int]:
    """
    This function uses 'row_variations()' to find all possible ways to fill
    the given line (row or column) with the given blocks,
    and then uses 'intersection_row()' to find the intersection of all filling
    possibilities - meaning fills every cell of the given line with 1 or with 0
    if there is one way only to fill it.
    :param line: A row or a column (list of ints).
    :param blocks: The constraints on the line. Every number in the list is a
                    sequence of cells to be filled.
    :return: An updated version of the given line - if it was possible to fill
    some of it's cells,
    or an empty list if there is no possible way to fill cells in the line
    with the given blocks.
    """
    possible_lines: List[List[int]] = row_variations(line, blocks)

    if possible_lines:
        updated_line = intersection_row(possible_lines)
        return updated_line

    return []


def find_different_cells(new_line: List[int], old_line: List[int]) -> Set[int]:
    """
    This function compares the to given lines (rows or columns) index be index,
    and finds the indexes of cells that are different between the two lines.
    :param new_line: A row or column (list of ints) that was updated.
    :param old_line: A row or column (list of ints) before the update.
    :return: The indexes of the changed cells.
    """
    changed_cells: Set[int] = set()

    for index in range(len(new_line)):
        if new_line[index] != old_line[index]:
            changed_cells.add(index)

    return changed_cells


def split_line_to_blocks(line: List[int]) -> List[int]:
    """
    this function finds all the 1's blocks in a given row.
    :param line: a row or a col in the board.
    :return: returns a list containing ints representing
                            blocks of 1's in the given line.
    """
    blocks: List[int] = [0]
    block_index: int = 0

    for cell in line:
        blocks[block_index] += cell
        if cell == 0 and blocks[block_index]:
            blocks.append(0)
            block_index += 1

    return blocks if blocks[-1] != 0 else blocks[:-1]


def blocks_match(curr_blocks: List[int],
                 col_blocks: List[int],
                 compare_last_block: bool = True) -> bool:
    """
    This function checks if the blocks that in the current column being formed,
    fulfilling the line_constraints of the specific column.
    :param curr_blocks: the blocks of 1's that was
                        inserted to the current column.
    :param col_blocks: the line_constraints of the specific column
    :param compare_last_block: False if the last cell is 1.
    :return: True if the blocks match.
    """
    if len(curr_blocks) > len(col_blocks):
        return False

    last_block_to_check: int = len(curr_blocks) - 1

    for block_index in range(last_block_to_check):
        if curr_blocks[block_index] != col_blocks[block_index]:
            return False

    if compare_last_block and curr_blocks[-1] !=\
            col_blocks[last_block_to_check]:
        return False

    elif not compare_last_block and curr_blocks[-1] > \
            col_blocks[last_block_to_check]:
        return False

    return True


def check_constraints(curr_solution: List[List[int]],
                      column_constraints: List[List[int]]) -> bool:
    """
    This function checks if a given partial solution of the nonogram (given as
    rows) meets the column line_constraints
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


def check_constraint_for_line(curr_line: List[int],
                              line_constraints: List[int]) \
                                    -> Tuple[bool, List[int]]:
    """
    This function checks if a given partially filled line of the nonogram
    meets the line_constraints.
    :param curr_line: a row or a col in the board.
    :param line_constraints: the constraints on the specific line.
    :return: the blocks of 1's that appear in the given line, and a boolean
                value representing if the current line is valid or not.
    """
    blocks: List[int] = split_line_to_blocks(curr_line)

    if blocks and not blocks_match(blocks, line_constraints,
                                   curr_line[-1] != 1):
        return False, blocks

    return True, blocks


def print_sol(boards: List[List[List[int]]]) -> None:
    """
    This function prints the solutions that were created by 'solve_nonogram()'.
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
