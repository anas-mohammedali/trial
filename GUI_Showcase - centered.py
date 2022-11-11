#Dropdown Menu fuer Benutzeroberflaeche
import tkinter as tk
from tkinter import *
import cv2


#import Auswertung_Showcase as showcase


#GUI-label
titel = "Berührungs-/Grifferkennung"
#Dropdown-Elements
dropdown = ["Tasse", "Computermaus", "Handtasche", "Rucksack", "Flasche"]
#Startbutton
start = "Greiferkennung starten"
#Stopbutton
stop = "Greiferkennung stoppen"
#text to be displayed
info = "Wählen Sie etwas aus dem Dropdown-Menü aus >>>"

#Function to be called when the button is pressed

def bla():
     print("ola")

def bla_bla():
     print("HaHa")

#Creating the GUI window
window = tk.Tk()
window.title(titel)
window.configure (background = "black") 

#Set the window size
window.geometry("900x400")

#background image
bgimg= tk.PhotoImage(file = "bg2.png")

#Specify the file name present in the same directory or else
#specify the proper path for retrieving the image to set it as background image.
limg= Label(window, i=bgimg)
limg.place(x=0, y=0, relwidth =1, relheight = 1)

# Create dropdown menu and set initial value
dropdown.sort()
variable = tk.StringVar(window)
variable.set(dropdown[0])
dropdown = tk.OptionMenu(window, variable, *dropdown)
dropdown.config(bg = "#23395d", fg= "White")
dropdown["menu"].config( bg="#23395d", fg= "White")


#dropdown.place(x = 400, y = 45)


#Insertion of a start button --> call of associated function when activated
start_button = tk.Button(window, text = start, foreground = "white", background = "#23395d", command = bla)
#start_button.place(x = 150 , y = 120)
#start_button.pack()

#Insertion of a stop button --> call of associated function when activated
stop_button = tk.Button(window, text = stop, foreground = "white", background = "#23395d", command  = bla_bla)
#stop_button.place(x = 300, y = 120)
#stop_button.pack()

#Code for the text_box
label = tk.Label(window, text = info, font = ('none', 10, "italic", "bold"), foreground = "white", background = "#020202") 
#label.place(x = 50, y = 50)

# Specify Grid
Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)
Grid.rowconfigure(window,3,weight=1)
Grid.rowconfigure(window,4,weight=1)
Grid.rowconfigure(window,5,weight=1)
Grid.rowconfigure(window,6,weight=1)
Grid.columnconfigure(window,0,weight=1)
Grid.columnconfigure(window,1,weight=1)
Grid.columnconfigure(window,2,weight=1)
Grid.columnconfigure(window,3,weight=1)
Grid.columnconfigure(window,4,weight=1)
Grid.columnconfigure(window,5,weight=1)
Grid.columnconfigure(window,6,weight=1)
Grid.columnconfigure(window,7,weight=1)
Grid.columnconfigure(window,8,weight=1)
Grid.columnconfigure(window,9,weight=1)

#creating grid to enable resizability
label.grid(row=1,column = 1, columnspan = 8, sticky="NSEW")
dropdown.grid(row=3, column = 3, columnspan = 4, sticky="NSEW", padx = 20,pady = 20)
start_button.grid(row=5,column=1, columnspan = 3, sticky="NSEW")
stop_button.grid(row=5,column=6, columnspan = 3, sticky="NSEW")




# drop = OptionMenu(window)
# drop.pack()

window.mainloop()


