"""Test file for functions is square.py"""
from squares import is_valid_square


def test_is_valid_square_true_input_1():
    # Arrange
    data = [4, 4, 4, 4]
    # Act
    result = is_valid_square(data)
    # Assert
    assert result == True
    # assert is_valid_square([4, 4, 4, 4]) == True


def test_is_valid_square_false_input_1():
    assert is_valid_square([1, 2, 3, 4]) == False


def test_is_valid_square_false_input_2():
    assert is_valid_square([1, 2]) == False


def test_is_valid_square_false_input_3():
    assert is_valid_square() == False


def test_is_valid_square_false_input_4():
    assert is_valid_square(["4", "4", "4", "4"]) == True
