class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return(2*(self.length+self.breadth))



r1=rectangle(2,4)
r2=rectangle(3,5)
print("Area of rectangle1:", r1.area())
print("Area of rectangle2:", r2.area())
print("perimeter of rectangle1:", r1.perimeter())
print("Perimeter of rectangle2:", r2.perimeter())

if(r1.area()>r2.area()):
    print("rectangle1 is greater")
else:
    print("rectangle2 is greaiter")