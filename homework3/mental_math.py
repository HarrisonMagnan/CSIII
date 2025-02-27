# List of numbers
numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

# Using list comprehension to filter even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Using list comprehension to filter odd numbers (Bonus)
odd_numbers = [num for num in numbers if num % 2 != 0]

# Printing the results
print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
