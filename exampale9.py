"""Q 9:Accept a string from the user and print it in uppercase if the length of the
string is greater than 5, else print it in lowercase using a function."""


def check_string(s):
    if len(s) > 5:
        print(s.upper())
    else:
        print(s.lower())

# Input from user
text = input("Enter a string: ")
check_string(text)
