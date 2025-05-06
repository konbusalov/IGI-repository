from .serializer import Serializer

GTO_NORMS_FILE_NAME = "gto_norms.csv"
STUDENTS_FILE_NAME = "students.csv"
GTO_NORMS_PICKLE_FILE_NAME = "gto_norms.csv"
STUDENTS_PICKLE_FILE_NAME = "students.csv"


class StudentStats:
    @staticmethod
    def get_passed_students(gto_norms, students):
        passed_students = []

        for student in students:
            if student["100m"] <= gto_norms["100m"] and student["jumps"] >= gto_norms["jumps"]:
                passed_students.append(student)
        
        return passed_students
    
    @staticmethod
    def get_failed_students(gto_norms, students):
        failed_students = []

        for student in students:
            if student["100m"] > gto_norms["100m"] or student["jumps"] < gto_norms["jumps"]:
                failed_students.append(student)
        
        return failed_students
    
    @staticmethod
    def get_top_3(students):
        sorted_students = sorted(students, key=lambda x: (float(x["100m"]), float(x["jumps"])))
        return sorted_students[:3]