# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    draw_vertical_gradient, start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
#Import the random from random module to generate random circles that would fit for a cloud
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_cloud(canvas, scene_width, scene_height, 200)
    draw_tree(canvas, 620, 100, 300)
    draw_grass(canvas, scene_width, scene_height)
    
    # draw_grid(canvas, scene_width, scene_height, 50)


    """_summary_
    """    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height ):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 5,
        scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 5, width=  0, fill="tan4")

def draw_cloud(canvas, width, height, interval):

    
    min_diameter = 20
    max_diameter = 70

    #use for loop to generate random ovals to make cloud
    
    for i in range(1, 16):
        x = random.randint(-40, 40 )
        y = random.randint(-30, 30)
        diameter = random.randint(min_diameter, max_diameter)
        
        for x in range(x, height, interval):
            draw_oval(canvas, 230+x, 440+ y, x + 150, y + 370, outline="white", fill="white")
        
def draw_tree(canvas, center_x, bottom, height):
# draw the tree trunk
    trunk_width = height / 8
    trunk_height = height / 6
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill= 'khaki4')

# draw the shirt of the tree
    draw_oval(canvas, 720, 145, 520, 350, outline = "paleGreen3", fill='ForestGreen') 
 
def draw_grass(canvas, width, height, ):
    
    for i in range(2):
        draw_line(canvas, 800, 60, 0, 50, width=110, fill="limegreen")

# def draw_grid(canvas, width, height, interval):
#     # draw a vertical line
#     label_y = 15                    
#     for x in range(interval, width, interval):
#         draw_line(canvas, x, 0, x, height )
#         draw_text(canvas, x, label_y, f'{x}')
    
#     label_x = 15
#     for y in range(interval, height, interval):        
#         draw_line(canvas, 0, y, width, y)
#         draw_text(canvas, label_x, y, f'{y}')



# Call the main function so that
# this program will start executing.
main()
