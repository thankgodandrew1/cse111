"""
Write a program that computes the volume and surface area of 12 can sizes and 
computes and prints the storage efficiency of all 12 cans
"""

# import the standard math module so that math.pi can be used in this program
import math

def main():
    """
    This main function contains the name, radius, and height of the cans
    """    
    name = '#1 Picnic'
    radius = 6.83
    height = 10.16
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name}, {storage_efficiency:.1f}')

    name = '#1 Tall'
    radius = 7.78
    height = 11.91
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
    name = '#2'
    radius = 8.73
    height = 11.59
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
     
    name = '#2.5'
    radius = 10.32
    height = 11.91
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')

    name = '#3 Cylinder'
    radius = 10.79
    height = 17.78
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
    name = '#5'
    radius = 13.02
    height = 14.29
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
    name = '#6Z'
    radius = 5.40
    height = 8.89
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
    name = '8Z short'
    radius = 6.83
    height = 7.62
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
    name = '#10'
    radius = 15.72
    height = 17.78
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
    name = '#211'
    radius = 6.83
    height = 12.38
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
    name = '#300'
    radius = 7.62
    height = 11.27
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
    name = '#303'
    radius = 8.10
    height = 11.11
    vol = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = vol / surface_area
    print(f'{name} {storage_efficiency:.1f}')
    
def compute_volume(radius, height):
    """
    computes and returns the volume of all 12 cans
    """    
    vol = math.pi * (radius ** 2) * height
    return vol

def compute_surface_area(radius, height):
    """Computes and returns the surface area of all 12 cans 
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# call main function to start executing the program
main()