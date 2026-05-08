# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:36:30 2026

@author: sulin
"""
#Updated upstream:Calculator Interface.py
#Calculator interface
import tkinter as tk
from tkinter import ttk

#----------------Setting up window--------------------------------
# window
window = tk.Tk()
window.title('Scientific Calculator')
window.geometry('450x500')

# define a grid (Row and Column weights)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight = 4)
window.columnconfigure((0, 1), weight=1)

#--------------------------Frames--------------------------------

# frame style 
""".TFrame , .TButton, .TEntry, .TLabel acts as a master tempelate
changes the visual of all the widgets that belong to the category"""
style = ttk.Style()
style.configure("DisplayFrame.TFrame", background = '#d7dcd9')

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
bottom_left_frame.grid(row = 2, column=0, sticky = 'nswe', padx = 3)
bottom_right_frame.grid(row = 2, column = 1, sticky = 'nswe', padx = 3)

#------------------------Frame Grids-----------------------------------
#top frame grid
top_frame.columnconfigure(0,weight = 1)
top_frame.rowconfigure(0, weight = 1)

#middle_left_frame grid 
middle_left_frame.columnconfigure((0,1,2),weight = 1)
middle_left_frame.rowconfigure((0,1,2), weight = 1)

#middle right frame grid
middle_right_frame.columnconfigure(0, weight = 1)
middle_right_frame.rowconfigure(0, weight = 1)

#botton left frame
bottom_left_frame.columnconfigure((0,1,2), weight = 1)
bottom_left_frame.rowconfigure((0,1,2,3), weight = 1)

#botton right frame
bottom_right_frame.columnconfigure((0,1), weight = 1)
bottom_right_frame.rowconfigure((0,1,2,3), weight = 1)


window.mainloop()