"""Author: ThankGod Andrew
   
   About: This program is as a result of CSE 111 Programming with Functions final project or as it's called LAST PROVE ASSSIGNMENT
           it's a python calculator that calculates some basic mathematical, chemistry, and physics problems. It isn't made to be 
           graphically represented, rather it's a program that runs in python tereminal....... Time taken: as a novice it took about 
           10 to 11 hours to get everything running perfectly or well and It's a program that enjoys the benefit of test functions.

    Purpose: This assignment is for students like me to improve and understand more about functions, test functions, how to call and use 
            python modules and method on programs and as well how to handle exception on programs.

    Date Completed: 12th July 2022 
    """
import emoji
import colorama 
from colorama import Fore
import math

def main():
    """Get users input, determine inputs, call, and print results of inputted value
    """   
    print(Fore.GREEN + """
                     ....Welcome....
                    .....  To   ......
                ..TeeGee's Calculator..\n""") 
    
    print("""
To calculate the perimeter of a trapezium (enter 1)
To calculate the area of a trapezium (enter 2)
To calculate the volume of a trapezium (enter 3)
To calculate the perimeter of a triangle (enter 4)
To calculate area of a triangle (enter 5)
To calculate the volume of a triangle (enter 6)
To calculate for the circumference of a circle (enter 7)
To calculate for the area of a circle (enter 8)
To calculate for the perimeter of a square (enter 9) 
To calculate for the area of a square (enter 10)
To calculate for the perimeter of a rectangle (enter 11)
To calculate for the area of a rectangle (enter 12)
To calculate the volume of a rectangle (enter 13)
To calculate the volume of a right circular cone (enter 14)
To calculate wind chill (enter 15)
To calculate for Density (enter 16)
To calculate the square root of a number(enter 17)
To convert from degree Fahrenheit  to degree Celsius (enter 18) 
To convert from degree Celsius to degree Fahrenheit  (enter 19)
To convert from degree Celsius to degree Kelvin (enter 20)
To calculate the Molarity of a substance in a volume solution (enter 21)""")


    try:
        user_choice = float
        
        # Import the datetime class from the datetime
        # module so that it can be used in this program.
        from datetime import datetime

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        while user_choice != 0:
            user_choice = int(input('\nEnter your choice of calculation (1-21) enter 0 to end the program: '))
        
            if user_choice == 1:
                base_a = float(input('\033[1;32M Enter the first base a: '))
                base_b = float(input('Enter the second base b: '))
                side_c = float(input('Enter the first side c: '))
                side_d = float(input('Enter the second side d: '))

                # call the function that computes the perimeter of a trapezium
                trapezium_solution_param = perimeter_trapezoid(base_a, base_b, side_c, side_d)
                
                # stores the result into an external file as a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the perimeter of a trapezium with the following inputed value {base_a}, {base_b}, {side_c}, {side_d} = {trapezium_solution_param}cm', file=calculator_file)
            
                print(f'Perimeter = {trapezium_solution_param}cm')
            
            elif user_choice == 2:
                a_base = float(input('Enter the first base a: '))
                b_base = float(input('Enter the second base b: '))
                height = float(input('Enter the height of the trapezium h: '))

                # call the function that computes the area of a trapezium
                area_trapezium_solution = area_trapezoid(a_base, b_base, height)
                
                # stores the result into an external file as a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the area of a trapezium with the following inputed value {a_base}, {b_base}, {height} = {area_trapezium_solution}', file=calculator_file)
            
                    # prints the results
                    print(f'Area = {area_trapezium_solution}')

            elif user_choice == 3:
                area = float(input('Enter the area of the trapezium: '))
                heigth = float(input('Enter the height of the trapezium: '))

                # call the function that computes the volume of a trapezium prism
                volume_trapezium_sol = volume_trapezoid_prism(area, heigth)
                
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the volume of a trapezium with the following inputed value {area}, {height} = {volume_trapezium_sol}', file=calculator_file)
            
                    # prints the results
                    print(f'Volume = {volume_trapezium_sol}')
                
            elif user_choice == 4:
                side_a = float(input('Enter the first side of the triangle a: '))
                base_c = float(input('Enter the base: '))
                side_b = float(input('Enter the second side of the triangle: '))

                # call to thee function that calculates the perimeter of a triangle
                perimeter_tri_sol = perimeter_triangle(side_a, base_c, side_b)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the perimeter of a triangle with the following inputed value {side_a}, {base_c}, {side_b} = {perimeter_tri_sol}', file=calculator_file)
            
                    # prints the results
                    print(f'Perimeter = {perimeter_tri_sol}')

            elif user_choice == 5:
                breath = float(input('Enter the breath of the triangle: '))
                tri_height = float(input('Eenteer the triangular height: '))

                # call to the function that calculates the area of a triangle
                area_tri_sol = area_triangle(breath, tri_height)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the area of a triangle with the following inputed values {breath}, {tri_height} = {area_tri_sol}', file=calculator_file)
            
                    # prints the results
                    print(f'Area = {area_tri_sol}')

            elif user_choice == 6: 
                vol_breath = float(input('Enter the triangle breath: '))
                vol_heigth = float(input('Enter the triangle height: '))
                length = float(input('Enter the triangle length: '))

                volume_tri_sol = volume_triangle_prism(vol_breath, vol_heigth, length)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the volume of a triangle with the following inputed values {vol_breath}, {vol_heigth}, {length} = {volume_tri_sol}', file=calculator_file)
            
                    # prints the results
                    print(f'Volume = {volume_tri_sol}')
            
            elif user_choice == 7:
                radius = float(input('Enter the radius of the circle: '))

                # call to the function that computes the circumference of a circle
                circumference_circle_sol = circumference_circle(radius)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the circumference of a circle with the radius value of {radius} = {circumference_circle_sol}', file=calculator_file)
            
                    # prints the results
                    print(f'Circumference = {circumference_circle_sol}')

            elif user_choice == 8:
                radius_a = float(input('Enter the radius of the circle: '))

                # call to the function that calculates the area of a circle
                circle_area = area_circle(radius_a)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the area of a circle with the radius value of {radius_a} = {circle_area}', file=calculator_file)
            
                    # prints the results
                    print(f'Area = {circle_area}')

            elif user_choice == 9:
                side = float(input('Enter the value of the square side: '))

                # call to the function that computes the perimeter of a square
                perimeter_square = p_square(side)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the perimeter of a square with equal sides of {side} = {perimeter_square}', file=calculator_file)
            
                    # prints the results
                    print(f'Perimeter = {perimeter_square}')

            elif user_choice == 10:
                sides = float(input('Enter the value for the square side: '))

                # call to the function that computes the area of a square
                square_area = area_square(sides)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the area of a square with equal sides of {sides} = {perimeter_square}', file=calculator_file)
            
                    # prints the results
                    print(f'Area = {square_area}')

            elif user_choice == 11:
                rect_length = float(input('Enter the length of the rectangle: '))
                width = float(input('Enter the width of the triangle: '))

                # call to the funtion that calculates the perimeter of a rectangle
                rectangle_p = p_rectangle(rect_length, width)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the perimeter of the rectangle with value length and width {rect_length}, {width} = {rectangle_p}', file=calculator_file)
            
                    # prints the results
                    print(f'Perimeter = {rectangle_p}')

            elif user_choice == 12:
                area_length = float(input('Enter the length of the rectange: '))
                area_width = float(input('Enter thee width of the rectangle: '))

                # call to the function that calculates the area of a rectangle
                rectangle_area = area_rectangle(area_length, area_width)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the area of the rectangle with value length and width: {rect_length}, {width} = {rectangle_area}', file=calculator_file)
                    
                    # prints the result
                    print(f'Area = {rectangle_area}')

            elif user_choice == 13:
                vol_length = float(input('Enter the length of the rectangle: '))
                volume_heigth  = float(input('Enter the height of the rectangle: '))
                volume_width = float(input('Enter the width of the rectangle: '))

                # call to thee function that calculates the volume of a rectangle
                rectangle_vol = vol_rectangle(vol_length, volume_heigth, volume_width)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the volume of the rectangle with value length, heigth, and width: {vol_length}, {volume_heigth}, {volume_width} = {rectangle_vol}', file=calculator_file)
                    
                    # prints the result
                    print(f'Volume = {rectangle_vol}')

            elif user_choice == 14:
                cone_radius = float(input("Enter the value of the cone's radius: "))
                cone_height = float(input("Enter the value of the cone's height: "))

                # call to the function that computes the volume of a cone
                volume_cone = cone_volume(cone_radius, cone_height)

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the volume of the right circular cone with value radius, heigth: {cone_radius}, {cone_height} = {volume_cone}', file=calculator_file)
                    
                    # prints the result
                    print(f'Volume = {volume_cone}')
                
            elif user_choice == 15:
                temp = float(input('What is the temperature? '))
                speed = float(input('Enter the speed in mph: '))
                degrees = input('\u00b0Fahrenheit or \u00b0Celcius (F/C)? ').lower()

                if degrees == 'f':
                    wind_chill = wind_chill_calculator(temp, speed)

                    print(f'At temperature {temp}\u00b0F, and wind speed {speed} mph, the windchill is {wind_chill}\u00b0F')
                    
                    # stores the solution in an external text file in place of a note
                    with open('calculator.txt', 'at') as calculator_file:
                        print(f'{current_date_and_time:%Y-%m-%d}, the temperature: {temp}, speed:{speed} = windchill {wind_chill}F', file=calculator_file)
                elif degrees == 'c':
                    convert = conversion(temp)
                    the_wind_chill = 35.74 + (0.6215 * convert) - (35.75 * (speed ** 0.16)) + (0.4275 * convert * (speed ** 0.16))
            
                    print(f'At temperature {convert}\u00b0F, and wind speed {speed} mph, the windchill is {the_wind_chill}\u00b0C')
                    
                    # stores the solution in an external text file in place of a note
                    with open('calculator.txt', 'at') as calculator_file:
                        print(f'{current_date_and_time:%Y-%m-%d}, the temperature: {temp}, speed:{speed} = windchill {the_wind_chill}C', file=calculator_file)

            elif user_choice == 16:
                print('Enter the mass and volume to calculate density: ')
                mass = float(input('m: '))
                volume = float(input('v: ')) 

                # call the function to calculate density
                calc_density = density(mass, volume)
                
                # prints result
                print(f'Density = {calc_density}g/cm^3')

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the density with mass: {mass} and volume: {volume} = {calc_density}g/cm^3', file=calculator_file)


            elif user_choice == 17:
                number = float(input('Enter the number you want to square root: '))

                # call to the function that calculates the square root of a number
                square_number = square_root(number)
                
                print(f'Square root = {square_number}')

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the square root of the number: {number} = {square_number}', file=calculator_file)
            
            elif user_choice == 18:
                print('Enter the fahrenheit degree:')
                f_temp = float(input('Enter in \u00b0Farenheiet: '))

                # call to the function that converts F to C
                c_temperature = c_conversion(f_temp)

                # prints the result
                print(f'Celcius = {c_temperature}\u00b0C')

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the fahrenheit: {f_temp} degree when converted to Celcius = {c_temperature}C', file=calculator_file)

            elif user_choice == 19:
                print('Enter the degrees in Celcius: ')
                c_temp = float(input('Enter in \u00b0Celcius: '))

                # call to the function that converts C to F
                f_temperature = conversion(c_temp)

                # prints the result
                print(f'Fahrenheit = {f_temperature}\u00b0F')

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the Celcius: {c_temp} degree when converted to Fahrenheit = {f_temperature}F', file=calculator_file)
            
            elif user_choice == 20:
                print('Enter the temperature in Celcius:')
                cel_temp = float(input('Enter in \u00b0Celsius: '))

                # call to the function that converts C to Kelvin
                cel_temperature = k_conversion(cel_temp)

                # prints the result
                print(f'Kelvin = {cel_temperature}\u00B0K')

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the Celcius: {cel_temp} degree when converted to Kelvin = {cel_temperature}K', file=calculator_file)

            elif user_choice == 21:
                print('Enter the moles of solute and the litres of solution: ')
                m = float(input('m = '))
                l = float(input('l = ')) 

                # call to the function that calculates molarity
                molarity = calc_molarity(m, l)

                # prints the result
                print(f'Molarity (M) = {molarity}mol/L')

                # stores the solution in an external text file in place of a note
                with open('calculator.txt', 'at') as calculator_file:
                    print(f'{current_date_and_time:%Y-%m-%d}, the moles of solute: {m} and the litres of solution: {l} result to Molarity = {molarity}mol/L', file=calculator_file)
            
            elif user_choice > 21 or user_choice < 0:
                print('\nOops \U0001F617 you entered a wrong value OPTION choose between option (1-21) ENTER 0 to end the program ')
    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer or float for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer or decimal for the section to input a value.")
        print("Run the program again and enter an integer or decimal" \
                " as prompted.") 

    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")                       

def area_trapezoid(a_base, b_base, heigth):
    """Defines the area of a trapezoid. Calculates the area of a trapezoid with the equation defined in this function 
    returns the area....equation A = ((a+b) / 2) * h .....where a and b is the base of the trapezoid and h is the height

    Parameter: 
        a_base, b_base: which are the bases of the trapezoid (parallel sides)
        height: the height (the pependicular distance between the  a_base and b_base)
    Returns: area
    """ 
    area = 0
    area = ((a_base + b_base) / 2 ) * heigth

    return area 

def perimeter_trapezoid(base_a, base_b, side_c, side_d):
    """Compute and returns the perimeter of a trapezium, returns 
    """        
    perimeter = base_a + base_b + side_c + side_d
    return perimeter

def volume_trapezoid_prism(area, height):
    """Computes and returns the volume of the trapezoid prism where area = area of a trapezoid, height = height between the 
    trapezium ends.

    Parameters:
        area: area of  a trapezium
        height: height between trapezium ends:
    """  
    # area = area_trapezoid()
    volume = area * height

    return volume  
    

def area_triangle(breath, height):
    """Defines the area of a triangle, calculates the area of a triangle with the equation defined in this function
    returns the area where the equation for the function is A = (b * h) / 2 where b = breath or base of the triangle, A = area
    and h = height of the triangle

    Parameters:
        breath : the base of the triangle
        height : the height of the triangle
    Returns: area
    """    
    area =  (breath * height) / 2
    
    return area

def perimeter_triangle(side_a, base_c, side_b):
    """Computes and returns the perimeter of a triangle
    """
    perimeter = side_a + base_c + side_b   

    return perimeter 

def volume_triangle_prism(breath, height, length):
    """Computes and returns the volume of  a triangular prism, 

    Parameter:
        breath: where breath is the length of the base
        height: height is the height of the triangle
        length: length is the prism length
    """    

    vol = 0.5 * breath * height * length

    return vol

def area_circle(radius):
    """Defines the area of a circle, calculates the area of a circle with the equation defined in this function
    returns the area where the equation for the function is A = pi * radius ** 2
    
    Parameters: 
        radius: the radius of a circle 
    Returns: area
    """    
    area = math.pi * (radius ** 2)
    
    return area
def circumference_circle(radius):
    """Computes and returns the perimiter or circumference of a circle

    Parameters:
        radius: the radius of the circle
    Returns c: as the  circumference
    """    
    c = 2 * (math.pi * radius) 

    return c

def area_square(sides):
    """Defines the area of a square, calculates the area of a square usin this equation A = side ** 2
    returns the area of the square.
    Parameters:
        sides: the sides of the square
    Returns area: the area of a square
    """    
    area = sides ** 2
    return area

def p_square(side):
    """Computes and returns the perimeter of a square using the formula P = 4a were a = side and P = peremeter
    Parameter:
        side: sides of a square
    Returns: perimeter
    """    
    peremeter = 4 * side

    return peremeter

def area_rectangle(length, width):
    """Defines the area of a rectangle, calculates the area using this formula A = wl 
    where l = length, w = width, and A = area of the rectangle

    Parameters:
        length: length of the rectangle
        width: width of the rectangle
    """    
    area = width * length
    return area

def p_rectangle(length, width):
    """Computes and returns the parameter of a rectangle __formula__ is P = 2(l*w) where l is length and w is the with

    Parameters:
        length: length of the rectangle
        width: width of the rectangle
    """    
    parameter = 2 * (length) + 2 * (width)

    return parameter

def vol_rectangle(length, heigth, width):
    """Computes and returns the volume of a rectangular prism 

    Parameters:
        length: length of the rectangle
        heigth: height of the rectangle
        width: width of the rectangle
    """    

    vol = (length * heigth * width)

    return vol

def cone_volume(radius, height):
    """Compute and return the volume of a right circular cone."""
    volume = math.pi * radius**2 * height / 3
    return volume

def square_root(number):
    """Calculates the square root of a number 

    Parameter:
        number: the number
    """    
    square_root = math.sqrt(number) 

    return square_root

def density(mass, volume):
    """Computes and returns density.... equatiion for density: p = m/v where p = density, m = mass, v = volume

    Parameter:
        mass
        volume
    Returns: 
        p: density
    """ 
    # calculates density     
    p = mass / volume
    return p

# this wind_chill_calculator function has in it the formula for calculating wind chill
def wind_chill_calculator(temp, speed):
    """computes the wind chill at a given time and speed

    Parameter:
        temp: temperature to determine the wind chill
        speed: speed in mph
    """    
    return 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + (0.4275 * temp * (speed ** 0.16))
    
# This function holds the convertion of celsius temperrature to Fahrenheit
def conversion(temp):
    """Converts temperature from Celsius to Fahrenheit 

    Parameter:
        temp : Temperature in Celsius
    """    
    return temp * (9/5) + 32

def c_conversion(temp):
    """Converts a temperature from degree Fahrenheit to degree Celsius

    Parameter:
        temp : temperature in Fahrenheit
    Returns: celsius
    """    
    celsius = (temp - 32) * (5/9)
    return celsius

def k_conversion(temp):
    """Converts a temperature from Celsius to Kelvin

    Parameters:
        temp: Temperature in celcius
    Returns: kelvin
    """    
    kelvin = (temp + 273.15)
    return kelvin

def calc_molarity(moles, litres):
    """To computee the measure of a chemical specie, in particular of a solute in a solution 

    Parameters:
        moles: moles of solute
        litres: litres of solution
    Returns: mole
    """  
    molarity = moles / litres
    return molarity 



# If this file was executed like this:
# > python calculator.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()