
# using text file named demo.txt

# read to file
file = open("demo.txt", 'r')

data = file.read()
print(data)
file.close()


# write to file
file = open("demo.txt", 'a')

file.write("I want to learn python")
file.close()

