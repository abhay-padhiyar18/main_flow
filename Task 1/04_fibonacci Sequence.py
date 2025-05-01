n = int(input("Enter the number of terms: "))

a,b = 0, 1

if n <= 0:
    print("Please enter a positive integer")

elif n==1:

    print("Fibonacci sequence up to",n,":")
    print(a)

else:   
    print("Fibonacci sequence:")
    print(a, ",", b, end=", ")
    for i in range(2,n):
        c = a + b
        print(c, end=", ")
        a = b
        b = c
