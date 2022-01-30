class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self,other):
        return self.length*self.width
    def __lt__(self, other):
        return self.area() < self.other
    l1=int(input("enter the length of 1st rectangle"))
    w1=int(input("enter the width of 1st rectangle"))
    rectangle1=(l1,w1)
    l2=int(input("enter the length of 2nd rectangle"))
    w2=int(input("enter the width of 2nd rectangle"))
    rectangle2=(l2,w2)
    if rectangle1 > rectangle2:
        print("rectangle1 is greater")
    else:
        print("rectangle2 is greater")
