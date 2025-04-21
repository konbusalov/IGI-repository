from math import pi, factorial

def cos_series_func(x, eps):
    if not -pi <= x <= pi:
        raise ValueError("x must be between -π and π (inclusive).")
    if eps >= 1:
        raise ValueError("eps must be less than 1.")

    n = 0
    result = 0
    current_el = ((-1)**n )*((x**(2*n))/factorial((2*n)))
    while abs(current_el) > eps and n < 500:
        result += current_el
        n += 1
        current_el = ((-1)**n )*((x**(2*n))/factorial((2*n)))
    
    return result, n




