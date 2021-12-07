my_file = open("important-information.txt", "w+")

for i in range(10):
    my_file.write("These boots were made for walking")

my_file.close()