import csv

def main():
    """Open the students.csv file for reading, skip the first
       line of text in the file because it contains only
       headings, and read the other lines of the file into a dictionary.
       The program must store each student I-Number as a key and each 
       name as a value in the dictionary.
    """    

    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    # Read the contents of the students.csv file
    # into a compound list.
    students_dict = read_dict('students.csv', I_NUMBER_INDEX)
    
    # Get an I-Number from thr user
    inumber = input("Please enter an I-Number (xx-xxx-xxxx): ")

    # The I-Numbers are stored in the CSV file as digits only (without
    # any dashes), so we remove all dashes from the user's input.
    inumber = inumber.replace("-", "")

    # Determine if the user input is formatted correctly.
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if inumber not in students_dict:
                print("No such student")
            else:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                value = students_dict[inumber]
                name = value[NAME_INDEX]

                # Print the student name.
                print(name)

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # skip the first linne of text
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                key = row_list[key_column_index]
                
                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list
    return dictionary
if __name__ == "__main__":
    main()