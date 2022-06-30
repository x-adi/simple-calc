import time
import math

print('''Welcome to Calculator. This Calculator can Calculate the following things -
\n[-] Addition
[-] Subtraction
[-] Division
[-] Multiplication
[-] Square and Square Root
[-] Cube and Cube Root\n
''')
def main():
    time.sleep(1)
    a = input(''' What do you want to do?
    a - Addition
    b - Subtraction
    c - Division
    d - Multiplication
    e - Square
    f - Square Root
    g - Cube
    h - Cube Root
    \nEnter the corresponding alphabet here - 
    ''')
    if a == "a":
        print("\nA D D I T I O N\n")
        time.sleep(0.5)
        b=float(input("Enter first number "))
        b=b+float(input("Enter second number "))
        print("\nSum is ", b)

        r = input("Do you want to do anything else? (y/n)")
        if r == "y":
            time.sleep(0.5)
            main()
        elif r == "n":
            input("Thank you for using Calculator. Press Enter Key to exit this program...")
        else:
            print("Invalid alphabet...")
            main()

    elif a == "b":
        print("\nS U B T R A C T I O N\n")
        time.sleep(0.5)
        b=float(input("Enter first number "))
        b=b-float(input("Enter second number "))
        print("\nDifference is ", b)

        r = input("Do you want to do anything else? (y/n)")
        if r == "y":
            time.sleep(0.5)
            main()
        elif r == "n":
            input("Thank you for using Calculator. Press Enter Key to exit this program...")
        else:
            print("Invalid alphabet...")
            main()

    elif a == "c":
        print("\nD I V I S I O N\n")
        time.sleep(0.5)
        b=float(input("Enter first number "))
        b=b/float(input("Enter second number "))
        print("\nQuotient is ", b)

        r = input("Do you want to do anything else? (y/n)")
        if r == "y":
            time.sleep(0.5)
            main()
        elif r == "n":
            input("Thank you for using Calculator. Press Enter Key to exit this program...")
        else:
            print("Invalid alphabet...")
            main()
        
    elif a == "d":
        print("\nM U L T I P L I C A T I O N\n")
        time.sleep(0.5)
        b=float(input("Enter first number "))
        b=b*float(input("Enter second number "))
        print("\nProduct is ", b)

        r = input("Do you want to do anything else? (y/n)")
        if r == "y":
            time.sleep(0.5)
            main()
        elif r == "n":
            input("Thank you for using Calculator. Press Enter Key to exit this program...")
        else:
            print("Invalid alphabet...")
            main()

    elif a == "e":
        print("\nS Q U A R E\n")
        time.sleep(0.5)
        b=float(input("Enter any number "))
        b=b * b
        print("\nSquare is ", b)

        r = input("Do you want to do anything else? (y/n)")
        if r == "y":
            time.sleep(0.5)
            main()
        elif r == "n":
            input("Thank you for using Calculator. Press Enter Key to exit this program...")
        else:
            print("Invalid alphabet...")
            main()
    
    elif a == "f":
        print("\nS Q U A R E - R O O T\n")
        time.sleep(0.5)
        b=float(input("Enter any number "))
        b=math.sqrt(b)
        print("\nSquare root is ", b)

        r = input("Do you want to do anything else? (y/n)")
        if r == "y":
            time.sleep(0.5)
            main()
        elif r == "n":
            input("Thank you for using Calculator. Press Enter Key to exit this program...")
        else:
            print("Invalid alphabet...")
            main()

    elif a == "g":
        print("\nC U B E\n")
        time.sleep(0.5)
        b=float(input("Enter any number "))
        b=b * b * b
        print("\nCube is ", b)

        r = input("Do you want to do anything else? (y/n)")
        if r == "y":
            time.sleep(0.5)
            main()
        elif r == "n":
            input("Thank you for using Calculator. Press Enter Key to exit this program...")
        else:
            print("Invalid alphabet...")
            main()
        
    elif a == "h":
        print("\nC U B E - R O O T\n")
        time.sleep(0.5)
        b=float(input("Enter any number "))
        b=b ** (1/3)
        print("\nCube root is ", b)

        r = input("Do you want to do anything else? (y/n)")
        if r == "y":
            time.sleep(0.5)
            main()
        elif r == "n":
            input("Thank you for using Calculator. Press Enter Key to exit this program...")
        else:
            print("Invalid alphabet...")
            main()

    else:
        print("Invalid alphabet...")
        time.sleep(0.5)
        main()

main()
