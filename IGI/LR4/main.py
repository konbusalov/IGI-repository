#IGI Lab 4 Python
#Busalov Konstantin 
#07.04.2025
#VARIANT 7

from tasks.task1 import task1
from tasks.task2 import task2
from tasks.task3 import task3
from tasks.task4 import task4
from tasks.task5 import task5
from services.shapes import Hexagon
from math import isclose

while True:
    print("Choose a task to test:")
    print("1. Task 1: Serialization")
    print("2. Task 2: Text analysis with Regular Expressions")
    print("3. Task 3: Math graphs")
    print("4. Task 4: OOP")
    print("5. Task 5: Arrays and Matrices(NumPy)")
    print("0. Exit")

    choice = input("Enter your choice: ").strip()

    match choice:
        case '1':
            task1()
        case '2':
            task2()
        case '3':
            task3()
        case '4':
            def test_hexagon():
                hexagon = Hexagon(5, "Red")

                expected_area = (3 * (3**0.5)/2) * 5**2
                actual_area = hexagon.area()
                
                assert isclose(actual_area, expected_area, rel_tol=1e-9)

                print("All tests passed!")

            if __name__ == "__main__":
                test_hexagon()
            
            task4()
        case '5':
            task5()
        case '0':
            print("Exiting the program...")
            break
        case _:
            print("Invalid choice. Please enter a number between 0 and 5")