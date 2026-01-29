#Q 2: Write a function that accepts a string and returns True if the string is a palindrome, and False otherwise.


def is_palimdrome(s):
    return s==s[::-1]

txt=input("Enter the string:")
print(is_palimdrome(txt))