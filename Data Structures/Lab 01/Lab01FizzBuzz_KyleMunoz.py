#Kyle Munoz
#Create a FizzBuzz Program

def main():
    for i in range(100):
        i = i + 1
        if i / 15 and i % 15 == 0:
            print("FizzBuzz")
        elif i / 5 and i % 5 == 0:
            print("Buzz")
        elif i / 3 and i % 3 == 0:
            print("Fizz")
        else:
            print(i)
main()
