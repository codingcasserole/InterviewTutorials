from factorials import factorial
print("testing function for input: 5")
five_factorial=factorial(5)
if five_factorial == 120:
    print("   pass")
else:
    print("   fail")
print("testing function for input: 12")
five_factorial=factorial(12)
if five_factorial == 479001600:
    print("   pass")
else:
    print("   fail")
print("testing function for input: 2")
five_factorial=factorial(2)
if five_factorial == 2:
    print("   pass")
else:
    print("   fail")
print("testing function for input: 1")
five_factorial=factorial(1)
if five_factorial == 1:
    print("   pass")
else:
    print("   fail")
print("testing function for input: 0")
five_factorial=factorial(0)
if five_factorial == 1:
    print("   pass")
else:
    print("   fail")
print("testing function for input: -3")
five_factorial=factorial(-3)
if five_factorial == -1:
    print("   pass")
else:
    print("   fail")

