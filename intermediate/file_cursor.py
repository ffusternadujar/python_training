# close implicit using with (context manager)
def count_ocurrences (character, filepath):
    with open(filepath, "r") as my_file:
        content = my_file.read()

    return content.count(character)

# count_ocurrences('a', 'files/bear.txt')

### Append text to an existing file
with open("files/fruits.txt", "a+") as my_file:
    my_file.write("\nbanana")
    my_file.seek(0)
    print(my_file.read())