from services.serializer import SerializerFactory
from services.student_stats import StudentStats

GTO_NORMS_FILE_NAME_CSV = "gto_norms.csv"
STUDENTS_FILE_NAME_CSV = "students.csv"
GTO_NORMS_FILE_NAME_PICKLE = "gto_norms.txt"
STUDENTS_FILE_NAME_PICKLE = "students.txt"


def task1():
    gto_norms = {
        "100m": 15.0,
        "jumps": 2.5,
    }

    students = [
        {"name": "Ivan", "100m": 14.5, "jumps": 2.8},
        {"name": "Maria", "100m": 15.2, "jumps": 2.4},
        {"name": "Alex", "100m": 14.8, "jumps": 2.6},
        {"name": "Olga", "100m": 15.5, "jumps": 2.3},
        {"name": "Sergey", "100m": 13.9, "jumps": 3.0},
        {"name": "Anna", "100m": 16.0, "jumps": 2.2},
    ]

    new_student = {"name": input("Input name: "), "100m": float(input("Input 100m: ")), "jumps": float(input("Input jumps: "))}
    students.append(new_student)

    choice = input("Serialize with CSV(1); Serialize with Pickle(2): ")

    if choice == '1':
        #Serialization with CSV
        SerializerFactory.get_serializer(GTO_NORMS_FILE_NAME_CSV).serialize(GTO_NORMS_FILE_NAME_CSV, gto_norms)
        SerializerFactory.get_serializer(STUDENTS_FILE_NAME_CSV).serialize(STUDENTS_FILE_NAME_CSV, students)

        deserialized_gto_norms = SerializerFactory.get_serializer(GTO_NORMS_FILE_NAME_CSV).deserialize(GTO_NORMS_FILE_NAME_CSV)
        deserialized_students = SerializerFactory.get_serializer(STUDENTS_FILE_NAME_CSV).deserialize(STUDENTS_FILE_NAME_CSV)

        passed_students = StudentStats.get_passed_students(deserialized_gto_norms, deserialized_students)
        failed_students = StudentStats.get_failed_students(deserialized_gto_norms, deserialized_students)
        top_3 = StudentStats.get_top_3(deserialized_students)

        print('-' * 148)
        print(f"Passed students: {passed_students}")
        print()
        print(f"Failed students: {failed_students}")
        print()
        print(f"Top 3: {top_3}")
        print('-' * 148)
    elif choice == '2':
        #Serialization with Pickle
        SerializerFactory.get_serializer(GTO_NORMS_FILE_NAME_PICKLE).serialize(GTO_NORMS_FILE_NAME_PICKLE, gto_norms)
        SerializerFactory.get_serializer(STUDENTS_FILE_NAME_PICKLE).serialize(STUDENTS_FILE_NAME_PICKLE, students)

        deserialized_gto_norms = SerializerFactory.get_serializer(GTO_NORMS_FILE_NAME_PICKLE).deserialize(GTO_NORMS_FILE_NAME_PICKLE)
        deserialized_students = SerializerFactory.get_serializer(STUDENTS_FILE_NAME_PICKLE).deserialize(STUDENTS_FILE_NAME_PICKLE)

        passed_students = StudentStats.get_passed_students(deserialized_gto_norms, deserialized_students)
        failed_students = StudentStats.get_failed_students(deserialized_gto_norms, deserialized_students)
        top_3 = StudentStats.get_top_3(deserialized_students)

        print('-' * 148)
        print(f"Passed students: {passed_students}")
        print()
        print(f"Failed students: {failed_students}")
        print()
        print(f"Top 3: {top_3}")
        print('-' * 148)







