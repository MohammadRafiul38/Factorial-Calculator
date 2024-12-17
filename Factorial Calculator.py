while True:
    n = input("Type a number you want to factorial (Press 0 to exit) : ")
    n = int(n)

    if n == 0:
        print("The program has been stopped")
        break

    res = 1

    for num in range(1, n + 1):
        res = res * num
        
    print("Factorial of your number", n, "is : ", res)