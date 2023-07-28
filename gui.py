import tkinter as tk
import time
from  tkinter import ttk
from PIL import Image, ImageTk
from functools import partial


# Window
window1 = tk.Tk()
window1.title("window")
window1.geometry("1000x560")
bg = tk.PhotoImage(file = "images/background/bg.png")
canvas1 = tk.Canvas(window1, width = 1000,height = 560)


# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

# Images
img_start_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_start_out.png"))
img_start_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_start_in.png"))

img_info_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_info_out.png"))
img_info_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_info_in.png"))

img_simulation_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_simulation_out.png"))
img_simulation_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_simulation_in.png"))

img_addparticle_out = ImageTk.PhotoImage(Image.open("images/buttons/btn_addparticle_out.png"))
img_addparticle_in = ImageTk.PhotoImage(Image.open("images/buttons/btn_addparticle_in.png"))

frame1_1 = ImageTk.PhotoImage(Image.open("images/frames_others/frame1_1.png"))
frame1_2 = ImageTk.PhotoImage(Image.open("images/frames_others/frame1_2.png"))

# Buttons commands

def cmd_start(event):
    canvas1.delete(i_btn_start_out)
    canvas1.delete(i_btn_info_out)
    canvas1.delete(i_btn_start_in)
    canvas1.delete(i_btn_info_in)
    canvas1.itemconfigure(i_btn_simulation_out, state = "normal")
    canvas1.itemconfigure(i_btn_addparticle_out, state = "normal")

    return

def cmd_info(event):
    canvas1.delete(i_btn_start_out)
    canvas1.delete(i_btn_info_out)
    canvas1.delete(i_btn_start_in)
    canvas1.delete(i_btn_info_in)
    return

def cmd_simulation(event):
    pass

def cmd_addparticle(event):
    pass

# Titles

# Buttons - in/out functions
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

i_btn_start_out = canvas1.create_image(0, 227, anchor = "nw", image = img_start_out)
i_btn_start_in = canvas1.create_image(0, 227, anchor = "nw", image = img_start_in)
canvas1.itemconfigure(i_btn_start_in, state = "hidden")
canvas1.tag_bind(i_btn_start_out, "<Enter>", start_in)
canvas1.tag_bind(i_btn_start_in, "<Leave>", start_out)
canvas1.tag_bind(i_btn_start_in, "<Button>", cmd_start)

i_btn_info_out = canvas1.create_image(0, 329, anchor = "nw", image = img_info_out)
i_btn_info_in = canvas1.create_image(0, 329, anchor = "nw", image = img_info_in)
canvas1.itemconfigure(i_btn_info_in, state = "hidden")
canvas1.tag_bind(i_btn_info_out, "<Enter>", info_in)
canvas1.tag_bind(i_btn_info_in, "<Leave>", info_out)
canvas1.tag_bind(i_btn_info_in, "<Button>", cmd_info)

i_btn_simulation_out = canvas1.create_image(0, 227, anchor = "nw", image = img_simulation_out)
i_btn_simulation_in = canvas1.create_image(0, 227, anchor = "nw", image = img_simulation_in)
canvas1.itemconfigure(i_btn_simulation_out, state = "hidden")
canvas1.itemconfigure(i_btn_simulation_in, state = "hidden")
canvas1.tag_bind(i_btn_simulation_out, "<Enter>", simulation_in)
canvas1.tag_bind(i_btn_simulation_in, "<Leave>", simulation_out)
canvas1.tag_bind(i_btn_simulation_in, "<Button>", cmd_simulation)

i_btn_addparticle_out = canvas1.create_image(0, 329, anchor = "nw", image = img_addparticle_out)
i_btn_addparticle_in = canvas1.create_image(0, 329, anchor = "nw", image = img_addparticle_in)
canvas1.itemconfigure(i_btn_addparticle_out, state = "hidden")
canvas1.itemconfigure(i_btn_addparticle_in, state = "hidden")
canvas1.tag_bind(i_btn_addparticle_out, "<Enter>", addparticle_in)
canvas1.tag_bind(i_btn_addparticle_in, "<Leave>", addparticle_out)
canvas1.tag_bind(i_btn_addparticle_in, "<Button>", cmd_addparticle)

# Others
i_frame1_1 = canvas1.create_image(0, 0, anchor = "nw", image = frame1_1)
i_frame1_2 = canvas1.create_image(0, 430, anchor = "nw", image = frame1_2)

#window_start


#run
canvas1.pack(fill = "both", expand = True)
window1.mainloop()