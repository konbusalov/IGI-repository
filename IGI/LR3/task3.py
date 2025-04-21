from analyse_text import lowercase_count, num_count

def task3():
    text = input("Input text: ")
    lower_count, numbers_count = lowercase_count(text), num_count(text)

    print('-'*20)
    print(f"Lower case letters: {lower_count}")
    print(f"Numbers: {numbers_count}")
    print('-'*20)
    