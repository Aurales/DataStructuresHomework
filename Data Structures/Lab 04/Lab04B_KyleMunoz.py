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
key = []
value = []
def dynamicfib(n):
    if n <= 1:
        key.append(n)
        value.append(1)
        return 1
    else:
        if n in key:
            ind = key.index(n)
##            print("index:",ind)
##            print("key list", key)
##            print("value list",value)
            return value[ind]
        else:
            value.append(dynamicfib(n-1) + dynamicfib(n-2))
            key.append(n)
            ind = key.index(n)
##            print("index b:",ind)
##            print("key list b", key)
##            print("value list b",value)
            return value[ind]


def main():
    for i in range(30,101,10):
        starttime = time.time()
        dynamicfib(i)
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
