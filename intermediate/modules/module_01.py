import time
import os

while True:
    if os.path.exists("../files/fruits.txt"):
        with open("../files/fruits.txt") as file:
            print(file.read())
    else:
        print("File not found")
    time.sleep(10)

