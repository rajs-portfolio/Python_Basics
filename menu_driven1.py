def getfactor(x):
    factors = [i for i in range(1, x + 1) if x % i == 0]
    return factors

def isprime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def iscomposite(x):
    return not isprime(x) and x > 1

def isperfect(x):
    return sum(i for i in range(1, x) if x % i == 0) == x

def isabundance(x):
    return sum(i for i in range(1, x) if x % i == 0) > x

def menu():
    while True:
        print("\nMenu:")
        print("1. Get factors of a number")
        print("2. Check if a number is prime")
        print("3. Check if a number is composite")
        print("4. Check if a number is perfect")
        print("5. Check if a number is abundant")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            x = int(input("Enter a number: "))
            print(f"Factors of {x}: {getfactor(x)}")

        elif choice == 2:
            x = int(input("Enter a number: "))
            print(f"{x} is prime: {isprime(x)}")

        elif choice == 3:
            x = int(input("Enter a number: "))
            print(f"{x} is composite: {iscomposite(x)}")

        elif choice == 4:
            x = int(input("Enter a number: "))
            print(f"{x} is perfect: {isperfect(x)}")

        elif choice == 5:
            x = int(input("Enter a number: "))
            print(f"{x} is abundant: {isabundance(x)}")

        elif choice == 6:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

menu()