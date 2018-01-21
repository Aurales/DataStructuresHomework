#Kyle Munoz
#Make a program that ask for the chronological price of apples and calculates the best possible profit.
def main():
    apples = [14,6,9,7,8,10,3,9]
    applesvalue = []
##    while True:
##        try:
##            apples.append(int(input("Please enter the prices of apples one at a time: ")))
##            print(apples)
##        except ValueError:
##            break
    applelistlength = len(apples)
    for apple in apples:
        difference = int(apples[apple]) - int(apples[apple])
        print(difference)
   
main()
