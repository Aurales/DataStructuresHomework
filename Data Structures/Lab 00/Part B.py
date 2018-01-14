text = open("sample.txt", "r")
text = text.readlines()
linenumber = 1
for i in text:
    print(linenumber, i)
    linenumber = linenumber + 1
