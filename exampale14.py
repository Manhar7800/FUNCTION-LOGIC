#Q 14: Write a function that accepts a list of strings and returns the longest string in the list.

def longest_string(lst):
    return max(lst,key=len)

word=["apple","banana","cat"]
print(longest_string(word))