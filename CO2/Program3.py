# Find the sum of all items in a list
myList = []
n = int(input("Enter the size of List"))
for i in range(0,n):
    item = int(input("Enter the element"))
    myList.append(item)
print(myList)
print("Sum Of all elements in the list")
sum = 0
for i in range(0,n):
    sum = sum + myList[i]
print(sum)    