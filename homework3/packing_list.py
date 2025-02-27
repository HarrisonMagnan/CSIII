import csv

# Packing list data
data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

# Try to read the packing list; if it doesn't exist, create one
try:
    with open('packing_list.csv', 'r') as file:
        reader = csv.reader(file)
        print("Current Packing List:")
        for row in reader:
            print(row)

except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")
    with open('packing_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("New packing list created successfully.")
