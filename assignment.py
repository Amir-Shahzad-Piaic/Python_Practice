def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Get user input
user_name = input("What's your name? ")
print(f"Hello, {user_name}! Welcome to the number explorer.")

# Collect favorite numbers
numbers = []
for i in range(3):
    while True:
        try:
            number = int(input(f"Enter your favorite number #{i + 1}: "))
            numbers.append(number)
            break
        except ValueError:
            print("Please enter a valid integer.")

# Create list of tuples indicating if each number is even or odd
even_odd_list = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

# Print the even/odd information
print("\nHere's the information about your numbers:")
for num, type_ in even_odd_list:
    print(f"The number {num} is {type_}.")

# Create list of tuples with numbers and their squares
squares_list = [(num, num ** 2) for num in numbers]

# Print the numbers and their squares
print("\nHere's the square of each number:")
for num, square in squares_list:
    print(f"The square of {num} is {square}.")

# Calculate the sum of the numbers
sum_of_numbers = sum(numbers)
print(f"\nThe sum of your favorite numbers is: {sum_of_numbers}")

# Check if the sum is a prime number
if is_prime(sum_of_numbers):
    print("Wow! The sum of your numbers is a prime number!")
else:
    print("The sum of your numbers is not a prime number, but it’s still interesting!")

print("Thank you for exploring numbers with us. Have a great day!")

