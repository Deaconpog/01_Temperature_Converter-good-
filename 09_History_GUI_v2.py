""" Builds on 09_History_GUI_v1
Hard coded list (generated in v1) added this version at lines 18-24
Not much use. Appends these 7 items to any others added.
"""

from tkinter import *
from functools import partial  # To prevent unwanted additional windows
import random


class Converter:
    def __init__(self):
        # Formatting variables
        background_color = "light blue"

        # Initialise list to hold calculation history
        # In later versions list will be populated with user calculations
        self.all_calculations = ['0 degrees F is -17.8 degrees C',
                                 '0 degrees C is 32 degrees F',
                                 '40 degrees C is 104 degrees F',
                                 '40 degrees F is 4.4 degrees C',
                                 '12 degrees C is 53.6 degrees F',
                                 '24 degrees C is 75.2 degrees F',
                                 '100 degrees F is 37.8 degrees C']

        # Converter frame
        self.converter_frame = Frame(bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 19 bold",
                                        bg=background_color,
                                        pady=10, padx=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons "
                                                  "below...",
                                             font="Arial 10 italic", wrap=290,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        # Celsius temperature conversion
        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="Khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        # Fahrenheit temperature conversion
        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame,
                                       font="Arial 12 bold",
                                       text="Calculation history",
                                       width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"  # Pale pink background for when error screen appears

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check amount is valid and convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert,
                                                               fahrenheit)
                self.to_convert_entry.configure(bg="white")

            # Check amount is valid and convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert,
                                                               celsius)
                self.to_convert_entry.configure(bg="white")

            # If input is invalid (e.g. too low)
            else:
                answer = "Too cold"
                self.to_convert_entry.configure(bg=error)
                has_errors = "Yes"

            # Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.converted_label.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.converted_label.configure(bg=error)

            if answer != "Too cold":
                self.all_calculations.append(answer)
                print(self.all_calculations)


        except ValueError:
            self.converted_label.configure(text="Please enter a number",
                                           fg="red")
            self.to_convert_entry.configure(bg=error)

    # Rounding
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        return rounded


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Title goes here")
    something = Converter()
    root.mainloop()
