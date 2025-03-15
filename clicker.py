import tkinter as tk 
from PIL import image, ImageTk
root = tk.Tk() #tworzenie okna 

root.title("bomb clicker")
root.geometry("800x600+500+200") 
root.iconbitmap("icon.ico")
root.resizable(False, False) 

bomb = 100 
score = 00 
press_return = True 

label = tk.Label(root, text = "PRESS [ENT3R] 2 START DE G4ME", font = ("Chiller", 22)) 
label.pack() 

fuse_label = tk.Label(root, text = f"T1M3R: {str(bomb)}", font=("Chiller", 20))
fuse_label.pack() 

score_label = tk.Label(root, text = f"SC0R3: {str(score)}", font=("Chiller", 20))
score_label.pack() 

img_1 = tk.PhotoImage(file = "img_1.png").subsample(2, 2)
img_2 = tk.PhotoImage(file = "img_2.png").subsample(2, 2)
img_3 = tk.PhotoImage(file = "img_3.png").subsample(2, 2)
img_4 = tk.PhotoImage(file = "img_4.png").subsample(2, 2)

bomb_label = tk.Label(image = img_1)
bomb_label.pack() 

def update_display(): 
    pass 

def is_alive(): 
    pass 

def update_bomb(): 
    pass 

def update_score(): 
    pass 

def start(): 
    pass 

def click(): 
    pass 

click_button = tk.Button(root, text = "CL!CK M3", bg = "black", fg = "white", font = ("Chiller", 22), width = 23, command = click) 
click_button.pack()

root.mainloop() 
