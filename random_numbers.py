import random

def main():

    numbers = [16.2, 75.1, 52.3]
    
    # Prints the numbers list
    print(f"The numbers list are: {numbers} ")

    # Calls the append_random_numbers function 
    # with only one argument to add one number to numbers
    # Prints the numbers list
    append_random_numbers(numbers)
    print(f'numbers {numbers}')
    
    
    # Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    # Prints the numbers list
    append_random_numbers(numbers, 3)
    print(f'numbers {numbers}')


 
def append_random_numbers(numbers_list, quantity=1):
    """Has two parameters: a list named numbers_list and an integer named quantity.
    The parameter quantity has a default value of 1
    Computes quantity pseudo random numbers by calling the random.uniform function.
    Rounds the quantity pseudo random numbers to one digit after the decimal.
    Appends the quantity pseudo random numbers onto the end of the numbers_list.

    Parameters: number_list, quantity
    """    
    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number)
        numbers_list.append(rounded)
        
if __name__ == '__main__':
    main()