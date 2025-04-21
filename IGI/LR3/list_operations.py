def enter_elements(my_list: list):
    while True:
        val = input("Enter a value('end' to exit): ")
        if val.lower() == 'end':
            break
        try:
            num = float(val)
            my_list.append(num)
        except ValueError:
            print('Value must be a number')
            continue

def pos_list_elements_count(my_list: list, c: float):
    count = 0
    for el in my_list:
        if el > 0 and el > c:
            count += 1
    
    return count

def get_max_element(my_list: list):
    if not my_list:
        raise ValueError("List cannot be empty")

    max_index = 0
    greatest = my_list[0]
    for i, el in enumerate(my_list):
        if el > greatest:
            greatest = el
            max_index = i
    return max_index

def product_after_max_el(my_list: list):
    index = get_max_element(my_list)
    product = 1
    for el in my_list[index + 1:]:
        product *= el
    return product





    



    



