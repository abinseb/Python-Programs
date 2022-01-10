# List comprehension
number = []
n = int(input("Enter the list size"))
i = 1
for i in range(n):
    item = input("Enter the element  "+str(i)+" position")
    number.append(item)
print(number)

# (a) Generate positive list of numbers from a given list of integer

print("Positive Numbers from given list are")
for i in range(len(number)):
    number[i] = int(number[i])

    if number[i] >= 0:
       print(number[i])

# (b) Square of N numbers

print("Square of element in the list are")
squared_numbers = [i ** 2 for i in number]
print(squared_numbers)
# (c) Form a list of vowels selected from a given word
word = []
w = input("Enter the Word")
list1=[]
vowels = ['a','e','i','o','u','A','E','I','O','U']
for i in w:
    if ( i in vowels and i not in list1 ):
        list1.append(i)
print(list1)

# (d) List ordinal value of each element of a word(Hint:Use ord() to get ordinal values)

vale = []
word = list(w)
length=len(word)
print("Ordinal value of each element in the word  ")
i=0
for i in range(length):
    value=ord(word[i])
    print(word[i],+value)

    © 2022 GitHub, Inc.

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

