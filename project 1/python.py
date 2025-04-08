#edge case for create = number and symbols in name and grade can be a number above 12 
#edge case for read = insted of letting you reenter  aid after entering one that does not exist it takes you back to teh menu insted and you ar enot able to reda muliple peoples data at once 
#edge case for update = when adding a class it adds it to the csv file but only adds the  grade in that class to the one person you added it to and when updating a studnets grad eyou can make it letters that do not have to do with teh grade 
#edge case for delete = cant delete multiple studnets at once and if a studnet is deleted there id becomes open to be taken which can lead to duplicates 

import csv
import os
import re

# Define CSV file
CSV_FILE = "s_data.csv"

# GPA scale with letter grades
GPA_SCALE = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "F": 0.0
}

GRADE_SIGNS = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

# Secret names
SECRET_NAMES = {
    "albert einstein": "A genius has entered the system! Prepare for greatness!",
    "isaac newton": "Welcome, great physicist! Ready to discover gravity again?",
    "bruce wayne": "Are you sure you should be here? Gotham needs you!",
    "tony stark": "Mr. Stark, shouldn't you be building a new Iron Man suit?"
}

# Secret answer
SECRET_ANSWERS = {
    "42": "The Answer to the Ultimate Question of Life, the Universe, and Everything!",
    "i don't know": "Admitting ignorance is the first step to wisdom!",
    "yoda": "Do or do not, there is no try. But you, my young padawan, passed the quiz!"
}

#both
# Ensure the CSV file exists with headers
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "First Name", "Last Name", "Grade", "Email", "Phone", "Date of Birth", "Address", "History", "English", "Math", "Science", "GPA"])
 
#both            
# Function to adjust grades based on quiz performance
def adjust_grade(grade, correct):
    if grade not in GRADE_SIGNS:
        return grade  # If grade is invalid, return it as is
    index = GRADE_SIGNS.index(grade)
    if correct and index > 0:
        return GRADE_SIGNS[index - 1]  # Move up a grade
    elif not correct and index < len(GRADE_SIGNS) - 1:
        return GRADE_SIGNS[index + 1]  # Move down a grade
    return grade

#both
# Quiz function
def quiz_game():
    student_id = input("Enter Student ID to take the quiz: ").strip()
    data = read_csv()
    student = next((s for s in data if s["ID"] == student_id), None)
    
    if not student:
        print("Student not found.")
        return

    print(f"Starting quiz for {student['First Name'].title()} {student['Last Name'].title()}!")
    
    questions = {
        "History": [
            ("Which civilization built Machu Picchu?", "inca empire"),
            ("Who was the first President of the United States?", "george washington"),
            ("What year did World War II end?", "1945"),
            ("Who wrote the Declaration of Independence?", "thomas jefferson"),
            ("What was the name of the first human civilization?", "sumerians")
        ],
        "English": [
            ("What literary device is used in 'The wind whispered through the trees'?", "personification"),
            ("What is the synonym of 'happy'?", "joyful"),
            ("What is the opposite of 'brave'?", "cowardly"),
            ("Who wrote 'Romeo and Juliet'?", "william shakespeare"),
            ("Identify the poetic meter used in Shakespeare’s sonnets.", "iambic pentameter")
        ],
        "Math": [
            ("Solve for x: log₂(x) + log₂(4) = 5 (in x= form)", "x=8"),
            ("What is the derivative of x²?", "2x"),
            ("What is the integral of 2x dx?", "x^2 + c"),
            ("What is the sum of the first 50 prime numbers?", "3283"),
            ("Solve for x: 5x - 3 = 2x + 9", "x=4")
        ],
        "Science": [
            ("What is the heaviest naturally occurring element on Earth?", "uranium"),
            ("Which quantum mechanical principle states no two electrons in an atom can have the same quantum numbers?", "pauli exclusion principle"),
            ("What is the atomic number of carbon?", "6"),
            ("What is the name of the nearest star to Earth?", "proxima centauri"),
            ("What is the most abundant gas in Earth's atmosphere?", "nitrogen")
        ]
    }

    correct_answers = 0
    
    for subject, qlist in questions.items():
        print(f"\n{subject} Questions:")
        for question, correct_answer in qlist:
            user_answer = input(f"{question} ").strip().lower()
            if user_answer in SECRET_ANSWERS:
                print(SECRET_ANSWERS[user_answer])
            correct = user_answer == correct_answer
            if correct:
                correct_answers += 1
            student[subject] = adjust_grade(student[subject], correct)
            print(f"{'Correct!' if correct else 'Incorrect!'} {subject} grade adjusted to: {student[subject]}")
    
    if correct_answers == 20:  # If all questions are correct, unlock the bonus round
        print("\n Bonus Round Unlocked!")
        bonus_question = input("Bonus Question: What is the speed of light in m/s? ").strip().lower()
        if bonus_question == "299792458":
            print("Correct! Extra grade applied!")
            for subject in questions.keys():
                student[subject] = adjust_grade(student[subject], True)  # Extra grade 
        else:
            print("Incorrect! you failed")
    
    with open(CSV_FILE, "w", newline="") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print("Quiz completed! Your grades have been updated.")

#both   
def secret_quiz_game():
    student_id = input("Enter Student ID to take the secret quiz: ").strip()
    data = read_csv()  # Read student data
    student = next((s for s in data if s["ID"] == student_id), None)
    
    if not student:
        print("Student not found.")
        return

    print(f"Starting secret quiz for {student['First Name'].title()} {student['Last Name'].title()}!")

    questions = {
        "Nomie quiz": [
            ("What does CRUD stand for?", "create read update delete"),
            ("What is the time complexity of Binary Search?", "o(logn)"),
            ("How many points is the project worth?", "50"),
        ]
    }

    correct_answers = 0

    # Ask the quiz questions
    for subject, qlist in questions.items():
        print(f"\n{subject} Questions:")
        for question, correct_answer in qlist:
            user_answer = input(f"{question} ").strip().lower()
            if user_answer in SECRET_ANSWERS:
                print(SECRET_ANSWERS[user_answer])
            correct = user_answer == correct_answer.lower()
            if correct:
                correct_answers += 1
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer was: {correct_answer}")

    # If all answers are correct, set GPA to 4.0 and all grades to A+
    if correct_answers == len([q[1] for q in sum(questions.values(), [])]):  # All questions answered correctly
        print("\nAll answers are correct! GPA set to 4.0 and grades updated to A+.")
        student["GPA"] = "4.0"
        student["Grade"] = "A+"  # Assuming the student has a general grade attribute for all subjects
        # Set all subject grades to A+
        subjects = ["History", "English", "Math", "Science"]
        for subject in subjects:
            student[subject] = "A+"

    # Write updated student data back to the CSV
    with open(CSV_FILE, "w", newline="") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("Secret quiz completed and grades updated!")

#both
# Read data from CSV file
def read_csv():
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
 
#both    
# Calculate GPA based on letter grades
def calculate_gpa(grades):
    total = 0
    for grade in grades:
        if grade.upper() in GPA_SCALE:
            total += GPA_SCALE[grade.upper()]
    return round(total / len(grades), 2)

#both
# function to validate phone number
def validate_phone_number(phone):
    return phone.isdigit() and len(phone) == 10

#both
# function to validate email format
def validate_email(email):
    # Basic email validation with a regular expression
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

#both
# function to validate date of birth format
def validate_dob(dob): # 
    dob_regex = r"\d{2}/\d{2}/\d{4}"
    return re.match(dob_regex, dob) is not None

#both
def validate_grade(grade):
    return grade.upper() in GPA_SCALE

#both
# Create a new student record
def create_student():
    data = read_csv()
    student_id = str(len(data) + 101)  # Auto-generate unique ID
    first_name = input("Enter First Name: ").strip().lower()  # Convert to lowercase
    last_name = input("Enter Last Name: ").strip().lower()  # Convert to lowercase
        # Check for secret names
    full_name = f"{first_name} {last_name}"
    if full_name in SECRET_NAMES:
        print(f"{SECRET_NAMES[full_name]} ")
    grade = input("Enter Grade: ").strip().lower()  # Convert to lowercase
    
    # Validate email format
    while True:
        email = input("Enter Email: ").strip().lower()  # Convert to lowercase
        if validate_email(email):
            break
        else:
            print("Invalid email. Please enter a valid email address.")
    
    # Validate phone number
    while True:
        phone = input("Enter Phone: ").strip()
        if validate_phone_number(phone):
            break
        else:
            print("Invalid phone number. Please enter a 10-digit phone number.")
    
    # Validate date of birth
    while True:
        dob = input("Enter Date of Birth (MM/DD/YYYY): ").strip()
        if validate_dob(dob):
            break
        else:
            print("Invalid date format. Please enter in MM/DD/YYYY format.")

    # Enter address
    address = input("Enter Address: ").strip()
    
 # Enter and validate letter grades for subjects
    while True:
        history = input("Enter History Grade (A+, A, A-, B+, etc.): ").strip().upper()
        if validate_grade(history):
            break
        else:
            print("Invalid grade. Please enter a valid letter grade for History.")

    while True:
        english = input("Enter English Grade (A+, A, A-, B+, etc.): ").strip().upper()
        if validate_grade(english):
            break
        else:
            print("Invalid grade. Please enter a valid letter grade for English.")
            
    while True:
        math = input("Enter Math Grade (A+, A, A-, B+, etc.): ").strip().upper()
        if validate_grade(math):
            break
        else:
            print("Invalid grade. Please enter a valid letter grade for Math.")
    
    while True:
        science = input("Enter Science Grade (A+, A, A-, B+, etc.): ").strip().upper()
        if validate_grade(science):
            break
        else:
            print("Invalid grade. Please enter a valid letter grade for Science.")

    # Calculate GPA
    gpa = calculate_gpa([history, english, math, science])

    # Save to CSV
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, first_name, last_name, grade, email, phone, dob, address, history, english, math, science, gpa])
    print("Student added successfully.")
    print(f"students ID is: {student_id}\n")

#both        
# View all students and their IDs
def view_students():
    data = read_csv()
    if not data:
        print("No student records available.")
        return
    
    print("List of Students:")
    for idx, student in enumerate(data, start=1):
        print(f"{idx}. {student['First Name'].title()} {student['Last Name'].title()} (ID: {student['ID']})")
    
    # Ask for selection
    try:
        student_index = int(input("Select a number to view details (0 to cancel): "))
        if student_index == 0:
            print("Cancelled.")
            return
        selected_student = data[student_index - 1]
        print(f"\nDetails for {selected_student['First Name'].title()} {selected_student['Last Name'].title()}:")
        print(f"ID: {selected_student['ID']}")
        print(f"Grade: {selected_student['Grade'].title()}")
        print(f"Email: {selected_student['Email']}")
        print(f"Phone: {selected_student['Phone']}")
        print(f"Date of Birth: {selected_student['Date of Birth']}")
        print(f"Address: {selected_student['Address']}")
        print(f"History: {selected_student['History']}")
        print(f"English: {selected_student['English']}")
        print(f"Math: {selected_student['Math']}")
        print(f"Science: {selected_student['Science']}")
        print(f"GPA: {selected_student['GPA']}")
    except (ValueError, IndexError):
        print("Invalid selection. Please choose a valid number.")

#both
# Read a student record by ID
def read_student():
    student_id = input("Enter Student ID to read: ").strip()
    data = read_csv()
    for student in data:
        if student["ID"] == student_id:
            print(student)
            return
    print("Student not found.")

#both
# Update a student record
def update_student():
    student_id = input("Enter Student ID to update: ").strip()
    data = read_csv()
    
    for student in data:
        if student["ID"] == student_id:
            print("Current Data:", student)
            feature = input("Enter the feature to update (First Name, Last Name, Grade, Email, Phone, Date of Birth, Address, History, English, Math, Science, GPA, Add Class): ").strip().lower()
            
            # Handle invalid feature input
            if feature not in ['first name', 'last name', 'grade', 'email', 'phone', 'date of birth', 'address', 'history', 'english', 'math', 'science', 'gpa', 'add class']:
                print("Invalid feature.")
                return
            
            # Handle phone number validation
            if feature == "phone":
                while True:
                    new_value = input(f"Update {feature} (Current: {student['Phone']}): ").strip()
                    if validate_phone_number(new_value):
                        student["Phone"] = new_value
                        break
                    else:
                        print("Invalid phone number. Please enter a 10-digit number.")
            
            # Handle email validation
            elif feature == "email":
                while True:
                    new_value = input(f"Update {feature} (Current: {student['Email']}): ").strip().lower()
                    if validate_email(new_value):
                        student["Email"] = new_value
                        break
                    else:
                        print("Invalid email. Please enter a valid email address.")
            
            # Handle date of birth validation
            elif feature == "date of birth":
                while True:
                    new_value = input(f"Update {feature} (Current: {student['Date of Birth']}): ").strip()
                    if validate_dob(new_value):
                        student["Date of Birth"] = new_value
                        break
                    else:
                        print("Invalid date format. Use MM/DD/YYYY.")
            
            # Handle Add Class Feature
            elif feature == "add class":
                new_class = input("Enter the name of the new class (e.g., Geography, Art): ").strip().capitalize()
                
                # Prevent adding a class that already exists
                if new_class in student:
                    print(f"{new_class} class already exists for this student.")
                    return
                
                # Validate grade input
                while True:
                    new_grade = input(f"Enter the grade for {new_class} (A+, A, A-, B+, etc.): ").strip().upper()
                    if validate_grade(new_grade):
                        break
                    else:
                        print("Invalid grade. Please enter a valid letter grade.")
                
                # Add new class and grade
                student[new_class] = new_grade
                
                # Recalculate GPA
                grades = [student[key] for key in student.keys() if key not in ['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Date of Birth', 'Address', 'GPA']]
                gpa = calculate_gpa(grades)
                student['GPA'] = gpa
                
                # Write the updated data with the new class
                with open(CSV_FILE, "w", newline="") as file:
                    fieldnames = list(data[0].keys()) + [new_class] if new_class not in data[0].keys() else list(data[0].keys())
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)
                
                print(f"Class {new_class} with grade {new_grade} added successfully.")
                print(f"Updated GPA: {gpa}")
                print(f"\n{student['First Name'].title()} {student['Last Name'].title()} has been updated successfully. Feature updated: {feature.title()}")

                return
            
            # Handle normal text updates (like First Name, Last Name, etc.)
            else:
                new_value = input(f"The {feature} feature is currently {student[feature.capitalize()]}, update to: ").strip().lower()
                
                # Prevent numbers in name fields
                if feature in ["first name", "last name"] and not new_value.replace(" ", "").isalpha():
                    print("Name cannot contain numbers or special characters.")
                    return
                
                # Prevent letters in phone number
                if feature == "phone" and not new_value.isdigit():
                    print("Phone number must contain only numbers.")
                    return
                
                student[feature.capitalize()] = new_value
            
            # Write the updated data
            with open(CSV_FILE, "w", newline="") as file:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            
            print(f"\n{student['First Name'].title()} {student['Last Name'].title()} has been updated successfully. Feature updated: {feature.title()}")

            return
    
    print("Student not found.")

#both
# Delete a student record
def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    data = read_csv()
    updated_data = [student for student in data if student["ID"] != student_id]
    
    if len(data) == len(updated_data):
        print("Student not found.")
        return
    
    with open(CSV_FILE, "w", newline="") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)
    
    print("Student deleted successfully!")

#both
# Binary Search for student by ID or Full Name
def binary_search(data, target, key):
    data = sorted(data, key=lambda x: x[key])
    low, high = 0, len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid][key] == target:
            return data[mid]
        elif data[mid][key] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "Student not found"

#both
def search_student():
    data = read_csv()
    search_query = input("Enter First Name, Last Name, Full Name, Email, or Student ID to search: ").strip().lower()

    #  searching by ID using binary search
    student = binary_search(data, search_query, "ID")
    if student != "Student not found":
        print(student)
        return

    #  searching by Email using binary search
    for s in data:
        s["Email"] = s["Email"].lower()  # normalize for binary search
    student = binary_search(data, search_query, "Email")
    if student != "Student not found":
        print(student)
        return

    #  First Name or Last Name
    matches = [s for s in data if search_query == s['First Name'].lower() or search_query == s['Last Name'].lower()]

    if not matches:
        print("Student not found.")
        return

    if len(matches) == 1:
        print(matches[0])
        return

    print("Multiple students found with the same first or last name. Please provide the full name.")
    full_name_query = input("Enter Full Name (First Last): ").strip().lower()

    # Add full name field temporarily for binary search
    for s in matches:
        s["Full Name"] = f"{s['First Name'].lower()} {s['Last Name'].lower()}"

    student = binary_search(matches, full_name_query, "Full Name")
    if student != "Student not found":
        print(student)
        return

    print("Full name did not match any records.")


#both
# Sort students by chosen key
def merge_sort(data, key):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid], key)
    right = merge_sort(data[mid:], key)
    return merge(left, right, key)

#both
def merge(left, right, key):
    result = []
    while left and right:
        if left[0][key] <= right[0][key]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

#both
# Sort students by GPA instead of letter grade
def sort_students():
    data = read_csv()
    if not data:
        print("No student records found.")
        return

    key_input = input("Enter the attribute to sort by (LastName, ID, GPA): ").strip().lower()
    key_mapping = {"lastname": "Last Name", "id": "ID", "gpa": "GPA"}

    if key_input not in key_mapping:
        print("Invalid attribute. Try again.")
        return

    key = key_mapping[key_input]

    # Handle GPA as float during sorting
    if key == "GPA":
        for student in data:
            student["GPA"] = float(student["GPA"])
    
    sorted_data = merge_sort(data, key)

    print("\nSorted Students:")
    for student in sorted_data:
        print(student)


#both
# CLI Loop
def main():
    initialize_csv()
    while True:
        action = input("\nWhat would you like to do? (Create, Read, Update, Delete, View, Search, Sort, Quiz, Exit): ").strip().lower()
        if action in ["create", "c"]:
            create_student()
        elif action in ["read", "r"]:
            read_student()
        elif action in ["update", "u"]:
            update_student()
        elif action in ["delete", "d"]:
            delete_student()
        elif action in ["view", "v"]:
            view_students()
        elif action in ["search", "s"]:
            search_student()
        elif action in ["sort", "so"]:
            sort_students()
        elif action in ["quiz", "q"]:
            quiz_game()
        elif action in ["secret quiz", "sq"]:
            secret_quiz_game()
        elif action in ["exit", "e"]:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
