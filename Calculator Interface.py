# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:36:30 2026

@author: sulin
"""
# Updated upstream:Calculator Interface.py
# Calculator interface
import tkinter as tk
from tkinter import *
from tkinter import ttk

# ----------------Setting up window--------------------------------
# window
class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Scientific Calculator')
        self.geometry('500x550')
        
        self.is_dark_mode = False
        
        #widgets
        self.main_grid()
        self.frame()
        self.display_widget()
        self.create_buttons()
        self.calculator_history()

    def main_grid(self):
        # defining a grid to place frames
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=4)
        self.columnconfigure((0, 1), weight=1)
# --------------------------Frames--------------------------------
    # frames
    def frame(self):
       self.top_frame = ttk.Frame(master=self, style='DisplayFrame.TFrame', width=300, height=200)
       self.middle_left_frame = ttk.Frame(master=self, style='DisplayFrame.TFrame', width=140, height=100)
       self.middle_right_frame = ttk.Frame(master=self, style='DisplayFrame.TFrame', width=140, height=100)
       self.bottom_left_frame = ttk.Frame(master=self, style='DisplayFrame.TFrame')
       self.bottom_right_frame = ttk.Frame(master=self, style='DisplayFrame.TFrame')

       # frame layouts
       self.top_frame.grid(row=0, column=0, columnspan=2, sticky='nswe', padx=10, pady=10)
       self.middle_left_frame.grid(row=1, column=0, sticky='nswe', padx=5, pady=5)
       self.middle_right_frame.grid(row=1, column=1, sticky='nswe', padx=5, pady=5)
       self.bottom_left_frame.grid(row=2, column=0, sticky='nswe')
       self.bottom_right_frame.grid(row=2, column=1, sticky='nswe')

       # ------------------------Defining Frame Grids-----------------------------
       self.top_frame.columnconfigure(0, weight=1)
       self.top_frame.rowconfigure(0, weight=1)

       # middle_left_frame grid
       self.middle_left_frame.columnconfigure((0, 1, 2), weight=1)
       self.middle_left_frame.rowconfigure((0, 1, 2, 3), weight=1)

       # middle right frame grid
       self.middle_right_frame.columnconfigure(0, weight=1)
       self.middle_right_frame.columnconfigure(1, weight=0)
       self.middle_right_frame.rowconfigure(0, weight=0)
       self.middle_right_frame.rowconfigure(1, weight=1)

       # botton left frame grid
       self.bottom_left_frame.columnconfigure((0, 1, 2), weight=1)
       self.bottom_left_frame.rowconfigure((0, 1, 2, 3), weight=1)

       # botton right frame grid
       self.bottom_right_frame.columnconfigure((0, 1), weight=1)
       self.bottom_right_frame.rowconfigure((0, 1, 2, 3), weight=1)
# -----------------------Styling---------------------------------
    # frame style
    def styling(self):
        """.TFrame , .TButton, .TEntry, .TLabel acts as a master tempelate
        changes the visual of all the widgets that belong to the category"""
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure("DisplayFrame.TFrame", background='#F9F9F9')

        # button style
        self.style.configure("NumericButton.TButton", padding=10, relief='flat', background='#FFFFFF', font=('Segoe UI', 14))
        self.style.configure("FunctionButton.TButton", padding=10, relief='flat', background='#E0E0E0', font=('Calibri', 14))
        self.style.configure("EqualButton.TButton", padding=10, relief='flat', background='#6BB1BA', font=('Calibri', 14))
        
        # history label style
        self.style.configure("LabelStyle.TLabel", font=('Calibri', 12), foreground='#5E5D5D')

        # button effects ; style.map(function,properties)
        self.style.map("NumericButton.TButton", background=[('active', '#EAEAEA')],relief = 'flat')
        self.style.map("FunctionButton.TButton", background=[('active', '#D4D4D4')],relief = 'flat')
        self.style.map("EqualButton.TButton", background=[('active', '#5A9AA3')],relief = 'flat')
    
# -------------------Placing display widget--------------------------------
    def display_widget(self):
        # display textbox
        self.display_textbox = ttk.Entry(master=self.top_frame, font=("Consolas", 20), justify="right")
        self.display_textbox.grid(row=0, column=0, sticky='nswe')
# ----------------------create button function-----------------------------
    # create repeating buttons
    def repeat_buttons(self,button_per_row, pass_list, frame, style_name):
        key_row = 0
        key_column = 0
        for char in pass_list:
            buttons = ttk.Button(master=frame,
                                 style=style_name,
                                 width=3,
                                 text=char)
            buttons.grid(row=key_row, column=key_column, sticky='nswe', padx=2, pady=2)

            # check if a certain number of buttons have been placed in a row
            # if so, go to next row
            key_column += 1
            if key_column == button_per_row:
                key_column = 0
                key_row += 1
# ---------------create button widget on frame-------------------------------
    def create_buttons(self):
        self.styling()
        # trigonometry button, and other functions
        further_functions = ['x²', '√', 'π', 'arcsin', 'arctan', 'arccos', 'sin', 'tan', 'cos', "radian", "log()", "ln"]
        # call function
        self.repeat_buttons(3, further_functions, self.middle_left_frame, 'FunctionButton.TButton')

        # numberic buttons from 1 - 9
        numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "(", ")"]
        self.repeat_buttons(3, numbers, self.bottom_left_frame, 'NumericButton.TButton')

        # arithemtic buttons
        """
        CE - deletes both display and history
        Del - deletes the charater before the cursor
        """
        arithmetic_functions = ['Del', 'CE', "x", "÷", "+", "-", "."]
        self.repeat_buttons(2, arithmetic_functions, self.bottom_right_frame, 'FunctionButton.TButton')

        equal_button = ttk.Button(master=self.bottom_right_frame,
                                  style='EqualButton.TButton',
                                  width=3,
                                  text='=')
        equal_button.grid(row=3, column=1, sticky='nswe')

# ---------------------History widget----------------------------------------
    def calculator_history(self):
        # history label
        self.label = ttk.Label(master= self.middle_right_frame,
                          style='LabelStyle.TLabel',
                          text='History')
        # scrollbar
        self.scrollbar = Scrollbar(master= self.middle_right_frame)

        # history display
        self.calculator_history_widget = tk.Text(master= self.middle_right_frame,
                                     width=20,
                                     height=10,
                                     bg='white',
                                     yscrollcommand= self.scrollbar.set)
        self.scrollbar.config(command= self.calculator_history_widget.yview)

        # place widgets
        self.label.grid(row=0, columnspan = 2, sticky='we')
        self.calculator_history_widget.grid(row=1, sticky='nswe')
        self.scrollbar.grid(row=1, column=1, sticky='ns')

#main
if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()