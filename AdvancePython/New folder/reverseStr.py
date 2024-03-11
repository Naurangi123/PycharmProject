def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                  
        new_string += a_string[index]
    return new_string