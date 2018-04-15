def addDigits(num):
    num = int(num)
    if num < 10:
        return num
    else:
        return addDigits(num/10) + num%10
    #your solution here


print(addDigits(input("Enter a number: ")))
