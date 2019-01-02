"""
How to find a square root, without using "math.sqrt" function
"""


def square_root(a):
    current_val = a / 2.0
    square = current_val ** 2
    while abs(square - a) > 0.001:
        if square > a:
            current_val = current_val / 2.0
            square = current_val ** 2
        else:
            current_val = current_val * 2.0
            square = current_val ** 2

    return current_val


a = 16
print "+-", square_root(a)
