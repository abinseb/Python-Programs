#Display future leap years from current year to a final year entered by user.

start = int(input("Enter start year"))
end = int(input("Enter end year"))
if start < end:
    print("Leap years between  "+str(start) + "  and  " + str(end))
    while start < end:
        if start % 4 ==0 and start % 100 != 0:
            print(start)
        if start % 100 ==0 and start % 400 == 0:
            print(start)
        start = start+1
else:
    print("check your year input")
