with open("example.txt", "r") as file:
    file.seek(0,2)
    line = file.readline()
    print (line)