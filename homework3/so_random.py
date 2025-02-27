import random
from functools import reduce

# Prefixes and suffixes for generating fantasy names
prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

# Function to create a fantasy name by randomly combining a prefix and a suffix
def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

# Function to capitalize the suffix
def capitalize_suffix(name):
    return name.capitalize()

# Apply capitalize_suffix to all suffixes
capitalized_suffixes = list(map(capitalize_suffix, suffixes))

# Generate 10 random fantasy names using list comprehension
random_names = [create_fantasy_name(prefixes, capitalized_suffixes) for _ in range(10)]

# Function to check if 'Fire' is in the name
def fire_in_name(name):
    return 'Fire' in name

# Function to concatenate two names
def concatenate_names(name1, name2):
    return name1 + ', ' + name2

# Filter names that include 'Fire'
filtered_names = list(filter(fire_in_name, random_names))

# Reduce the filtered names into a single string
if filtered_names:
    reduced_names = reduce(concatenate_names, filtered_names)
else:
    reduced_names = "No names contained 'Fire'."

# Function to display the generated names and results
def display_name_info():
    print("Generated Fantasy Names:")
    for name in random_names:
        print("-", name)

    print("\nFiltered Names (Containing 'Fire'):")
    print(filtered_names if filtered_names else "No matching names found.")

    print("\nConcatenated Filtered Names:")
    print(reduced_names)

# Run the display function
display_name_info()
