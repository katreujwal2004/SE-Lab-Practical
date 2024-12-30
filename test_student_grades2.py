"""
Unit tests for the StudentGrades class.
This module contains test cases to validate the functionality of adding grades,
retrieving grades, calculating averages, and handling empty or populated student lists.
"""

from SELab2.student_grades2 import StudentGrades

def test_add_grade():
    """Test adding grades for students."""
    sg = StudentGrades()
    sg.add_grade("Alice", 85)
    sg.add_grade("Alice", 90)
    sg.add_grade("Bob", 78)
    assert sg.get_grades("Alice") == [85, 90]
    assert sg.get_grades("Bob") == [78]

def test_get_grades():
    """Test retrieving grades for students."""
    sg = StudentGrades()
    sg.add_grade("Alice", 85)
    assert sg.get_grades("Alice") == [85]
    assert sg.get_grades("Bob") == []  # Bob has no grades yet

def test_calculate_average():
    """Test calculating the average grade for students."""
    sg = StudentGrades()
    sg.add_grade("Alice", 85)
    sg.add_grade("Alice", 95)
    sg.add_grade("Bob", 78)
    assert sg.calculate_average("Alice") == 90.0
    assert sg.calculate_average("Bob") == 78.0
    assert sg.calculate_average("Charlie") == 0  # Charlie has no grades

def test_get_all_students():
    """Test retrieving all student names."""
    sg = StudentGrades()
    sg.add_grade("Alice", 85)
    sg.add_grade("Bob", 78)
    sg.add_grade("Charlie", 92)
    assert set(sg.get_all_students()) == {"Alice", "Bob", "Charlie"}

def test_empty_class():
    """Test behavior when the class is empty."""
    sg = StudentGrades()
    assert not sg.get_all_students()  # Simplified boolean comparison
    assert sg.get_grades("Alice") == []
    assert sg.calculate_average("Alice") == 0
