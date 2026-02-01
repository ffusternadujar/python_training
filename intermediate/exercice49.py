with open("files/data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    print(content)
    content *= 2
    print(content)
    file.write(content)