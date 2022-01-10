#Find gcd of 2 numbers

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
i = 1
while(i <= n1 and i <= n2):
  if(n1 % i == 0 and n2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is:", gcd)


#method2
# import math
# print(math.gcd(x,y))
