from list_operations import enter_elements, pos_list_elements_count, product_after_max_el

def task5():
    my_list = []
    enter_elements(my_list)
    
    c = float(input("Enter c: "))
    pos_elements_count = pos_list_elements_count(my_list, c)
    product = product_after_max_el(my_list)

    print('-'*100)
    print(f"Positive elements greater than C: {pos_elements_count}")
    print(f"Product of elements after max element: {product}")
    print('-'*100)

    