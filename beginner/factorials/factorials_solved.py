def factorial(n):
    if n < 0:
        print("Factorials do not exist below zero")
        return -1
    elif (n == 0) or (n == 1):
        return 1
    elif n > 1:
        product=1
        for x in range(2, n+1):
            product=product*x
        return product
