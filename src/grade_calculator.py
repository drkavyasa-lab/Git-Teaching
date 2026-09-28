"""Simple functions for calculating student grades."""


def calculate_average(marks):
    """Return the arithmetic mean of a list of marks."""
    if not marks:
        raise ValueError("Marks list cannot be empty")
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100")
    return sum(marks) / len(marks)


def calculate_grade(average):
    """Convert an average mark into a letter grade."""
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100")

    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def calculate_result(marks):
    """Return a dictionary containing average, grade and pass/fail status."""
    average = calculate_average(marks)
    grade = calculate_grade(average)
    return {
        "average": round(average, 2),
        "grade": grade,
        "passed": average >= 40,
    }
