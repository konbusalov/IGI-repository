from series_func import cos_series_func
from math import cos, pi

def task1():
    x = float(input("Enter x [-3.14..3.14]:"))
    if not -3.14 <= x <= 3.14:
        print("x must be between -3.14 and 3.14!")
        return None
    
    eps = float(input("Enter epsilon(<1): "))
    if eps >= 1:
        print("eps must be less than 1!")
        return None
    
    cos_func_result, n = cos_series_func(x, eps)
    cos_math_func_result = cos(pi)

    print('-'*100)
    print(f"My function result: {cos_func_result}; Argument(x):{x}; Epsilon(eps):{eps}; Amount of elements(n):{n}")
    print(f"Math function result: {cos_math_func_result}")
    print('-'*100)
