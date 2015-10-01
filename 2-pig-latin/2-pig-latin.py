string = raw_input("Give a word: ")
vowels = ['a','e','i','o','u']
if string[0:1] in vowels:
    print(string+"way");
else:
    print(string[1:]+string[0:1]+"ay")
