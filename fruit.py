"""Write a small Python program named fruit.py that demonstrates object oriented programming
by modifying a list.
"""
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    # code that reverses fruit_list
    print()
    fruit_list.reverse()
    print(f'Reversed list: {fruit_list}')

    # code to append "orange" to the end of fruit_list and print the list.
    fruit_list.append('orange')
    print(f'\nAdded orange to list: {fruit_list}')

    try:
        # Code to find where "apple" is located in fruit_list and insert "cherry" before "apple" 
        # in the list and print the list.
        index = fruit_list.index('apple')
        fruit_list.insert(index, 'cherry')
        print(f'\nInserted cherry: {fruit_list}')

        # code to remove "banana" from fruit_list and print the list.
        fruit_list.remove('banana')
        print(f'\nRemoved banana: {fruit_list}')

        # code to pop the last element from fruit_list and print the popped element and the list.
        last = fruit_list.pop()
        print(f'\npop {last}: {fruit_list}')


        #code to sort and print fruit_list.
        fruit_list.sort()
        print(f'\nSorted list: {fruit_list}')
    
        # Add code to clear and print fruit_list.
        fruit_list.clear()
        print(f'\nCleared list: {fruit_list}')

    except IndexError as err:
        print(type(err). __name__, err, sep=': ')


if __name__ == '__main__':
    main()