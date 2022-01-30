class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second

    def __add__(self,other):
        second=self.__second+other.__second
        minute=self.__minute+other.__minute
        hour=self.__hour+other.__hour

        if second>60:
            minute+=int(second/60)
            second=second % 60

        if minute>60:
            hour+=int(minute/60)
            minute=minute % 60

        time = "{0} Hours: {1} minutes: {2} seconds".format(hour, minute, second)
        return time
h1=int(input("enter the hours of first time\t"))
m1=int(input("enter the minute of first tome\t"))
s1=int(input("enter the 1st second \t"))

h2=int(input("enter 2nd hour\t"))
m2=int(input("enter the 2nd minute"))
s2=int(input("enter the 2nd second"))

time1=Time(h1,m1,s1)
time2=Time(h2,m2,s2)
print("sum of the time=",time1 + time2)
