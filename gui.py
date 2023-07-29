import tkinter as tk
import time
from  tkinter import ttk
from PIL import Image, ImageTk
from functools import partial


# Window 
"""Initializing the window, the main canvas and displaying the bakground image"""
window1 = tk.Tk()
window1.title("Particles in a box")
window1.geometry("1000x560")
bg = tk.PhotoImage(file = "images/background/bg.png")
canvas1 = tk.Canvas(window1, width = 1000,height = 560)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

# Colours
colour_lightblue = '#E8EDF4'
colour_blue = "#afc6e9"
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

img_next_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_next_out.png"))
img_next_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_next_in.png"))


# Backgrounds, logos and others
icon = ImageTk.PhotoImage(Image.open("images/logo/icon.png"))
window1.iconphoto(False, icon)

logo1 = ImageTk.PhotoImage(Image.open("images/logo/logo1.png"))
logo2 = ImageTk.PhotoImage((Image.open("images/logo/logo1.png")).resize((222,74)))

frame1_1 = ImageTk.PhotoImage(Image.open("images/frames_others/frame1_1.png"))
frame1_2 = ImageTk.PhotoImage(Image.open("images/frames_others/frame1_2.png"))

frame2_1 = ImageTk.PhotoImage((Image.open("images/frames_others/frame1_1.png")).resize((438,312)))
frame2_2 = ImageTk.PhotoImage((Image.open("images/frames_others/frame1_1.png")).resize((438,150)))
frame2_3 = ImageTk.PhotoImage((Image.open("images/frames_others/frame1_1.png")).resize((222,1)))

info_bg = ImageTk.PhotoImage(Image.open("images/background/info_bg.png"))

# Input fileds

"Tracking of the mouse pointer. When the coordinates are in the box, insert them to xy coordinates fields." 
"Then scale the coordinates so they are 0-10 as they are in the animation"

entry_x = tk.DoubleVar()
entry_y = tk.DoubleVar()

def motion(event):
    if 62 <= event.y <= 502 and 500 <= event.x <= 940:
        entry_x.set(round(((event.x - 500)/440)*10,2)) #move by 500 and than scaling by 10/440 and rounding to two digits
        entry_y.set(round(((event.y - 62)/440)*10,2)) #move by 62 and than scaling by 10/440 and rounding to two digits
    else:
        entry_x.set(0.0)
        entry_y.set(0.0)
    return

canvas1.bind('<Motion>', motion)

entry_radius = tk.DoubleVar()

input_x_coord = tk.Entry(window1, font = ("Avenir", 35, "bold"), textvariable = entry_x, width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)
input_y_coord = tk.Entry(window1, font = ("Avenir", 35, "bold"), textvariable = entry_y, width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)
input_radius = tk.Entry(window1, font = ("Avenir", 35, "bold"), textvariable = entry_radius, width = 5, borderwidth=0, highlightbackground = colour_blue, bg = colour_lightblue, fg = colour_darkblue)


# VARIABLES

# Storage for all widgets on the canvas. When moving on the next page, all widgets make hidden and just some make visible 
all_widgets_on_canvas = [] 

still_position = False

point = False

# PARTICLES
#Properties of the particle that we are adding
var_x = 0
var_y = 0
var_vx = 0
var_vy = 0
var_r = 0
var_d = 0
var_m = 0

# WIDGETS
"Adding widgets on the canvas and choose the right position for them" 

# Titles
text_addparticle1 = canvas1.create_text(20,10, anchor = "nw", text = "Select the position\nof the particle", font = ("Avenir", 40, "bold"), fill = colour_darkblue)
text_addparticle2 = canvas1.create_text(20,120, anchor = "nw", text = "Click in the white box\nor fill in the x and y coordinates", font = ("Avenir", 25, "bold"), fill = colour_lightblue)
text_addparticle6 = canvas1.create_text(20,190, anchor = "nw", text = "Click one more time to reselect", font = ("Avenir", 20), fill = colour_lightblue)
text_addparticle3 = canvas1.create_text(28,227, anchor = "nw", text = "X = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
text_addparticle4 = canvas1.create_text(230,227, anchor = "nw", text = "Y = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
text_addparticle5 = canvas1.create_text(57,277, anchor = "nw", text = "(Insert numbers between 0 and 10)", font = ("Avenir", 20), fill = colour_lightblue)
all_widgets_on_canvas += [text_addparticle1, text_addparticle2, text_addparticle3, text_addparticle4, text_addparticle5, text_addparticle6]

text_radius1 = canvas1.create_text(20,10, anchor = "nw", text = "Select the radius\nof the particle", font = ("Avenir", 40, "bold"), fill = colour_darkblue)
text_radius2 = canvas1.create_text(20,120, anchor = "nw", text = "Click in the white box\nor fill in the radius.", font = ("Avenir", 25, "bold"), fill = colour_lightblue)
text_radius3 = canvas1.create_text(28,227, anchor = "nw", text = "Radius = ", font = ("Avenir", 35, "bold"), fill = colour_darkblue)
all_widgets_on_canvas += [text_radius1, text_radius2, text_radius3]

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

i_btn_next1_out = canvas1.create_image(0, 329, anchor = "nw", image = img_next_out)
i_btn_next1_in = canvas1.create_image(0, 329, anchor = "nw", image = img_next_in)
all_widgets_on_canvas += [i_btn_next1_in, i_btn_next1_out]

i_btn_next2_out = canvas1.create_image(0, 329, anchor = "nw", image = img_next_out)
i_btn_next2_in = canvas1.create_image(0, 329, anchor = "nw", image = img_next_in)
all_widgets_on_canvas += [i_btn_next2_in, i_btn_next2_out]

# Input fields
i_input_x_coord = canvas1.create_window(100,220, anchor = "nw", window = input_x_coord)
i_input_y_coord = canvas1.create_window(300,220, anchor = "nw", window = input_y_coord)
all_widgets_on_canvas += [i_input_x_coord, i_input_y_coord]

i_input_radius = canvas1.create_window(180,220, anchor = "nw", window = input_radius)
all_widgets_on_canvas += [i_input_radius]

# Logo
i_logo1 = canvas1.create_image(15,37, anchor = "nw", image = logo1)
i_logo2 = canvas1.create_image(120,456, anchor = "nw", image = logo2)
all_widgets_on_canvas += [i_logo1, i_logo2]

# Others
"Backgrounds and other elements on the canvas"
the_box = canvas1.create_rectangle(500,62,940,502, width = 4, fill = "white", outline = "black")
all_widgets_on_canvas += [the_box]

i_frame1_1 = canvas1.create_image(0, 0, anchor = "nw", image = frame1_1)
i_frame1_2 = canvas1.create_image(0, 430, anchor = "nw", image = frame1_2)
all_widgets_on_canvas += [i_frame1_1, i_frame1_2]

i_frame2_1 = canvas1.create_image(0, 0, anchor = "nw", image = frame2_1)
i_frame2_2 = canvas1.create_image(0, 430, anchor = "nw", image = frame2_2)
all_widgets_on_canvas += [i_frame2_1, i_frame2_2]

i_info_bg = canvas1.create_image(0, 0, anchor = "nw", image = info_bg)
all_widgets_on_canvas += [i_info_bg]


# FUNCTIONS

"Function that is called when opening the program or clicking on the home button"
def main_page(event = None):
    #particles.destroy_particles()
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
    if point != False:
        canvas1.delete(point)
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
    canvas1.tag_raise(i_logo2) #move logo to the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(i_btn_simulation_out, state = "normal")
    canvas1.itemconfigure(i_btn_addparticle_out, state = "normal")
    canvas1.itemconfigure(the_box, state = "normal")
    canvas1.tag_raise(the_box)
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
    canvas1.itemconfigure(i_logo2, state = "normal")
    canvas1.tag_raise(i_logo2) #move logo to the top layer
    canvas1.itemconfigure(i_btn_home_in, state = "normal")
    canvas1.itemconfigure(i_btn_home_out, state = "normal")
    canvas1.tag_raise(i_btn_home_out)
    canvas1.itemconfigure(the_box, state = "normal")
    canvas1.tag_raise(the_box)
    return

def cmd_addparticle(event):
    global still_position
    still_position = True
    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
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
    canvas1.itemconfigure(text_addparticle6, state = "normal")
    canvas1.tag_raise(text_addparticle6)
    canvas1.itemconfigure(the_box, state = "normal")
    canvas1.tag_raise(the_box)
    return

def cmd_next1(event):
    global still_position
    still_position = False
    #adding xy coordinates of the particle
    global var_x, var_y
    var_x = entry_x.get()
    var_y = entry_y.get()
    print(var_x * 44 + 500  - 5, var_y * 44 + 62 - 5)

    for p in all_widgets_on_canvas:
        canvas1.itemconfigure(p, state = "hidden")
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
    canvas1.tag_raise(the_box)
    canvas1.itemconfigure(text_radius1, state = "normal")
    canvas1.tag_raise(text_radius1)
    canvas1.itemconfigure(text_radius2, state = "normal")
    canvas1.tag_raise(text_radius2)
    canvas1.itemconfigure(text_radius3, state = "normal")
    canvas1.tag_raise(text_radius3)
    canvas1.itemconfigure(i_input_radius, state = "normal")
    canvas1.create_oval(var_x * 44 + 500  - 5, var_y * 44 + 62 - 5, var_x * 44 + 500  + 5, var_y * 44 + 62 + 5, fill = "black")
    return

def cmd_next2(event):
    pass


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

canvas1.tag_bind(i_btn_next1_out, "<Enter>", next1_in)
canvas1.tag_bind(i_btn_next1_in, "<Leave>", next1_out)
canvas1.tag_bind(i_btn_next1_in, "<Button>", cmd_next1)

canvas1.tag_bind(i_btn_next2_out, "<Enter>", next2_in)
canvas1.tag_bind(i_btn_next2_in, "<Leave>", next2_out)
canvas1.tag_bind(i_btn_next2_in, "<Button>", cmd_next2)

# binding action to the box
"When clicking on the box while choosing position, is stops/start to track the pointer coordinates."
box_bool = True #if the tracking of the pointer is currently active or not
def cmd_box_click(event):
    global box_bool, still_position, point
    if still_position == False:
        return
    elif box_bool == True:
        canvas1.unbind('<Motion>')
        point = canvas1.create_oval((entry_x.get()) * 44 + 500  - 5, (entry_y.get()) * 44 + 62 - 5, (entry_x.get()) * 44 + 500  + 5, (entry_y.get()) * 44 + 62 + 5, fill = "black")
        box_bool = not box_bool    
    else:
        canvas1.bind('<Motion>', motion)
        canvas1.delete(point)
        box_bool = not box_bool


canvas1.tag_bind(the_box,"<Button>", cmd_box_click)

# Run
canvas1.pack(fill = "both", expand = True)
window1.mainloop()