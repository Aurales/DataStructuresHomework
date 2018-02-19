#Kyle Munoz
#Collatz Conjecture Recursively

def CollatzConjecture(n, c = 0):
    if n == 1:
        print("Steps Taken: ",c)
    elif n % 2==0:
        return CollatzConjecture(n/2, c + 1)   
    else:
        return CollatzConjecture(((n * 3) + 1), c + 1)



def main():
    x = int(input("What number would you like to try? "))
    CollatzConjecture(x, c = 0)

main()
