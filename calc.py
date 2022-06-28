import time #IMPORTS TIME FROM OS#
import math #IMPORTS MATH MODULE

print("Welcome to Calculator")
print("This Calculator will calculate the following things- ")
print("\n[-] Addition")
print("[-] Subtraction")
print("[-] Division")
print("[-] Multiplication")
print("[-] Square and Square root")
print("[-] Cube and Cube root")
time.sleep(1)

def script():
    print("\nWhat do you want to do?")
    print("\na - Addition")
    print("b - Subtraction")
    print("c - Division")
    print("d - Multiplication")
    print("e - Square")
    print("f - Square root")
    print("g - Cube")
    print("h - Cube root")
    a=input("\nEnter the corresponding alphabet here. ")


    #ADDTION STARTS HERE#

    if a == "a":
        time.sleep(1)
        print("\nA D D I T I O N")
        time.sleep(1)
        b=float(input("\nEnter first number "))
        time.sleep(1)
        c=float(input("Enter second number "))
        d=b + c
        time.sleep(1)
        print("\nSum is " + str(d))

    
        r = input("\nDo you want to do anything more? If yes then then enter 'y' and if no then enter 'n' ")
        if r == "Y" or r == "y":
            script()   
        elif r ==str("n") or r ==str("N"):
            print("\nThank you for using Calculator. This program will close in 3 seconds...")
            time.sleep(3)


    #SUBTRACTION STARTS HERE#

    elif a == "b":
        time.sleep(1)
        print("\nS U B T R A C T I O N")
        time.sleep(1)
        e=float(input("\nEnter first number "))
        time.sleep(1)
        f=float(input("Enter second number "))
        g=e - f
        time.sleep(1)
        print("\nDifference is " + str(g))
        r = input("\nDo you want to do anything more? If yes then then enter 'y' and if no then enter 'n' ")
        if r == "Y" or r == "y":
            script()   
        elif r ==str("n") or r ==str("N"):
            print("\nThank you for using Calculator. This program will close in 3 seconds...")
            time.sleep(3)

    #MULTIPLICATIONS STARTS HERE#

    elif a == "d":
        time.sleep(1)
        print("\nM U L T I P L I C A T I O N")
        time.sleep(1)
        h=float(input("\nEnter first number "))
        time.sleep(1)
        i=float(input("Enter second number "))
        j=h * i
        time.sleep(1)
        print("\nProduct is " + str(j))
        r = input("\nDo you want to do anything more? If yes then then enter 'y' and if no then enter 'n' ")
        if r == "Y" or r == "y":
            script()   
        elif r ==str("n") or r ==str("N"):
            print("\nThank you for using Calculator. This program will close in 3 seconds...")
            time.sleep(3)

    #DIVISION STARTS HERE#

    elif a == "c":
        time.sleep(1)
        print("\nD I V I S I O N")
        time.sleep(1)
        k=float(input("\nEnter first number "))
        time.sleep(1)
        l=float(input("Enter second number "))
        m=k / l
        time.sleep(1)
        print("\nQuotient is " + str(m))
        r = input("\nDo you want to do anything more? If yes then then enter 'y' and if no then enter 'n' ")
        if r == "Y" or r == "y":
            script()   
        elif r ==str("n") or r ==str("N"):
            print("\nThank you for using Calculator. This program will close in 3 seconds...")
            time.sleep(3)

    #SQUARE STARTS HERE#

    elif a == "e":
        time.sleep(1)
        print("\nS Q U A R E")
        time.sleep(1)
        n=float(input("\nEnter any number "))
        o= n * n
        time.sleep(1)
        print("\nSquare is " + str(o))
        r = input("\nDo you want to do anything more? If yes then then enter 'y' and if no then enter 'n' ")
        if r == "Y" or r == "y":
            script()   
        elif r ==str("n") or r ==str("N"):
            print("\nThank you for using Calculator. This program will close in 3 seconds...")
            time.sleep(3)

    #CUBE STARTS HERE#

    elif a == "g":
        time.sleep(1)
        print("\nC U B E")
        time.sleep(1)
        p=float(input("\nEnter any number "))
        q= p * p * p
        time.sleep(1)
        print("\nCube is " + str(q))
        r = input("\nDo you want to do anything more? If yes then then enter 'y' and if no then enter 'n' ")
        if r == "Y" or r == "y":
            script()   
        elif r ==str("n") or r ==str("N"):
            print("\nThank you for using Calculator. This program will close in 3 seconds...")
            time.sleep(3)

    #SQUARE ROOT STARTS FROM HERE#

    elif a == "f":
        time.sleep(1)
        print("\nS Q U A R E - R O O T")
        time.sleep(1)
        u=float(input("\nEnter a number "))
        v=math.sqrt(u)
        print("\nSquare root is " + str(v))
        r = input("\nDo you want to do anything more? If yes then then enter 'y' and if no then enter 'n' ")
        if r == "Y" or r == "y":
            script()   
        elif r ==str("n") or r ==str("N"):
            print("\nThank you for using Calculator. This program will close in 3 seconds...")
            time.sleep(3)

    #CUBE ROOT STARTS FROM HERE#

    elif a == "h":
        time.sleep(1)
        print("\nC U B E - R O O T")
        time.sleep(1)
        r=float(input("\nEnter any number "))
        s=r ** (1./3.)
        print("\nCube root is " + str(s))
        r = input("\nDo you want to do anything more? If yes then then enter 'y' and if no then enter 'n' ")
        if r == "Y" or r == "y":
            script()   
        elif r ==str("n") or r ==str("N"):
            print("\nThank you for using Calculator. This program will close in 3 seconds...")
            time.sleep(3)

    else:
        print("\nInvalid alphabet...")
        time.sleep(3)
        script()
script()
