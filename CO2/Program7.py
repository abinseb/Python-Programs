# Add th 'ing' at the end of the given string.If it already ends with 'ing' , then add 'ly'

str = input("Enter a string:")
if str.endswith("ing"):
    string = str + "ly"
else:
    string = str + "ing"
print("Modified string is:",str)


# Method 2
# if s[-3:]=="ing":
#    print(s+"ly")
# else:
#    print(s+"ly")