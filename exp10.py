#factorial of a given Natural Number n using the recursive functions
def factorial(n):
     #if (n==1 or n==0):
     #     return 1
     #else:
     #     n * factorial(n - 1)
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
 

num = int(input('Enter the number to find factorial'))
print("Factorial of",num,"is",factorial(num))