#Q 12: Write a function that accepts a string and counts how many vowels are in the string.


def vowels_count(s):
    vowels="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count

str=input("Enter the string:")
print(vowels_count(str))