#Q 5: Accept a number from the user and check if it is a prime number using a function with a parameter and return type.

def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True


num=int(input("Enter the number:"))
if prime(num):
    print("Prime number")
else:
    print("Not prime number")