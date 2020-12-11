from nonogram import *
from copy import deepcopy

INTERSECTION_ROWS = (
    # empty row
    ([[]], []),
    # empty rows
    ([[], []], []),
    # one row
    ([[1, 0, -1, 0, 1]], [1, 0, -1, 0, 1]),
    # row with unknown
    ([
         [1, 0, -1],
         [-1, 0, 1]
     ], [-1, 0, -1]
    ),
    # row with other values
    ([
         [-1, 0, 1, 1],
         [1, 1, 1, 1]
     ], [-1, -1, 1, 1]
    ),
    # many rows
    ([
         [1, 1, 1, 0, 0],
         [1, 1, 1, 0, 0],
         [1, 1, 1, 0, 0],
         [1, 1, 1, 0, 1],
         [1, -1, 1, 0, 0],
     ], [1, -1, 1, 0, -1]
    ),
    ([[0, 0, 1], [0, 1, 1], [0, 0, 1]], [0, -1, 1]),
    ([[0, 1, -1], [-1, -1, -1]], [-1, -1, -1])
)

ROW_VARIATIONS = (
    # empty row
    # (([], []), [[]]),
    # full row
    (([1, 1, 0], [2]), [[1, 1, 0]]),
    # all options
    (([-1, -1, -1], [1]), [[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1], ]),
    # all options 2
    (([-1, -1, -1], [2]), [[1, 1, 0],
                           [0, 1, 1]]),
    # simple one
    (([-1, -1, -1, -1, -1, -1, -1, -1], [2, 3, 1]),
     [[1, 1, 0, 1, 1, 1, 0, 1]]),
    # hard one
    (([-1, -1, -1, -1, -1, -1, -1, -1], [1, 2, 1]),
     [
         [1, 0, 1, 1, 0, 1, 0, 0],
         [1, 0, 1, 1, 0, 0, 1, 0],
         [1, 0, 1, 1, 0, 0, 0, 1],
         [1, 0, 0, 1, 1, 0, 1, 0],
         [1, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 0, 0, 1, 1, 0, 1],
         [0, 1, 0, 1, 1, 0, 1, 0],
         [0, 1, 0, 1, 1, 0, 0, 1],
         [0, 1, 0, 0, 1, 1, 0, 1],
         [0, 0, 1, 0, 1, 1, 0, 1],
     ]),
    (([1, 1, -1, 0], [3]), [[1, 1, 1, 0]]),
    (([-1, -1, -1, 0], [2]), [[0, 1, 1, 0], [1, 1, 0, 0]]),
    (
    ([-1, 0, 1, 0, -1, 0], [1, 1]), [[0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0]]),
    (([-1, -1, -1], [1]), [[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
    (([0, 0, 0], [1]), []),
    (([0, 0, -1, 1, 0], [3]), []),
    (([0, 0, -1, 1, 0], [2]), [[0, 0, 1, 1, 0]]),
    (([0, 0, 1, 1, 0], [2]), [[0, 0, 1, 1, 0]]),
)


def test_constraint_satisfactions():
    res1 = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
    constraints1 = [1]
    constraints1_copy = deepcopy(constraints1)
    assert sorted(constraint_satisfactions(3, constraints1)) == sorted(res1)
    assert constraints1 == constraints1_copy,"Do not change the input"
    res2 = [[0, 1, 1], [1, 1, 0]]
    constraints2 = [2]
    constraints2_copy = deepcopy(constraints2)
    assert sorted(constraint_satisfactions(3, constraints2)) == sorted(res2)
    assert constraints2 == constraints2_copy,"Do not change the input"
    res3 = [[1, 0, 1]]
    constraints3 = [1, 1]
    constraints3_copy = deepcopy(constraints3)
    assert sorted(constraint_satisfactions(3, constraints3)) == sorted(res3)
    assert constraints3 == constraints3_copy,"Do not change the input"
    res4 = [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1]]
    constraints4 = [1, 1]
    constraints4_copy = deepcopy(constraints4)
    assert sorted(constraint_satisfactions(4, constraints4)) == sorted(res4)
    assert constraints4 == constraints4_copy,"Do not change the input"
    res5 = [[1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 0, 1]]
    constraints5 = [2, 1]
    constraints5_copy = deepcopy(constraints5)
    assert sorted(constraint_satisfactions(5, constraints5)) == sorted(res5)
    assert constraints5 == constraints5_copy,"Do not change the input"
    res6 = [[0,0,0]]
    constraints6 = []
    constraints6_copy = deepcopy(constraints6)
    assert sorted(constraint_satisfactions(3, constraints6)) == sorted(res6)
    assert constraints6 == constraints6_copy,"Do not change the input"


def test_row_variations():
    for i in range(len(ROW_VARIATIONS)):
        row, blocks = ROW_VARIATIONS[i][0]
        row_copy = deepcopy(row)
        res = ROW_VARIATIONS[i][1]
        assert sorted(row_variations(row, blocks)) == sorted(
            res), f"Intersection_row failed on {i + 1} run"
        assert row == row_copy, "Do not change the input"


def test_intersection_row():
    for i in range(len(INTERSECTION_ROWS)):
        input = INTERSECTION_ROWS[i][0]
        input_copy = deepcopy(input)
        res = INTERSECTION_ROWS[i][1]
        assert intersection_row(
            input) == res, f"Intersection_row failed on {i + 1} run"
        assert input == input_copy, "Do not change the input"
