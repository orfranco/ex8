import pytest
import nonogram
def test_check_exists_nonogram_file():
    try:
        f = open("nonogram.py")
    except FileNotFoundError:
        pytest.fail("No nonogram.py file")

def test_check_exists_authors_file():
    try:
        f = open("AUTHORS")
    except FileNotFoundError:
        pytest.fail("No wave_editor file")


def test_function_names():
    funcs = ["constraint_satisfactions", "row_variations", "intersection_row",
             "solve_easy_nonogram","solve_nonogram"]
    errors = []
    for func in funcs:
        if func not in dir(nonogram):
            errors.append(func)
    assert not errors, f"the following functions are missing or mispelled {','.join(errors)}"