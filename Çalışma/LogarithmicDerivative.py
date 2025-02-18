import math

print("*******************************\nDerivatives of Logarithmic Expressions\n*******************************")
print("\nF: R^+ -> R ve a ∈ R^+ - {-1}")


def log(a, x):
    operation = 1 / (x * math.log(a, math.e))
    return operation


def ln(x):
    operation = 1 / x
    return operation


def derivative(b, n):
    b, n = b * n, n - 1
    return print("(", b, "x^", n, ")", sep="")


def function(a, b, n, r):
    return print("(", b, "x^", n, "+", r, ")", " * ", math.log(a, math.e), sep="")


def functional(a, n, r, b):
    derivative(b, n), print("-----------------------------"), function(a, b, n, r)


def ln_derivative(b, n, r):
    return derivative(b, n), print("--------"), function(b, n, r)


while True:

    print("\n1.log \n2.ln \n3.log(function) \n4.ln(function)")
    secim = int(input("\nSelect the Statement to derivative = "))

    if secim == 1:
        a = int(input("Enter Base = "))
        x = int(input("Enter Top = "))
        islem = math.log(x, a)
        if islem == int(islem):
            print("Derivative = 0")
        else:
            print("Derivative = ", log(a, x))

    elif secim == 2:
        x = int(input("Üssü Giriniz = "))
        print("Derivative = ", ln(x))

    elif secim == 3:
        a = int(input("Enter Base = "))
        n = int(input("Enter X top = "))
        r = int(input("Enter the Constant Number = "))
        b = int(input("Enter the Coefficient of X = "))
        print("\nDerivative = \n")
        functional(a, n, r, b)

    elif secim == 4:
        n = int(input("Enter X top = "))
        r = int(input("Enter the Constant Number = "))
        b = int(input("Enter the Coefficient of X = "))
        print("\nDerivative = \n")
        ln_derivative(b, n, r)
