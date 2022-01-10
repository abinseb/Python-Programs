# Accept a list of words and reyorn length of length of longest word

word = input("Enter some words separated by commas:")
word_lst=word.split(",")
longest = len(word_lst[1])
for i in word_lst:
    if len(i) > longest:
        longest=len(i)
print("Length of longest word in the list is:",longest)