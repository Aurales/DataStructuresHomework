#Kyle Munoz
#Create a program that ask for input of a text files and produces a text file but now with lines numbers.
def main():
    file = input("Please enter the name of a text file: ")
    modfile = open(file, "r")
    filelines = modfile.readlines()
    linenumber = 1
    modfile.close()
    modfile = open(file, "w")
    for i in filelines:
        print(linenumber, i, file = modfile)
        linenumber = linenumber + 1
    modfile.close()
main()
