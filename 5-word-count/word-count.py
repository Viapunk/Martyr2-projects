#Program reads from a file input.txt, then give's an output to a file output.txt
input_file = open("input.txt", 'r')
output_file = open("output.txt",'w+')

string = input_file.read().split()
output_file.write("Number of words in sentence: %d" % len(string))

input_file.close()
output_file.close()