from generator import user_input_sequence
from decorator import decorator_it

@decorator_it
def seq_sum():
    num = 0
    result = 0
    count = 0
    my_list = [val for val in user_input_sequence()]
    for num in my_list:
        if num < 10:
            count += 1
        result += num
    
    return result, count
