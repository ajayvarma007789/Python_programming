#Python Program to Check if a Number is Palindrome or not

a=int(input("Enter the number to be checked: "))
temp=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
print("The number is palindrome!" if temp==rev else "The number is not a paliandrome?!")
