#Q 6: Write a function that accepts a string and a character, and returns the number of times the character appears in the string.


def count_char(string,character):
    count=0
    for i in string:
        if i==character:
            count+=1
    return count

txt="Manhar"# string
char="a"# character

result=count_char(txt,char)
print(result)

str1="manhar"
print(str1.count())