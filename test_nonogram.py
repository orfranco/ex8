from nonogram import *


def test_constraint_satisfactions():
    assert sorted(constraint_satisfactions(3, [1])) == sorted([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert sorted(constraint_satisfactions(3, [2])) == sorted([[1, 1, 0], [0, 1, 1]])
    assert sorted(constraint_satisfactions(3, [1, 1])) == sorted([[1, 0, 1]])
    assert sorted(constraint_satisfactions(4, [1, 1])) == sorted([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1]])
    assert sorted(constraint_satisfactions(5, [2, 1])) == sorted([[1, 1, 0, 1, 0] , [1, 1, 0, 0, 1], [0, 1, 1, 0, 1]])
