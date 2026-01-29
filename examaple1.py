#Q 1: Accept a number from the user and find the factorial of the number using a function with a parameter and return type.


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

num=int(input("enter the number:"))
result=factorial(num)
print(result)


