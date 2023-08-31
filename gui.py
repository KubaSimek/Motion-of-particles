"""
GIT for simulation of moving particles in 2D box using Tkinter

To divide the code for different sections I use //TITLE and /Subtitle
"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import tkinter as tk
import time
import webbrowser
from  tkinter import ttk
import math
from PIL import Image, ImageTk
import Main_program as mp

# //WINDOW
 
"""Initializing the window, the main canvas and displaying the bakground image"""
window1 = tk.Toplevel()
window1.title("Particles in a box")
window1.geometry("1000x560")
bg = tk.PhotoImage(file = "images/background/bg.png")
canvas1 = tk.Canvas(window1, width = 1000,height = 560)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")


# /Colours
colour_lightblue = "#E8EDF4"
colour_blue = "#afc6e9"
colour_darkblue = "#214478"
colour_grayblue = "#586b89"


# //IMAGES

# /Buttons
"""For buttons always importing two different styles.
Diferrent style is used when the mouse pointer enters the button and when it leaves."""
img_home_out = ImageTk.PhotoImage((Image.open("images/buttons/btn_home_out.png")).resize((70,70)))
img_home_in = ImageTk.PhotoImage((Image.open("images/buttons/btn_home_in.png")).resize((70,70)))

img_start_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_start_out.png"))
img_start_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_start_in.png"))

img_info_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_info_out.png"))
img_info_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_info_in.png"))

img_simulation_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_simulation_out.png"))
img_simulation_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_simulation_in.png"))

img_addparticle_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_addparticle_out.png"))
img_addparticle_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_addparticle_in.png"))

img_next_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_next_out.png"))
img_next_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_next_in.png"))


# /Backgrounds, logos and others
main_sim = ImageTk.PhotoImage(Image.open("images/frames_others/main_sim.png"))

icon = ImageTk.PhotoImage(Image.open("images/logo/icon.png"))
window1.iconphoto(False, icon)

logo1 = ImageTk.PhotoImage(Image.open("images/logo/logo1.png"))
logo2 = ImageTk.PhotoImage((Image.open("images/logo/logo1.png")).resize((222,74)))

frame1_1 = ImageTk.PhotoImage(Image.open("images/frames_others/frame1_1.png"))
frame1_2 = ImageTk.PhotoImage(Image.open("images/frames_others/frame1_2.png"))

frame2_1 = ImageTk.PhotoImage((Image.open("images/frames_others/frame1_1.png")).resize((438,312)))
frame2_2 = ImageTk.PhotoImage((Image.open("images/frames_others/frame1_1.png")).resize((438,150)))

frame3_1 = ImageTk.PhotoImage((Image.open("images/frames_others/frame1_1.png")).resize((438,700)))

info_bg = ImageTk.PhotoImage(Image.open("images/background/info_bg.png"))


# //VARIABLES

# Storage for all widgets on the canvas. When moving on the next page, all widgets make hidden and just some make visible 
all_widgets_on_canvas = [] 

circles = []

# Boolean variables that helps us to orient ourselves in which phase of particle parameter selection we are currently in
still_radius = False

point = False

box_bool = True 

still_position = False

circle = False


# //PARTICLES
"""Through the process of adding the particle we will change these variables and after selecting last variable (mass) 
it will add the particle with its properties to the set of all particles"""
var_x = 0
var_y = 0
var_vx = 0
var_vy = 0
var_r = 0
var_m = 0
num = 0


# /Input fileds

"""Tracking of the mouse pointer. When the coordinates are in the box, insert them to xy coordinates fields. 
Then scale the coordinates so they are 0-10 as they are in the animation"""

entry_x = tk.DoubleVar()
entry_y = tk.DoubleVar()

point_moving = False #point that is shown under the pointer

def motion_positon(event):
    global point_moving
    if 62 <= event.y <= 502 and 500 <= event.x <= 940:
        entry_x.set(round(((event.x - 500)/440)*10,2)) #move by 500 and than scaling by 10/440 and rounding to two digits
        entry_y.set(round(((event.y - 62)/440)*10,2)) #move by 62 and than scaling by 10/440 and rounding to two digits
    else:
        entry_x.set(0.0)
        entry_y.set(0.0)
    return

# Binding action to the box

"""When clicking on the box while choosing position, it stops/starts tracking the pointer coordinates."""
def cmd_box_click_position(event):
    global box_bool, still_position, point
    if still_position == True:
        if box_bool == True:
            canvas1.unbind('<Motion>')
            point = canvas1.create_oval(entry_x.get() * 44 + 500  - 5, entry_y.get() * 44 + 62 - 5, entry_x.get() * 44 + 500  + 5, entry_y.get() * 44 + 62 + 5, fill = "black")
            box_bool = not box_bool    
        else:
            canvas1.bind('<Motion>', motion_positon)
            canvas1.delete(point)
            box_bool = not box_bool

"""
Implementing better way to select the radius - it does not working. 

entry_radius = tk.DoubleVar()

circle = False
def motion_radius(event):
    global circle
    if 62 <= event.y <= 502 and 500 <= event.x <= 940:
        if circle != False:
            canvas1.delete(circle)
        entry_radius.set(round(math.sqrt(((((event.x - 500)/440)*10) - var_x) ** 2 + ((((event.y - 62)/440)*10) - var_y) ** 2),2)) #from pyth theorem compute the radius (same scale as the position)
        circle = canvas1.create_oval(var_x * 44 + 500  - (entry_radius.get() * 44), var_y * 44 + 62 - (entry_radius.get() * 44), var_x * 44 + 500  + (entry_radius.get() * 44), var_y * 44 + 62 + (entry_radius.get() * 44), fill = "white", outline = "black")
    else:
        entry_radius.set(0.0)
    return

canvas1.bind('<Motion>', motion_radius)

"""

input_x_coord = tk.Entry(window1, font = ("Avenir", 35, "bold"), textvariable = entry_x, width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)
input_y_coord = tk.Entry(window1, font = ("Avenir", 35, "bold"), textvariable = entry_y, width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)
input_radius = tk.Entry(window1, font = ("Avenir", 35, "bold"), textvariable = str(1), width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)
input_x_vel = tk.Entry(window1, font = ("Avenir", 35, "bold"), width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)
input_y_vel = tk.Entry(window1, font = ("Avenir", 35, "bold"), width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)
input_mass = tk.Entry(window1, font = ("Avenir", 35, "bold"), width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)


# //WIDGETS
"""Adding widgets on the canvas and choose the right position for them"""

# /Titles
text_home1 = canvas1.create_text(20,460, anchor = "nw", text = "Created by Jakub Šimek", font = ("Avenir", 25, "bold"), fill = colour_grayblue)
all_widgets_on_canvas += [text_home1]

text_start1 = canvas1.create_text(20,10, anchor = "nw", text = "Create your own\nsimulation", font = ("Avenir", 45, "bold"), fill = colour_darkblue)
text_start2 = canvas1.create_text(20,130, anchor = "nw", text = "Add particle to your simulation\nor start the simulation", font = ("Avenir", 25, "bold"), fill = colour_grayblue)
all_widgets_on_canvas += [text_start1, text_start2]

text_addparticle1 = canvas1.create_text(20,10, anchor = "nw", text = "Select the position\nof the particle", font = ("Avenir", 40, "bold"), fill = colour_darkblue)
text_addparticle2 = canvas1.create_text(20,130, anchor = "nw", text = "Click in the white box\nto select the position", font = ("Avenir", 25, "bold"), fill = colour_grayblue)
text_addparticle6 = canvas1.create_text(20,190, anchor = "nw", text = "Click one more time to reselect", font = ("Avenir", 20), fill = colour_grayblue)
text_addparticle3 = canvas1.create_text(28,227, anchor = "nw", text = "X = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
text_addparticle4 = canvas1.create_text(230,227, anchor = "nw", text = "Y = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
text_addparticle5 = canvas1.create_text(57,277, anchor = "nw", text = "(Insert numbers between 0 and 10)", font = ("Avenir", 20), fill = colour_grayblue)
all_widgets_on_canvas += [text_addparticle1, text_addparticle2, text_addparticle3, text_addparticle4, text_addparticle5]

text_radius1 = canvas1.create_text(20,10, anchor = "nw", text = "Select the radius\nof the particle", font = ("Avenir", 40, "bold"), fill = colour_darkblue)
text_radius2 = canvas1.create_text(20,130, anchor = "nw", text = "Click in the white box\nor fill in the radius", font = ("Avenir", 25, "bold"), fill = colour_grayblue)
text_radius3 = canvas1.create_text(28,227, anchor = "nw", text = "Radius = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
all_widgets_on_canvas += [text_radius1, text_radius2, text_radius3]

text_velocity1 = canvas1.create_text(20,10, anchor = "nw", text = "Select the velocity\nof the particle", font = ("Avenir", 40, "bold"), fill = colour_darkblue)
text_velocity2 = canvas1.create_text(20,130, anchor = "nw", text = "Fill in the velocity\nin each direction", font = ("Avenir", 25, "bold"), fill = colour_grayblue)
text_velocity3 = canvas1.create_text(28,227, anchor = "nw", text = "X = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
text_velocity4 = canvas1.create_text(230,227, anchor = "nw", text = "Y = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
text_velocity5 = canvas1.create_text(57,277, anchor = "nw", text = "(Insert numbers between -100 and 100)", font = ("Avenir", 20), fill = colour_grayblue)
all_widgets_on_canvas += [text_velocity1, text_velocity2, text_velocity3, text_velocity4, text_velocity5]

text_mass1 = canvas1.create_text(20,10, anchor = "nw", text = "Select the mass\nof the particle", font = ("Avenir", 40, "bold"), fill = colour_darkblue)
text_mass2 = canvas1.create_text(20,130, anchor = "nw", text = "Fill in the mass\nof the particle", font = ("Avenir", 25, "bold"), fill = colour_grayblue)
text_mass3 = canvas1.create_text(28,227, anchor = "nw", text = "Mass = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
all_widgets_on_canvas += [text_mass1, text_mass2, text_mass3]

text_simulation1 = canvas1.create_text(20,220, anchor = "nw", text = "I hope you enjoy\nthe simulation", font = ("Avenir", 40, "bold"), fill = colour_darkblue)
text_simulation2 = canvas1.create_text(20,340, anchor = "nw", text = "Run this program again\nto create another simulation ", font = ("Avenir", 25, "bold"), fill = colour_darkblue)
all_widgets_on_canvas += [text_simulation1, text_simulation2]

# /Buttons
i_btn_github_out= canvas1.create_text(20,500, anchor = "nw", text = "GitHub @KubaSimek", font = ("Avenir", 20), fill = colour_grayblue)
i_btn_github_in= canvas1.create_text(20,500, anchor = "nw", text = "GitHub @KubaSimek", font = ("Avenir", 20), fill = colour_darkblue)
all_widgets_on_canvas += [i_btn_github_in, i_btn_github_out]

i_btn_home_out = canvas1.create_image(30,459, anchor = "nw", image = img_home_out)
i_btn_home_in = canvas1.create_image(30,459, anchor = "nw", image = img_home_in)
all_widgets_on_canvas += [i_btn_home_out, i_btn_home_in]

i_btn_start_out = canvas1.create_image(0, 227, anchor = "nw", image = img_start_out)
i_btn_start_in = canvas1.create_image(0, 227, anchor = "nw", image = img_start_in)
all_widgets_on_canvas += [i_btn_start_in, i_btn_start_out]

i_btn_info_out = canvas1.create_image(0, 329, anchor = "nw", image = img_info_out)
i_btn_info_in = canvas1.create_image(0, 329, anchor = "nw", image = img_info_in)
all_widgets_on_canvas += [i_btn_info_in, i_btn_info_out]

i_btn_simulation_out = canvas1.create_image(0, 227, anchor = "nw", image = img_simulation_out)
i_btn_simulation_in = canvas1.create_image(0, 227, anchor = "nw", image = img_simulation_in)
all_widgets_on_canvas += [i_btn_simulation_in, i_btn_simulation_out]

i_btn_addparticle_out = canvas1.create_image(0, 329, anchor = "nw", image = img_addparticle_out)
i_btn_addparticle_in = canvas1.create_image(0, 329, anchor = "nw", image = img_addparticle_in)
all_widgets_on_canvas += [i_btn_addparticle_in, i_btn_addparticle_out]

i_btn_next1_out = canvas1.create_image(0, 329, anchor = "nw", image = img_next_out)
i_btn_next1_in = canvas1.create_image(0, 329, anchor = "nw", image = img_next_in)
all_widgets_on_canvas += [i_btn_next1_in, i_btn_next1_out]

i_btn_next2_out = canvas1.create_image(0, 329, anchor = "nw", image = img_next_out)
i_btn_next2_in = canvas1.create_image(0, 329, anchor = "nw", image = img_next_in)
all_widgets_on_canvas += [i_btn_next2_in, i_btn_next2_out]

i_btn_next3_out = canvas1.create_image(0, 329, anchor = "nw", image = img_next_out)
i_btn_next3_in = canvas1.create_image(0, 329, anchor = "nw", image = img_next_in)
all_widgets_on_canvas += [i_btn_next3_in, i_btn_next3_out]

i_btn_next4_out = canvas1.create_image(0, 329, anchor = "nw", image = img_next_out)
i_btn_next4_in = canvas1.create_image(0, 329, anchor = "nw", image = img_next_in)
all_widgets_on_canvas += [i_btn_next4_in, i_btn_next4_out]

# /Input fields
i_input_x_coord = canvas1.create_window(100,220, anchor = "nw", window = input_x_coord)
i_input_y_coord = canvas1.create_window(300,220, anchor = "nw", window = input_y_coord)
all_widgets_on_canvas += [i_input_x_coord, i_input_y_coord]

i_input_radius = canvas1.create_window(180,220, anchor = "nw", window = input_radius)
all_widgets_on_canvas += [i_input_radius]

i_input_x_vel = canvas1.create_window(100,220, anchor = "nw", window = input_x_vel)
i_input_y_vel = canvas1.create_window(300,220, anchor = "nw", window = input_y_vel)
all_widgets_on_canvas += [i_input_x_vel, i_input_y_vel]

i_input_mass = canvas1.create_window(180,220, anchor = "nw", window = input_mass)
all_widgets_on_canvas += [i_input_mass]

# /Logo
i_logo1 = canvas1.create_image(15,37, anchor = "nw", image = logo1)
i_logo2 = canvas1.create_image(120,456, anchor = "nw", image = logo2)
all_widgets_on_canvas += [i_logo1, i_logo2]

# /Others
"""Backgrounds and other elements on the canvas"""
i_main_sim = canvas1.create_image(500,62, anchor = "nw", image = main_sim)
all_widgets_on_canvas += [i_main_sim]

the_box = canvas1.create_rectangle(500,62,940,502, width = 4, fill = "white", outline = "black")
all_widgets_on_canvas += [the_box]

i_frame1_1 = canvas1.create_image(0, 0, anchor = "nw", image = frame1_1)
i_frame1_2 = canvas1.create_image(0, 430, anchor = "nw", image = frame1_2)
all_widgets_on_canvas += [i_frame1_1, i_frame1_2]

i_frame2_1 = canvas1.create_image(0, 0, anchor = "nw", image = frame2_1)
i_frame2_2 = canvas1.create_image(0, 430, anchor = "nw", image = frame2_2)
all_widgets_on_canvas += [i_frame2_1, i_frame2_2]

i_frame3_1 = canvas1.create_image(0, 0, anchor = "nw", image = frame3_1)
all_widgets_on_canvas += [i_frame3_1]

i_info_bg = canvas1.create_image(0, 0, anchor = "nw", image = info_bg)
all_widgets_on_canvas += [i_info_bg]


# //FUNCTIONS

"""Function that is called when opening the program or clicking on the home button"""
def main_page(event = None): #this function can be called as "event" - command for a button and also seperate
    global still_position, box_bool, num
    num = 0
    box_bool = False
    still_position = False

    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    """Make every element on the canvas hidden and then select just elements that are supposed to be visible"""
    
    for c in circles:
        canvas1.delete(c)
    
    if point != False:
        canvas1.delete(point)
    
    if circle != False:
        canvas1.delete(circle)
    
    canvas1.itemconfigure(text_home1, state = "normal")
    canvas1.tag_raise(text_home1)
    canvas1.itemconfigure(i_frame1_1, state = "normal")
    canvas1.itemconfigure(i_logo1, state = "normal")
    canvas1.tag_raise(i_logo1) #move logo in the top layer
    canvas1.itemconfigure(i_frame1_2, state = "normal")
    canvas1.itemconfigure(i_btn_start_out, state = "normal")
    canvas1.itemconfigure(i_btn_info_out, state = "normal")
    canvas1.itemconfigure(i_btn_github_out, state = "normal")
    canvas1.tag_raise(i_btn_github_out)
    canvas1.itemconfigure(i_main_sim, state = "normal")
    canvas1.tag_raise(i_main_sim)

main_page() #opening the main page when the program starts

# /Buttons commands
"""Command functions for each button"""
def cmd_start(event):
    global circles, num, var_m
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    """Make every element on the canvas hidden and then select just elements that are supposed to be visible"""

    canvas1.itemconfigure(text_start1, state = "normal")
    canvas1.tag_raise(text_start1)
    canvas1.itemconfigure(text_start2, state = "normal")
    canvas1.tag_raise(text_start2)
    canvas1.itemconfigure(i_frame1_1, state = "normal")
    canvas1.itemconfigure(i_frame1_2, state = "normal")
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo to the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(i_btn_simulation_out, state = "normal")
    canvas1.itemconfigure(i_btn_addparticle_out, state = "normal")
    canvas1.itemconfigure(the_box, state = "normal")

    # If we want to finish the process of adding the particle (var_m != 0), we add the particle to the simulation with its parametres
    if var_m != 0:
        var_m = float(input_mass.get())
        canvas1.delete(circle)
        circles.append(canvas1.create_oval(var_x * 44 + 500  - var_r * 44, var_y * 44 + 62 - var_r * 44, var_x * 44 + 500  + var_r * 44, var_y * 44 + 62 + var_r * 44, fill = "white", outline = "blue", width = 1))
        mp.add_par(var_x, 10 - var_y , var_vx, var_vy, var_r, var_m) #matplotlib is counting Y direction from the bottom so var_y has to be 10 - var_y so it is placed correctly 
    return

def cmd_info(event):
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo to the top layer
    canvas1.itemconfigure(i_info_bg, state = "normal")
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    return

def cmd_simulation(event):
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    canvas1.itemconfigure(i_logo1, state = "normal")
    canvas1.tag_raise(i_logo1) #move logo to the top layer
    canvas1.itemconfigure(i_frame3_1, state = "normal")
    canvas1.itemconfigure(the_box, state = "normal")
    canvas1.itemconfigure(text_simulation1, state = "normal")
    canvas1.tag_raise(text_simulation1)
    canvas1.itemconfigure(text_simulation2, state = "normal")
    canvas1.tag_raise(text_simulation2)
    canvas1.itemconfigure(text_home1, state = "normal")
    canvas1.tag_raise(text_home1)
    canvas1.itemconfigure(i_btn_github_out, state = "normal")
    canvas1.tag_raise(i_btn_github_out)

    #Start the animation
    mp.particles.print_par() #printing all particles just to check parametres
    mp.particles.innit_anim_on_canvas(window1)
    mp.bf.pairs_of_particles(mp.particles.par) #create pairs of particles
    mp.particles.animation(window1, save = False)
    return

def cmd_addparticle(event):
    global still_position, box_bool, circle, var_m, num
    num += 1
    circle = False
    var_m = 0

    box_bool = True
    still_position = True
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")

    canvas1.bind('<Motion>', motion_positon)
    canvas1.tag_bind(the_box,"<Button>", cmd_box_click_position)

    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo to the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(i_btn_next1_in, state = "normal")
    canvas1.itemconfigure(i_btn_next1_out, state = "normal")
    canvas1.tag_raise(i_btn_next1_out)
    canvas1.itemconfigure(i_input_x_coord, state = "normal")
    canvas1.itemconfigure(i_input_y_coord, state = "normal")
    canvas1.itemconfigure(i_frame2_1, state = "normal")
    canvas1.itemconfigure(i_frame2_2, state = "normal")
    canvas1.tag_raise(i_input_x_coord)
    canvas1.tag_raise(i_input_y_coord)
    canvas1.itemconfigure(text_addparticle1, state = "normal")
    canvas1.tag_raise(text_addparticle1)
    canvas1.itemconfigure(text_addparticle2, state = "normal")
    canvas1.tag_raise(text_addparticle2)
    canvas1.itemconfigure(text_addparticle3, state = "normal")
    canvas1.tag_raise(text_addparticle3)
    canvas1.itemconfigure(text_addparticle4, state = "normal")
    canvas1.tag_raise(text_addparticle4)
    canvas1.itemconfigure(text_addparticle5, state = "normal")
    canvas1.tag_raise(text_addparticle5)
    canvas1.itemconfigure(the_box, state = "normal")
    return

def cmd_next1(event):
    #adding xy coordinates of the particle
    global var_x, var_y, point
    var_x = float(entry_x.get())
    var_y = float(entry_y.get())

    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    
    canvas1.unbind("<Motion>")

    canvas1.delete(point)
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo to the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(i_btn_next2_in, state = "normal")
    canvas1.itemconfigure(i_btn_next2_out, state = "normal")
    canvas1.tag_raise(i_btn_next1_out)
    canvas1.itemconfigure(i_frame2_1, state = "normal")
    canvas1.itemconfigure(i_frame2_2, state = "normal")
    canvas1.itemconfigure(the_box, state = "normal")
    canvas1.itemconfigure(text_radius1, state = "normal")
    canvas1.tag_raise(text_radius1)
    canvas1.itemconfigure(text_radius2, state = "normal")
    canvas1.tag_raise(text_radius2)
    canvas1.itemconfigure(text_radius3, state = "normal")
    canvas1.tag_raise(text_radius3)
    canvas1.itemconfigure(i_input_radius, state = "normal")
    point = canvas1.create_oval(var_x * 44 + 500  - 5, var_y * 44 + 62 - 5, var_x * 44 + 500  + 5, var_y * 44 + 62 + 5, fill = "black")
    return


def cmd_next2(event):
    global still_radius, point, var_r, circle
    still_radius = False

    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
        
    var_r = float(input_radius.get())
        
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo to the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(i_btn_next3_in, state = "normal")
    canvas1.itemconfigure(i_btn_next3_out, state = "normal")
    canvas1.tag_raise(i_btn_next2_out)
    canvas1.itemconfigure(i_frame2_1, state = "normal")
    canvas1.itemconfigure(i_frame2_2, state = "normal")
    canvas1.itemconfigure(i_input_x_vel, state = "normal")
    canvas1.itemconfigure(i_input_y_vel, state = "normal")
    canvas1.tag_raise(i_input_x_vel)
    canvas1.tag_raise(i_input_y_vel)
    canvas1.itemconfigure(text_velocity1, state = "normal")
    canvas1.tag_raise(text_velocity1)
    canvas1.itemconfigure(text_velocity2, state = "normal")
    canvas1.tag_raise(text_velocity2)
    canvas1.itemconfigure(text_velocity3, state = "normal")
    canvas1.tag_raise(text_velocity3)
    canvas1.itemconfigure(text_velocity4, state = "normal")
    canvas1.tag_raise(text_velocity4)
    canvas1.itemconfigure(text_velocity5, state = "normal")
    canvas1.tag_raise(text_velocity5)
    canvas1.itemconfigure(the_box, state = "normal")
    canvas1.delete(point)
    circle = canvas1.create_oval(var_x * 44 + 500  - var_r * 44, var_y * 44 + 62 - var_r * 44, var_x * 44 + 500  + var_r * 44, var_y * 44 + 62 + var_r * 44, fill = "white", outline = "blue", width = 1)
    return

def cmd_next3(event):
    global var_vx, var_vy, var_m
    var_vx = float(input_x_vel.get())
    var_vy = float(input_y_vel.get())

    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo to the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(i_btn_next4_in, state = "normal")
    canvas1.itemconfigure(i_btn_next4_out, state = "normal")
    canvas1.tag_raise(i_btn_next4_out)
    canvas1.itemconfigure(i_frame2_1, state = "normal")
    canvas1.itemconfigure(i_frame2_2, state = "normal")
    canvas1.itemconfigure(the_box, state = "normal")
    canvas1.itemconfigure(text_mass1, state = "normal")
    canvas1.tag_raise(text_mass1)
    canvas1.itemconfigure(text_mass2, state = "normal")
    canvas1.tag_raise(text_mass2)
    canvas1.itemconfigure(text_mass3, state = "normal")
    canvas1.tag_raise(text_mass3)
    canvas1.itemconfigure(i_input_mass, state = "normal")
    canvas1.tag_raise(circle)
    var_m = 1
    return

# //BUTTONS

"""Functions that are used as commands for changing the style of the button when mouse pointer enters the button"""
# (It would be better to make just one function with argument - name of the button, but I was not able to make it work as action in self.tag_bind method)

def github_in(event):
    canvas1.itemconfigure(i_btn_github_in, state = "normal")
    canvas1.tag_raise(i_btn_github_in)
    return
    
def github_out(event):
    canvas1.itemconfigure(i_btn_github_in, state = "hidden")
    return

def home_in(event):
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.tag_raise(i_btn_home_in)
    return
    
def home_out(event):
    canvas1.itemconfigure(i_btn_home_in, state = "hidden")
    return

def start_in(event):
    canvas1.itemconfigure(i_btn_start_in, state = "normal")
    canvas1.tag_raise(i_btn_start_in)
    return
    
def start_out(event):
    canvas1.itemconfigure(i_btn_start_in, state = "hidden")
    return

def info_in(event):
    canvas1.itemconfigure(i_btn_info_in, state = "normal")
    canvas1.tag_raise(i_btn_info_in)
    return
    
def info_out(event):
    canvas1.itemconfigure(i_btn_info_in, state = "hidden")
    return

def simulation_in(event):
    canvas1.itemconfigure(i_btn_simulation_in, state = "normal")
    canvas1.tag_raise(i_btn_simulation_in)
    return
    
def simulation_out(event):
    canvas1.itemconfigure(i_btn_simulation_in, state = "hidden")
    return

def addparticle_in(event):
    canvas1.itemconfigure(i_btn_addparticle_in, state = "normal")
    canvas1.tag_raise(i_btn_addparticle_in)
    return
    
def addparticle_out(event):
    canvas1.itemconfigure(i_btn_addparticle_in, state = "hidden")
    return

def next1_in(event):
    canvas1.itemconfigure(i_btn_next1_in, state = "normal")
    canvas1.tag_raise(i_btn_next1_in)
    return
    
def next1_out(event):
    canvas1.itemconfigure(i_btn_next1_in, state = "hidden")
    return

def next2_in(event):
    canvas1.itemconfigure(i_btn_next2_in, state = "normal")
    canvas1.tag_raise(i_btn_next2_in)
    return
    
def next2_out(event):
    canvas1.itemconfigure(i_btn_next2_in, state = "hidden")
    return

def next3_in(event):
    canvas1.itemconfigure(i_btn_next3_in, state = "normal")
    canvas1.tag_raise(i_btn_next3_in)
    return
    
def next3_out(event):
    canvas1.itemconfigure(i_btn_next3_in, state = "hidden")
    return

def next4_in(event):
    canvas1.itemconfigure(i_btn_next4_in, state = "normal")
    canvas1.tag_raise(i_btn_next4_in)
    return
    
def next4_out(event):
    canvas1.itemconfigure(i_btn_next4_in, state = "hidden")
    return

"""Binding actions to these buttons"""
canvas1.tag_bind(i_btn_github_out, "<Enter>", github_in)
canvas1.tag_bind(i_btn_github_in, "<Leave>", github_out)
canvas1.tag_bind(i_btn_github_in, "<Button>", lambda e: webbrowser.open_new("https://github.com/KubaSimek"))

canvas1.tag_bind(i_btn_home_out, "<Enter>", home_in)
canvas1.tag_bind(i_btn_home_in, "<Leave>", home_out)
canvas1.tag_bind(i_btn_home_in, "<Button>", main_page)

canvas1.tag_bind(i_btn_start_out, "<Enter>", start_in)
canvas1.tag_bind(i_btn_start_in, "<Leave>", start_out)
canvas1.tag_bind(i_btn_start_in, "<Button>", cmd_start)

canvas1.tag_bind(i_btn_info_out, "<Enter>", info_in)
canvas1.tag_bind(i_btn_info_in, "<Leave>", info_out)
canvas1.tag_bind(i_btn_info_in, "<Button>", cmd_info)

canvas1.tag_bind(i_btn_simulation_out, "<Enter>", simulation_in)
canvas1.tag_bind(i_btn_simulation_in, "<Leave>", simulation_out)
canvas1.tag_bind(i_btn_simulation_in, "<Button>", cmd_simulation)

canvas1.tag_bind(i_btn_addparticle_out, "<Enter>", addparticle_in)
canvas1.tag_bind(i_btn_addparticle_in, "<Leave>", addparticle_out)
canvas1.tag_bind(i_btn_addparticle_in, "<Button>", cmd_addparticle)

canvas1.tag_bind(i_btn_next1_out, "<Enter>", next1_in)
canvas1.tag_bind(i_btn_next1_in, "<Leave>", next1_out)
canvas1.tag_bind(i_btn_next1_in, "<Button>", cmd_next1)

canvas1.tag_bind(i_btn_next2_out, "<Enter>", next2_in)
canvas1.tag_bind(i_btn_next2_in, "<Leave>", next2_out)
canvas1.tag_bind(i_btn_next2_in, "<Button>", cmd_next2)

canvas1.tag_bind(i_btn_next3_out, "<Enter>", next3_in)
canvas1.tag_bind(i_btn_next3_in, "<Leave>", next3_out)
canvas1.tag_bind(i_btn_next3_in, "<Button>", cmd_next3)

canvas1.tag_bind(i_btn_next4_out, "<Enter>", next4_in)
canvas1.tag_bind(i_btn_next4_in, "<Leave>", next4_out)
canvas1.tag_bind(i_btn_next4_in, "<Button>", cmd_start)

# /Run
canvas1.pack(fill = "both", expand = True)
window1.mainloop()