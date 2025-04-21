#IGI Lab 3 Python
#Busalov Konstantin 
#07.04.2025
#VARIANT 7

from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5

while True:
    print("Choose a task to test:")
    print("1. Task 1: Series calculation")
    print("2. Task 2: Numbers less then 10")
    print("3. Task 3: Count lowercase letters and numbers")
    print("4. Task 4: Text analysis")
    print("5. Task 5: List processing")
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
            task4()
        case '5':
            task5()
        case '0':
            print("Exiting the program...")
            break
        case _:
            print("Invalid choice. Please enter a number between 0 and 5")


            
        
            


