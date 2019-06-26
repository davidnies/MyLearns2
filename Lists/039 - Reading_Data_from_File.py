# https://www.youtube.com/watch?v=BCNRHvuHT-I&list=PLDoG9_gnmpXe8rZfrSsnseglCJmyKmzi-&index=28

file = open("demo.txt", 'r')
content = file.readline()
print(content)
file.close()


# write to file
file = open("demo.txt", 'a')

file.write("I want to learn python")
file.close()
