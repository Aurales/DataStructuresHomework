#Kyle Munoz
#Make a program that ask for the chronological price of apples and calculates the best possible profit from a single purchase and sale of apples.
def main():
    apples = []
    applesvalue = []
    positiveapplevalue = []
    #Collect all apple values
    while True:
        try:
            apples.append(int(input("Please enter the prices of apples one at a time. If you have nothing left to enter press enter one more time: ")))
        except ValueError:
            break
    #Get the length of the list 
    applelistlength = len(apples)
    #Compare the price difference from one purchase to one sale
    for i in range(applelistlength):
        try:
            applesvalue.append((-1) * (apples[i] - apples[i+1]))
        except IndexError:
                break
    #Add all poitive values to new list
    for value in applesvalue:
        if value > 0:
            positiveapplevalue.append(value)
    for i in range(100):
        try:
            if positiveapplevalue[0] < positiveapplevalue[1]:
                del(positiveapplevalue[0])
            elif positiveapplevalue[0] < positiveapplevalue[2]:
                del(positiveapplevalue[0])
            elif positiveapplevalue[0] < positiveapplevalue[3]:
                del(positiveapplevalue[0])
            elif positiveapplevalue[0] < positiveapplevalue[4]:
                del(positiveapplevalue[0])
            elif positiveapplevalue[0] < positiveapplevalue[5]:
                del(positiveapplevalue[0])
        except IndexError:
            break
    greatestapplevalue = positiveapplevalue[0] 
    print("The greatest possible profit from the purchase and sale of apples is", greatestapplevalue, "units per apple.")
main()  
