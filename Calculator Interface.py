# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:36:30 2026

@author: sulin
"""
#Updated upstream:Calculator Interface.py
#Calculator interface
import tkinter as tk
from tkinter import *
from tkinter import ttk

#----------------Setting up window--------------------------------
# window
window = tk.Tk()
window.title('Scientific Calculator')
window.geometry('500x550')

# defining a grid to place frames
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight = 4)
window.columnconfigure((0, 1), weight=1)

#--------------------------Frames--------------------------------
# frames
top_frame = ttk.Frame(master = window, style = 'DisplayFrame.TFrame', width = 300, height = 200)
middle_left_frame = ttk.Frame(master = window, style = 'DisplayFrame.TFrame',  width = 140, height = 100)
middle_right_frame = ttk.Frame(master = window, style = 'DisplayFrame.TFrame',  width = 140, height = 100)
bottom_left_frame = ttk.Frame(master = window, style = 'DisplayFrame.TFrame')
bottom_right_frame = ttk.Frame(master = window, style = 'DisplayFrame.TFrame')

# frame layouts
top_frame.grid(row = 0, column=0, columnspan=2, sticky = 'nswe', padx= 10, pady = 10)
middle_left_frame.grid(row = 1, column = 0, sticky = 'nswe', padx = 5, pady = 5)
middle_right_frame.grid(row = 1, column = 1, sticky = 'nswe', padx = 5, pady = 5)
bottom_left_frame.grid(row = 2, column=0, sticky = 'nswe')
bottom_right_frame.grid(row = 2, column = 1, sticky = 'nswe')

#------------------------Defining Frame Grids-----------------------------
#top frame grid
top_frame.columnconfigure(0,weight = 1)
top_frame.rowconfigure(0, weight = 1)

#middle_left_frame grid 
middle_left_frame.columnconfigure((0,1,2),weight = 1)
middle_left_frame.rowconfigure((0,1,2), weight = 1)

#middle right frame grid
middle_right_frame.columnconfigure(0, weight = 1)
middle_right_frame.columnconfigure(1, weight = 0)
middle_right_frame.rowconfigure(0, weight = 0)
middle_right_frame.rowconfigure(1, weight = 1)

#botton left frame grid
bottom_left_frame.columnconfigure((0,1,2), weight = 1)
bottom_left_frame.rowconfigure((0,1,2,3), weight = 1)

#botton right frame grid
bottom_right_frame.columnconfigure((0,1), weight = 1)
bottom_right_frame.rowconfigure((0,1,2,3), weight = 1)

#-----------------------Styling---------------------------------
# frame style 
""".TFrame , .TButton, .TEntry, .TLabel acts as a master tempelate
changes the visual of all the widgets that belong to the category"""
style = ttk.Style()
style.configure("DisplayFrame.TFrame", background = 'white')

#button style
style.configure("ButtonStyle.TButton", padx = 10, relief = 'raised',font = ('Calibri',14 ) )

#history label style
style.configure("LabelStyle.TLabel", font = ('Calibri', 12), foreground = '#5E5D5D')
#-------------------Placing display widget--------------------------------
#display textbox
display_textbox = ttk.Entry(master = top_frame, font = ("Consolas",20), justify = "right")
display_textbox.grid(row = 0, column = 0, sticky = 'nswe')

#----------------------create button function-----------------------------
#create repeating buttons
def repeat_buttons(button_per_row, pass_list,frame):
    key_row = 0
    key_column = 0
    for char in pass_list:
        buttons = ttk.Button(master = frame,
                             style = "ButtonStyle.TButton",
                             width = 3,
                             text = char)
        buttons.grid(row = key_row, column = key_column,sticky = 'nswe')
        
        #check if a certain number of buttons have been placed in a row
        #if so, go to next row
        key_column += 1
        if key_column == button_per_row:
            key_column = 0
            key_row += 1

#---------------create button widget on frame-------------------------------
#trigonometry button, and other functions
further_functions = ['x²','√','π','arcsin','arctan','arccos','sin','tan','cos']
#call function
repeat_buttons(3,further_functions,middle_left_frame)

#numberic buttons from 1 - 9
numbers = ["radian","degrees",9,8,7,6,5,4,3,2,1,0]
repeat_buttons(3,numbers,bottom_left_frame)

#arithemtic buttons
"""
CE - deletes both display and history
Del - deletes the charater before the cursor
"""
arithmetic_functions = ['Del', 'CE',"x","÷","+","-","=",'.']
repeat_buttons(2, arithmetic_functions, bottom_right_frame)

#---------------------History widget----------------------------------------
#history label
label = ttk.Label(master = middle_right_frame,
                  style = 'LabelStyle.TLabel',
                  text = 'History')

#scrollbar
scrollbar = Scrollbar(master = middle_right_frame)

#history display
calculator_history = tk.Text(master = middle_right_frame,
                             width = 20,
                             height = 10,
                             bg = 'white',
                             yscrollcommand = scrollbar.set)
scrollbar.config(command = calculator_history.yview)

#place widgets
label.grid(row = 0, columnspan = 2, sticky = 'we')
calculator_history.grid(row = 1, sticky = 'nswe')
scrollbar.grid(row = 1, column = 1, sticky = 'ns')
#run
window.mainloop()