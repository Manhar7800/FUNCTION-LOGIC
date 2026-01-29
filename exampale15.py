#Q 15: Write a function that accepts a number and checks if it is an Armstrong number.


def is_armstrong(num):
    temp=num
    digits=len(str(num))
    total=0

    while temp>0:
        digit=temp%10
        total+=digit**digits
        temp//=10
    return total==num

n=int(input("Enter the number:"))
if is_armstrong(n):
    print("Numbar is armstrong:")
else:
    print("Number is NOt aramstrong:")

