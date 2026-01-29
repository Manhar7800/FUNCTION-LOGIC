#Q 3: Write a function that accepts a list of numbers and returns the sum of all even numbers in the list.


def sum_even(numbers):
    total=0
    for num in numbers:
        if num%2==0:
            total+=num
    return total

l1=[1,2,3,4,5,6]
print(sum_even(l1))
