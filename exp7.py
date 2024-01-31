#Python Program to Check if a Number is Prime or not

num=int(input('Enter a number '))

flag = 0

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = 1
            break

print('<---The number is prime number--->' if flag==0 else '<---The number is not prime number--->')