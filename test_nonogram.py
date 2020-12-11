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
    assert sorted(constraint_satisfactions(5, [])) == []


def test_row_variations():
    assert sorted(row_variations([-1, -1, -1, 0], [2])) == sorted(
        [[1, 1, 0, 0], [0, 1, 1, 0]])
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


def test_solve_easy_nonogram():
    assert solve_easy_nonogram([[[2,2],[2],[1],[3],[3]],[[2],[2],[2],[1,2],[1,3]]]) == [[1, 1, 0, 1, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]
    # TODO: This test resutls should be changed after the function is completed !:
    assert solve_easy_nonogram([[[2], [1], [2], [4], [4]], [[2], [3], [3], [2, 2], [1]]]) == [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 1, 0, 0], [-1, 1, 1, 1, -1], [-1, 1, 1, 1, -1]]
    #TODO: empty list?
