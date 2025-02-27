# Step 1: Write a secret message to a file
sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

# Step 2: Read the original message and modify it
with open('sent_message.txt', 'r+') as file:
    # Read and print the original message
    original_message = file.read()
    print("Original Message:", original_message)
    
    # Move the cursor to the beginning of the file
    file.seek(0)
    
    # New message to replace the old one
    unsent_message = 'This message has been unsent.'

    # Write the new message
    file.write(unsent_message)

    # Truncate to ensure old content is removed
    file.truncate(len(unsent_message))

# Step 3: Read and print the modified message
with open('sent_message.txt', 'r') as file:
    modified_message = file.read()
    print("Modified Message:", modified_message)
