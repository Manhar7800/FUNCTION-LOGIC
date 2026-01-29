#Q 16: Write a function that accepts a number and returns the sum of its digits.

def sum_of_digit(num):
    sum=0

    while num>0:
        sum+=num%10
        num//=10
    return sum

n=int(input("Enter the number:"))
print(sum_of_digit(n))