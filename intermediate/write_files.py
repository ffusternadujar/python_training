with open("files/vegetables.txt", "w") as my_file:
    # if file exists, content will be overridden
    my_file.write("Tomato\nOnion\nCucumber\n")
    my_file.write("Garlic")

