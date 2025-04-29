def add_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is {result}.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def subtract_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
        print(f"The result of subtracting {num2} from {num1} is {result}.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

def display_message():
    print("Hello! Welcome to the Menu-Driven Program.")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Add Numbers")
        print("2. Subtract Numbers")
        print("3. Display a Message")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_numbers()
        elif choice == '2':
            subtract_numbers()
        elif choice == '3':
            display_message()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main_menu()
