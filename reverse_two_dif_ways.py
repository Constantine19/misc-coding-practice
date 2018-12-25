def reverse_1(my_str):
    return my_str[::-1]

def reverse_2(my_str):
    return ''.join(reversed(my_str))

my_str = 'Netskope'
print reverse_1(my_str)
print reverse_2(my_str)