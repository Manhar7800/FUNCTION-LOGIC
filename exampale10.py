#Q 10: Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.


def divide_by(numbers):
    new_list=[]
    for n in numbers:
        if n%3==0:
          new_list.append(n)
    return new_list

lst=[1,2,3,4,5,6,7,8,9,10]
result=divide_by(lst)
print(result)
