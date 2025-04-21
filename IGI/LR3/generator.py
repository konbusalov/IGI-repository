def user_input_sequence():
    while True:
        num = int(input("Enter number (100 to stop): "))
        if num == 100:
            break
        yield num



