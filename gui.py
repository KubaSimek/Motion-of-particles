import tkinter as tk
import time
from  tkinter import ttk
from PIL import Image, ImageTk
from functools import partial


# Window 
"""Initializing the window, the main canvas and displaying the bakground image"""
window1 = tk.Tk()
window1.title("window")
window1.geometry("1000x560")
bg = tk.PhotoImage(file = "images/background/bg.png")
canvas1 = tk.Canvas(window1, width = 1000,height = 560)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

# Colours
colour_lightblue = '#40E0D0'
colour_blue = "#D7E1F4"
colour_darkblue = "#214478"


# IMAGES

# Buttons
"For buttons always importing two different styles." 
"Diferrent style is used when the mouse pointer enters the button and when it leaves."
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

# Backgrounds, logos and others
logo1 = ImageTk.PhotoImage(Image.open("images/logo/logo1.png"))
logo2 = ImageTk.PhotoImage((Image.open("images/logo/logo1.png")).resize((222,74)))

frame1_1 = ImageTk.PhotoImage(Image.open("images/frames_others/frame1_1.png"))
frame1_2 = ImageTk.PhotoImage(Image.open("images/frames_others/frame1_2.png"))

info_bg = ImageTk.PhotoImage(Image.open("images/background/info_bg.png"))

# Input fileds
input_x_coord = tk.Entry(window1, font = ("Helvetica", 35), width = 5, bd = 0, bg = colour_blue, fg = colour_darkblue)
input_y_coord = tk.Entry(window1, font = ("Helvetica", 35), width = 5, bd = 0, bg = colour_blue, fg = colour_darkblue)


# VARIABLES

# Storage for all widgets on the canvas. When moving on the next page, all widgets make hidden and just some make visible 
all_widgets_on_canvas = [] 

# WIDGETS
"Adding widgets on the canvas and choose the right position for them" 

# Buttons
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

# Input fields
i_input_x_coord = canvas1.create_window(300,220, anchor = "nw", window = input_x_coord)
i_input_y_coord = canvas1.create_window(300,320, anchor = "nw", window = input_y_coord)
all_widgets_on_canvas += [i_input_x_coord, i_input_y_coord]

# Logo
i_logo1 = canvas1.create_image(15,37, anchor = "nw", image = logo1)
i_logo2 = canvas1.create_image(120,456, anchor = "nw", image = logo2)
all_widgets_on_canvas += [i_logo1, i_logo2]

# Others
"Backgrounds and other elements on the canvas"
i_frame1_1 = canvas1.create_image(0, 0, anchor = "nw", image = frame1_1)
i_frame1_2 = canvas1.create_image(0, 430, anchor = "nw", image = frame1_2)
all_widgets_on_canvas += [i_frame1_1, i_frame1_2]

i_info_bg = canvas1.create_image(0, 0, anchor = "nw", image = info_bg)
all_widgets_on_canvas += [i_info_bg]


# FUNCTIONS

"Function that is called when opening the program or clicking on the home button"
def main_page(event = None):
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    canvas1.itemconfigure(i_frame1_1, state = "normal")
    canvas1.itemconfigure(i_logo1, state = "normal")
    canvas1.tag_raise(i_logo1) #move logo in the top layer
    canvas1.itemconfigure(i_frame1_2, state = "normal")
    canvas1.itemconfigure(i_btn_start_out, state = "normal")
    canvas1.itemconfigure(i_btn_info_out, state = "normal")
    

main_page()

# Buttons commands
"Command for each button"
def cmd_start(event):
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    canvas1.itemconfigure(i_frame1_1, state = "normal")
    canvas1.itemconfigure(i_frame1_2, state = "normal")
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo in the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(i_btn_simulation_out, state = "normal")
    canvas1.itemconfigure(i_btn_addparticle_out, state = "normal")
    return

def cmd_info(event):
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo in the top layer
    canvas1.itemconfigure(i_info_bg, state = "normal")
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    return

def cmd_simulation(event):
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo in the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    return

def cmd_addparticle(event):
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo in the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(i_input_x_coord, state = "normal")
    canvas1.itemconfigure(i_input_y_coord, state = "normal")
    canvas1.tag_raise(i_input_x_coord)
    canvas1.tag_raise(i_input_y_coord)
    return


# BUTTONS

"Functions that are used as commands for changing the style of the button when mouse pointer enters the button"
def home_in(event):
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.tag_raise(i_btn_home_in)
    return
    
def home_out(event):
    canvas1.itemconfigure(i_btn_home_in, state = "hidden")
    return

def start_in(event):
    canvas1.itemconfigure(i_btn_start_in, state = "normal")
    return
    
def start_out(event):
    canvas1.itemconfigure(i_btn_start_in, state = "hidden")
    return

def info_in(event):
    canvas1.itemconfigure(i_btn_info_in, state = "normal")
    return
    
def info_out(event):
    canvas1.itemconfigure(i_btn_info_in, state = "hidden")
    return

def simulation_in(event):
    canvas1.itemconfigure(i_btn_simulation_in, state = "normal")
    return
    
def simulation_out(event):
    canvas1.itemconfigure(i_btn_simulation_in, state = "hidden")
    return

def addparticle_in(event):
    canvas1.itemconfigure(i_btn_addparticle_in, state = "normal")
    return
    
def addparticle_out(event):
    canvas1.itemconfigure(i_btn_addparticle_in, state = "hidden")
    return


"Binding actions to these buttons"
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


# Run
canvas1.pack(fill = "both", expand = True)
window1.mainloop()