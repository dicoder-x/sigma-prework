from triangle import *


def test_triangle_valid_input_true_1():
    assert is_valid_triangle([60, 60, 60]) == True


def test_triangle_valid_input_false_1():
    assert is_valid_triangle([20, 30, 10]) == False


def test_equal_valid_input_true_1():
    assert is_valid_equilateral_triangle([60, 60, 60]) == True


def test_equal_valid_input_false_1():
    assert is_valid_equilateral_triangle([30, 90, 60]) == False


def test_triangle_type_input_true_1():
    assert get_triangle_type([60, 60, 60]) == "equilateral"


def test_triangle_type_input_true_2():
    assert get_triangle_type([60, 30, 90]) == "right angle"


def test_triangle_type_input_true_3():
    assert get_triangle_type([30, 30, 120]) == "isoceles"


def test_triangle_type_input_true_4():
    assert get_triangle_type([40, 30, 110]) == "scalene"


def test_triangle_type_input_false_1():
    assert get_triangle_type([20, 30, 10]) == "not triangle"
