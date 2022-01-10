# Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square
l = int(input("Enter the lower range:"))
u = int(input("Enter the upper range:"))
a=[]
a=[x for x in range(l,u+1) if (int(x**0.5))**2==x and x%2==0]
print(a)