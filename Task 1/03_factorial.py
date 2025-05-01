n = int(input("Enter a positive integer: "))
factorial = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")

else: 
    for i in range(1,n +1):
        factorial *= i
    print("The factorial of", n, "is", factorial)
