# https://www.youtube.com/watch?v=AFNel8vkVjY&list=PLDoG9_gnmpXe8rZfrSsnseglCJmyKmzi-&index=30

file = open("demo.txt", 'w')
file.write("This is the text written to the file")
file.close()


file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()


file = open("demo.txt", 'a')
file.write("This is a new line")
file.close()
