#Q 11: Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.

def squere_no(numbers):
    new_list=[]
    for n in numbers:
        new_list.append(n*n)
    return new_list
    
l1=[1,2,3,4,5,6,7,8,9,10]
print(squere_no(l1))