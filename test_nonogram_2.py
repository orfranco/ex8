from nonogram import *


def test_constraint_satisfactions():
    assert sorted(constraint_satisfactions(3, [1])) == sorted(
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert sorted(constraint_satisfactions(3, [2])) == sorted(
        [[1, 1, 0], [0, 1, 1]])
    assert sorted(constraint_satisfactions(3, [1, 1])) == sorted([[1, 0, 1]])
    assert sorted(constraint_satisfactions(4, [1, 1])) == sorted(
        [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1]])
    assert sorted(constraint_satisfactions(5, [2, 1])) == sorted(
        [[1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 0, 1]])
    assert sorted(constraint_satisfactions(5, [2, 2])) == sorted(
        [[1, 1, 0, 1, 1]])
    assert sorted(constraint_satisfactions(0, [2, 1])) == []
    assert sorted(constraint_satisfactions(0, [])) == []
    assert sorted(constraint_satisfactions(5, [])) == [[0,0,0,0,0]]
    assert sorted(constraint_satisfactions(5, [5])) == [[1,1,1,1,1]]
    assert sorted(constraint_satisfactions(5, [6])) == []


def test_row_variations():

    assert sorted(row_variations([-1, -1, -1, 0], [2])) == sorted(
        [[1, 1, 0, 0], [0, 1, 1, 0]])
    assert sorted(row_variations([-1, -1, -1], [])) == [[0,0,0]]
    assert sorted(row_variations([-1, -1, -1, 0], [5])) == []
    assert sorted(row_variations([-1, -1, -1, -1], [3])) == sorted(
        [[1, 1, 1, 0], [0, 1, 1, 1]])
    assert sorted(row_variations([-1, -1, -1, -1], [1, 1])) == sorted(
        [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1]])
    assert sorted(row_variations([-1, -1, -1, -1], [1, 2])) == sorted(
        [[1, 0, 1, 1]])
    assert sorted(row_variations([1, 1, -1, 0], [3])) == sorted([[1, 1, 1, 0]])
    assert sorted(row_variations([-1, -1, -1], [1])) == sorted(
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert sorted(row_variations([0, 0, 0], [1])) == []
    assert sorted(row_variations([0, 0, -1, 1, 0], [3])) == []
    assert sorted(row_variations([0, 0, -1, 1, 0], [2])) == [[0, 0, 1, 1, 0]]
    assert sorted(row_variations([0, 0, 1, 1, 0], [2])) == [[0, 0, 1, 1, 0]]
    assert sorted(row_variations([-1, 0, 1, 0, -1, 0], [1, 1])) == sorted(
        [[0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0]])
    assert sorted(row_variations([], [1, 1])) == []

    assert sorted(
        row_variations([-1, 0, 1, 0, -1, -1, -1, -1, -1], [1, 3])) == sorted([[0, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 1, 0],[0, 0, 1, 0, 0, 0, 1, 1, 1]])
    assert sorted(
        row_variations(
            [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 1, 1, 1], [1, 7, 4])) == [
               [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 1, 1, 1]]
    assert sorted(
        row_variations(
            [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 1, 1, 1], [1, 7, 5])) == []
    assert sorted(
        row_variations(
            [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 1, 1, 1], [1, 7])) == []


def test_intersection_row():
    assert intersection_row([[0, 0, 1], [0, 1, 1], [0, 0, 1]]) == [0, -1, 1]
    assert intersection_row([[0, 1, -1], [-1, -1, -1]]) == [-1, -1, -1]
    assert intersection_row([[0], [-1]]) == [-1]
    assert intersection_row([[0], [1]]) == [-1]
    assert intersection_row([[1], [1]]) == [1]
    assert intersection_row(
        [[0, 1, -1, 0, 1], [1, 0, 1, 1, 0], [-1, -1, 0, -1, -1]]) == [-1, -1,
                                                                      -1, -1,
                                                                      -1]
    assert intersection_row([[], []]) == []
    assert intersection_row([[]]) == []


def test_solve_easy_nonogram():
    assert solve_easy_nonogram([[[2,2],[2],[1],[3],[3]],[[2],[2],[2],[1,2],[1,3]]]) == [[1, 1, 0, 1, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]
    assert solve_easy_nonogram([[[2,1],[1,3],[1,2],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[2]]]) == [[1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0]]
    assert solve_easy_nonogram([[[2], [1], [2], [4], [4]], [[2], [3], [3], [2, 2], [1]]]) == [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]
    assert solve_easy_nonogram([[[2,1],[1,3],[1,2],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[1,2,3]]]) == None
    assert solve_easy_nonogram([[[2,1],[1,3],[1,2],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[-1]]]) == None
    assert solve_easy_nonogram([[[2,1],[1,3],[1,2],[3],[],[1]],[[1],[5],[2],[5],[2,1],[2]]]) == None
    assert solve_easy_nonogram([[[2],[2],[2]],[[],[1],[]]]) == None
    assert solve_easy_nonogram([[[2],[2],[2]],[[1],[3],[]]]) == None
    assert solve_easy_nonogram([[[1],[1]],[[1],[1]]]) == [[-1,-1],[-1,-1]]
    assert solve_easy_nonogram([[[4],[4]],[[2],[2],[2],[2]]]) == [[1, 1, 1, 1], [1, 1, 1, 1]]
    assert solve_easy_nonogram([[[4],[]],[[1],[1],[1],[1]]]) == [[1,1,1,1],[0,0,0,0]]
    #TODO: empty list?

def test_split_col_to_blocks():
    assert split_line_to_blocks([1, 1, 1, 0, 0, 0, 1]) == [3, 1]
    assert split_line_to_blocks([1, 1, 1]) == [3]
    assert split_line_to_blocks([0, 0, 0]) == []
    assert split_line_to_blocks([]) == []
    assert split_line_to_blocks([1]) == [1]
    assert split_line_to_blocks([0]) == []
    assert split_line_to_blocks([1, 1, 0]) == [2]
    assert split_line_to_blocks([1, 1, 0, 0]) == [2]

def test_blocks_match():
    assert blocks_match([1,2],[1,2], compare_last_block=False) == True
    assert blocks_match([1,2],[1,2]) == True
    assert blocks_match([1,2],[1,3], compare_last_block=False) == True
    assert blocks_match([1,2],[1,3,3,3,3], compare_last_block=False) == True
    assert blocks_match([1,2],[1,3]) == False
    assert blocks_match([1,2],[1,3,3,3,3]) == False
    assert blocks_match([1,3],[1,2], compare_last_block=False) == False
    assert blocks_match([3,7],[1,2], compare_last_block=False) == False
    assert blocks_match([3,7],[1,2]) == False

def test_check_constraints():
    assert check_constraints([[1,1],[0,1],[1,1],[0,1],[1,1]],[[1,1,2],[5]]) == True
    assert check_constraints([[1,1,1,1],[0,0,0,0],[1,0,1,0]], [[1,1],[1],[1,7],[1]]) == True
    assert check_constraints([[1,1,1,1],[0,0,0,0],[1,0,1,0]], [[1,1],[2],[1,7],[1]]) == False
    assert check_constraints([[1,1,1,1],[0,0,0,0],[1,0,1,0]], [[1,1],[2],[1,7],[1]]) == False
    assert check_constraints([[1,0,1,0]],[[2],[1],[1],[]]) == True
    assert check_constraints([[1,1,1,0]],[[1],[1],[1],[1]]) == True

def test_solve_nonogram():
    assert solve_nonogram([[[2,2],[2],[1],[3],[3]],[[2],[2],[2],[1,2],[1,3]]]) == [[[1, 1, 0, 1, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]]
    assert solve_nonogram([[[2,1],[1,3],[1,2],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[2]]]) == [[[1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0]]]
    assert solve_nonogram([[[2], [1], [2], [4], [4]], [[2], [3], [3], [2, 2], [1]]]) == [[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0]]]
    assert solve_nonogram([[[2,1],[1,3],[1,2],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[1,2,3]]]) == []
    assert solve_nonogram([[[2,1],[1,3],[1,2],[3],[4],[1]],[[1],[5],[2],[5],[2,1],[-1]]]) == []
    assert solve_nonogram([[[2,1],[1,3],[1,2],[3],[],[1]],[[1],[5],[2],[5],[2,1],[2]]]) == []
    assert solve_nonogram([[[2],[2],[2]],[[],[1],[]]]) == []
    assert solve_nonogram([[[2],[2],[2]],[[1],[3],[]]]) == []
    assert solve_nonogram([[[4],[4]],[[2],[2],[2],[2]]]) == [[[1, 1, 1, 1], [1, 1, 1, 1]]]
    assert solve_nonogram([[[4],[]],[[1],[1],[1],[1]]]) == [[[1,1,1,1],[0,0,0,0]]]
    assert sorted(solve_nonogram([[[1],[1]],[[1],[1]]])) == sorted([[[1, 0], [0, 1]], [[0, 1], [1, 0]]])
