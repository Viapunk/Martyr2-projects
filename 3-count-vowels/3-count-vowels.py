string = raw_input("Enter a string: ").lower()

vowels = ['a','e','i','o','u']
counter = 0
for v in vowels:
    if v in string:
        print v, string.count(v)