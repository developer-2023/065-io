# docs.python.org/3/library/functions.html#open
# 7:19:20 Harvard CS50’s Introduction to Programming with Python – Full University Course

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())
