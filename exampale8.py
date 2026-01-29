#Q 8: Write a function that accepts a list of numbers and returns the average of the numbers.


def avrage(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers)/len(numbers)

l1=[10,20,30,40]
print("Avrage:",avrage(l1))