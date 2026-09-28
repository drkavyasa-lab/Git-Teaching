import pytest

from src.grade_calculator import (
    calculate_average,
    calculate_grade,
    calculate_result,
)


def test_calculate_average():
    assert calculate_average([80, 90, 70]) == 80


def test_average_with_decimal_result():
    assert calculate_average([70, 80, 75]) == 75


def test_empty_marks_raise_error():
    with pytest.raises(ValueError):
        calculate_average([])


def test_invalid_marks_raise_error():
    with pytest.raises(ValueError):
        calculate_average([80, 105])


def test_grade_boundaries():
    assert calculate_grade(90) == "A"
    assert calculate_grade(80) == "B"
    assert calculate_grade(70) == "C"
    assert calculate_grade(60) == "D"
    assert calculate_grade(59.99) == "F"


def test_invalid_average_raise_error():
    with pytest.raises(ValueError):
        calculate_grade(101)


def test_passed_result():
    result = calculate_result([60, 70, 80])
    assert result["passed"] is True
    assert result["grade"] == "C"


def test_failed_result():
    result = calculate_result([20, 30, 35])
    assert result["passed"] is False
