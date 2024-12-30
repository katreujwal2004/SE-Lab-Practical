
class StudentGrades:   
    def __init__(self):
        self.grades = {}

    def add_grade(self, student_name, grade):
        """Adds a grade for a specific student."""
        if student_name not in self.grades:
            self.grades[student_name] = []
        self.grades[student_name].append(grade)

    def get_grades(self, student_name):
        """Returns the list of grades for a specific student."""
        return self.grades.get(student_name, [])

    def calculate_average(self, student_name):
        """Calculates the average grade for a specific student."""
        grades = self.grades.get(student_name, [])
        if not grades:
            return 0
        return sum(grades) / len(grades)

    def get_all_students(self):
        """Returns a list of all student names."""
        return list(self.grades.keys())
