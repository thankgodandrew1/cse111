#Copyright © 2020, Brigham Young University - Idaho. All rights reserved.

# Example 1

def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }

    # Add an item to the dictionary.
    students["81-298-9238"] = "Sama Patel"

    # Remove an item from the dictionary.
    students.pop("61-315-0160")

    # Get the number of items in the dictionary and print it.
    length = len(students)
    print(f"length: {length}")

    # Print the entire dictionary.
    print(students)
    print()

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students:

        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students[id]

        # Print the student's name.
        print(name)

    else:
        print("No such student")

    # To add an item to an existing dictionary, write code that follows this
    # dictionary_name[key] = value

    # To check if a key is stored in a dictionary, write code that follows this---
    # ----if key in dictionary_name:
    
    # To find a key and retrieve its corresponding value, write code that follows this------
    # ---value = dictionary_name[key]

# Call main to start this program.
if __name__ == "__main__":
    main()