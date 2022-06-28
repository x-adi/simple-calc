import time
import math

message= "Do you want to do anything else? (y/n)"
tqmess= "\nThank you for using calculator. This program will exit in 5 seconds."

print('''Welcome to Calculator
This calculator can calculate the following things -\n
[-] Addition 
[-] Subtraction
[-] Division
[-] Multiplication
[-] Square
[-] Square root
[-] Cube
[-] Cube root\n
''')
def main():
    time.sleep(1)
    a=input('''\nWhat do you want to do-\n
    a - Addition
    b - Subtraction
    c - Division
    d - Multiplication
    e - Square
    f - Square root
    g - Cube
    h - Cube root
    \nEnter the corresponding alphabet here ''')
    if a == "a":
        print("\nA D D I T I O N")
        time.sleep(0.5)
        b=float(input("\nEnter first number "))
        c=float(input("Enter second number "))
        d= b + c
        time.sleep(1)
        print("\nSum is ", d)
        r=input(message)
        if r == "y" or r == "Y":
            main()
        else:
            print(tqmess)
            time.sleep(5)
    
    elif a == "b":
        print("\nS U B T R A C T I O N")
        time.sleep(0.5)
        b=float(input("Enter first number "))
        c=float(input("Enter second number "))
        d= b - c
        time.sleep(1)
        print("\nDifference is ", d)
        r=input(message)
        if r == "y" or r == "Y":
            main()
        else:
            print(tqmess)
            time.sleep(5)
    
    elif a == "c":
        print("\nD I V I S I O N")
        time.sleep(0.5)
        b=float(input("\nEnter first number "))
        c=float(input("Enter second number "))
        d= b / c
        time.sleep(1)
        print("\nQuotient is ", d)
        r=input(message)
        if r == "y" or r == "Y":
            main()
        else:
            print(tqmess)
            time.sleep(5)

    elif a == "d":
        print("\nM U L T I P L I C A T I O N")
        time.sleep(0.5)
        b=float(input("\nEnter first number "))
        c=float(input("Enter second number "))
        d= b * c
        time.sleep(1)
        print("\nProduct is ", d)
        r=input(message)
        if r == "y" or r == "Y":
            main()
        else:
            print(tqmess)
            time.sleep(5)

    elif a == "e":
        print("\nS U A R E")
        time.sleep(0.5)
        b=float(input("\nEnter a number "))
        c= b * b
        time.sleep(1)
        print("\nSquare is ", c)
        r=input(message)
        if r == "y" or r == "Y":
            main()
        else:
            print(tqmess)
            time.sleep(5)

    elif a == "f":
        print("\nS Q U A R E - R O O T\n")
        time.sleep(0.5)
        b=float(input("\nEnter a number "))
        c= math.sqrt(b)
        time.sleep(1)
        print("\nSquare root is ", c)
        r=input(message)
        if r == "y" or r == "Y":
            main()
        else:
            print(tqmess)
            time.sleep(5)
    
    elif a == "g":
        print("\nC U B E\n")
        time.sleep(0.5)
        b=float(input("\nEnter any number "))
        c= b * b * b
        time.sleep(1)
        print("\nCube is ", c)
        r=input(message)
        if r == "y" or r == "Y":
            main()
        else:
            print(tqmess)
            time.sleep(5)

    elif a == "h":
        print("\nC U B E - R  O O T \n")
        time.sleep(0.5)
        b=float(input("\nEnter any number "))
        c = b ** (1/3)
        time.sleep(0.5)
        print("\nCube root is ", c)
        r=input(message)
        if r == "y" or r == "Y":
            main()

        else:
            print(tqmess)
            time.sleep(5)

    else:
        print("\nInvalid alphabet.")
        main()

main()
