#Q 7: Write a function that accepts a list of strings and returns a new list with each string reversed.


def reverse_string(lst):
    return[s[::-1] for s in lst]

print(reverse_string(["HEllo","World"]))