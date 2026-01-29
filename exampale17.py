#Q 17: Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.


def alternating_case(s):
    result=" "
    for i in range(len(s)):
        if i%2==0:
            result+=s[i].upper()
        else:
            result+=s[i].lower()
    return result

str=input("Enter the string:")
print(alternating_case(str))