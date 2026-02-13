import os
import time
import pandas

while True:
    if os.path.exists("../files/temps_today.csv"):
        content = pandas.read_csv("../files/temps_today.csv")
        print(content.mean())
    else:
        print("File not found")
    time.sleep(10)