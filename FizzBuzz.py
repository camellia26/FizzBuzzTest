count = 1

while(count <= 100):
    if(count % 15 == 0):
        print("FizzBuzz")
    elif(count % 3 == 0):
        print("Fizz")
    elif(count % 5 == 0):
        print("Buzz")
    elif(count % 7 == 0):
        print("GitHub")
    else:
        print(count)
    count += 1
