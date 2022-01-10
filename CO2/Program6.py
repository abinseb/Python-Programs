# Count the number of character (character frequency) in a string
string = input("Enter a string:")
count = 0
for i in string:
    if i.isalpha():
        count = count+1
print("Number of characters in "+string+" is:",count)