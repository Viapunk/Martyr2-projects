string = raw_input("Enter a string: ")

string = string.replace(" ","")
if string == string[::-1]:
    print "This string IS a palindrome."
else:
    print  "This string IS NOT a palindrome"