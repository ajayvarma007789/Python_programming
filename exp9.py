#python program to sort the list in an ascending order without using any built in functions.

#user defined function to sort
def sort(list):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] >= list[j]:
                list[i], list[j] = list[j], list[i]

    print("Sorted List", list)

list = []
num = int(input("enter size of the array: "))

for i in range(0, num):
    element = int(input())
    list.append(element)

print("Original List:", list)

sort(list)

