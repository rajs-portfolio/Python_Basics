a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
original_a, original_b = a, b  # Store the original values for the final output

while b != 0:
    a, b = b, a % b

print(f"GCD of {original_a} and {original_b} is {a}")
