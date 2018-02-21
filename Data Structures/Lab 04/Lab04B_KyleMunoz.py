#Kyle Munoz
#
import time
#Linear Fib
def fib(n):
    x = 1
    y = 1
    z = 0
    for i in range(n):
        z = x + y
        x = y
        y = z
    return(x)
    print(x)

#Recursive Fib
def recursivefib(n):
    if (n <= 1):
        return 1
    else:
        return recursivefib(n-1) + recursivefib(n-2)
#Dynamic Fib
n = 35
key = [1,1]
for i in range(n):
    key.append(0)


def dynfib(x):
    #Check for x in the list
    #if x = 0, calculate and store
    #otherwise, return value from list
    #print(key)
    if key[x] == 0:
       key[x] = fib(x-1) + fib(x-2)
    return key[x]




def main():
    for x in range(100):
            key.append(0)
    for i in range(30,101,10):
        starttime = time.time()
        dynfib(i)
        endtime = time.time()
        totaltime = endtime - starttime
        print("It took", totaltime, "seconds to do the dynamic Fibonacci sequence of", i)
    for i in range(30,101,10):
        starttime = time.time()
        fib(i)
        endtime = time.time()
        totaltime = endtime - starttime
        print("It took", totaltime, "seconds to do the linear Fibonacci sequence of", i)
    for i in range(30,101,10):
        starttime = time.time()
        recursivefib(i)
        endtime = time.time()
        totaltime = endtime - starttime
        print("It took", totaltime, "seconds to do the recursive Fibonacci sequence of", i)

main()
