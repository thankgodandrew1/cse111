import csv
from tkinter import Y
"""A local grocery store subscribes to an online service that enables its customers to order groceries online.
 After a customer completes an order, the online service sends a CSV file that contains the customer's requests 
 to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal 
 window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.
"""

def main():
    """Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
       Prints the products_dict.
       Opens the request.csv file for reading.
       Contains a loop that reads and processes each row from the request.csv file. Within the body of the loop,
       your program must do the following for each row:
       Use the requested product number to find the corresponding ite
       m in the products_dict.
       Print the product name, requested quantity, and product price.

    """   
    #Indexes

    try:
        PRODUCTS_NUMBER_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2

        # Calls the read_dict function and stores the compound dictionary in a variable named products_dict.
        products_dict = read_dict('products.csv', PRODUCTS_NUMBER_INDEX)

        # Prints the products_dict. 
        # print('All Product:')   
        # print(products_dict)

        #Indexes for innerlist in the request.csv file
        REQUESTED_PRODUCT_NUMBER = 0
        REQUESTED_PRODUCT_QUANTITY = 1

    
        with open('request.csv', 'rt') as request_file:
      
            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(request_file)
    
            # skip the first linne of text
            next(reader)
            # prints the name of the store
            print('Inkom Emporium\n')
        
            print('\nRequested Items')
            prod_total = 0
            subtotal = 0
            # A loop that reads and processes each row from the request.csv file.
            for product, quantity in reader:

                # Use the requested product number to find the corresponding item in the products_dict.
                product_num = products_dict[product] 
            
                #Retrieves the product name, quantity and price for the products number in the products dictionary
                name = product_num[NAME_INDEX]
                item_quantity = quantity
                price = product_num[PRICE_INDEX]

                # Print the product name, requested quantity, and product price.
                print(f'{name}: {item_quantity} @ {price}')
            
               # sums the number of ordered items
                prod_total += int(item_quantity)

                # sum the subtotal due
                subtotal += float(price) * int(quantity)
            
                # compute the sales tax amount using 6% as the sales tax
                tax = (6/100) * subtotal

                # Compute and print the total amount due.
                total_amount = subtotal + tax
            
            print(f"\nNumber of Items: {prod_total}")
            print(f'Subtotal: {subtotal:.2f}')
            print(f'Sales Tax: {tax:.2f}')
            print(f'Total: {total_amount:.2f}')
        
            # Print a thank you message.
            print('\nThank You for shopping at the Inkom Emporium.')
        
            # Import the datetime class from the datetime
            # module so that it can be used in this program.
            from datetime import datetime
 
           # Call the now() method to get the current
           # date and time as a datetime object from
           # the computer's operating system.
            current_date_and_time = datetime.now()

            day_of_week = current_date_and_time.weekday()


            # Print the current day of the week and the current time.
            print(f"{current_date_and_time:%A %b %d %H:%M:%S %Y }")
            
            #Write code to discount the product prices by 10% if today is Tuesday or Wednesday.
             
            if (day_of_week == 1):
                discount = (10/100) * total_amount
                
                print(f'\nBecause today is Tuesday you have a discount of: {discount:.2f}')
            
            elif (day_of_week == 2):
                discount = (10/100) * total_amount
                
                print(f'\nBecause today is Wednesday you have a discount of: {discount:.2f}')
 
    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print('Error: missing file')
        print(type(not_found_err).__name__, not_found_err, sep=": ")

    except KeyError as key_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print('Error: unknown product ID in the request.csv file')
        print(type(key_err).__name__, key_err, sep=": ")
            
    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.  
        print()
        print(type(perm_err).__name__, perm_err, sep=': ')
        print(f"You don't have permission to read this file")
        print('Run the program again and enter \
             the name of the file you are allowed to read')
 

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
    products_dict = {}

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
                products_dict[key] = row_list
        return products_dict

if __name__ == '__main__':
    main()