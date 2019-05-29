print("enter a string to check for palindrome")
str=input()
revStr=reversed(str)
if(list(str)==list(revStr)):
    print("{} is palindrome".format(str))
else:
    print("Not a palindrome")

