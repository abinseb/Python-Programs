# Generate Fibonacci series of N terms

n = int(input("Enter the number"))
first = 0
second = 1
count = 0
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto",n,":")
    print(first)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(first)
        nth = first + second
        first = second
        second = nth
        count = count + 1

