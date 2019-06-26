# https://www.youtube.com/watch?v=W84g8vjuWIk&list=PLDoG9_gnmpXe8rZfrSsnseglCJmyKmzi-&index=29

file = open("demo.txt", 'w')
file.write("This is the text written to the file")
file.close()


file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()


file = open("demo.txt", 'w')
file.write("This is a new line")
file.close()
