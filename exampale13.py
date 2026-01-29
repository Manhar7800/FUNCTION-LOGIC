#Q 13: Write a function that accepts a number and prints its multiplication table from 1 to 10.


def multiplication_tabel(num):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

n=int(input("Enter the number:"))
multiplication_tabel(n)