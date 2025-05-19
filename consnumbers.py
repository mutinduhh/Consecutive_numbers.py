# This program generates 10 consecutive whole numbers starting from a user-defined number.
# It then separates these numbers into even and odd categories and prints them.
print("Enter the starting whole number:")
start = int(input())  

# Generate 10 consecutive numbers
numbers = [start + i for i in range(10)]

# Separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the results
print("\nThe 10 consecutive whole numbers are:")
print(numbers)

print("\nEven numbers are:")
print(even_numbers)

print("\nOdd numbers are:")
print(odd_numbers)
