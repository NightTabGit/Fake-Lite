import os
import time
import tkinter
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
    
def vape():
    ## Setup code...
    width = 914 # Width of window.
    height = 606 # Height of window.
    root = tkinter.Tk() # Name.
    root.overrideredirect(True) # Get rid off standard window (By Windows OS) declaring independancy.
    w, h = int(width), int(height) # Heigher, Width.
    canvas = tkinter.Canvas(root, width=w, height=h, highlightthickness=0) # Start canvas (Hidden borders).
    filename = PhotoImage(file = "Picture.png") # Set background.
    image = canvas.create_image(int(width), 0, anchor=NE, image=filename,) # Set in middle.
    canvas.pack(fill='both')
    root.eval('tk::PlaceWindow . center') # Window in center of screen.
    if isinstance(root, Tk): # Determine when packed.
        master = root  # Root window.
    else:
        master = root.master
    ## Drag window code...
    x, y = 0, 0
    def mouse_motion(event): # Drag event.
        global x, y
        offset_x, offset_y = event.x - x, event.y - y  
        new_x = master.winfo_x() + offset_x
        new_y = master.winfo_y() + offset_y
        new_geometry = f"+{new_x}+{new_y}"
        master.geometry(new_geometry)

    def mouse_press(event): # Detect mouse press.
        global x, y
        count = time.time()
        x, y = event.x, event.y

    root.bind("<B1-Motion>", mouse_motion) # Bind down + up.
    root.bind("<Button-1>", mouse_press)

    def destroy(): # Destroy window.
        root.destroy()

    def minimize(): # Hide (Temporary) window.
        root.state('withdrawn')
        time.sleep(0.2) # Wait 2 seconds before showing again (Make it seem glitched).
        root.state('normal')
    ## Button code...
    exit_btn= PhotoImage(file='Exit.png') # Exit button.
    img_label= Label(image=exit_btn)
    button = Button(root, image=exit_btn,command= destroy, borderwidth=0, highlightthickness=0, relief = FLAT,activebackground = "#19191b")
    button.pack(pady=30)
    button.place(x=870, y=3) # X + Y co-ords.
    button.lift()

    click_btn= PhotoImage(file='Minimize.png') # Minimize button.
    img_label2= Label(image=click_btn)
    button = Button(root, image=click_btn,command= minimize, borderwidth=0, highlightthickness=0, relief = FLAT,activebackground = "#19191b")
    button.pack(pady=30)
    button.place(x=845, y=4) # X + Y co-ords.
    button.lift()

    def fade_in():
        Alpha = 0.0
        root.attributes("-alpha", Alpha)
        while 1.0 > Alpha :
            Alpha = Alpha + 0.04
            root.attributes("-alpha", Alpha)
            time.sleep(0.005)
        
    ## Launch code...
    root.attributes('-topmost', True) # Window always ontop.
    Alpha = 0
    root.attributes("-alpha", Alpha)
    root.after(800, fade_in)
    root.mainloop() # Start loop.

print("No Minecraft found...")
vape()
