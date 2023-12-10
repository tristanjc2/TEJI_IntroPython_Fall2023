
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title("BMI Calculator")

window.geometry('900x900')

def calculate():
    global bmi
    name = name_entry.get()
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = float(weight) / float(height) ** 2 * 703
    tkinter.messagebox.showinfo(title="BMI Calculations", message="Your BMI is {:.1f} - {}".format(bmi, name))
    if bmi <= 18.5:
        print("you are underweight")
    elif bmi > 18.5 or bmi <= 24.9:
        print("you are normal weight")
    elif bmi > 24.9 or bmi <= 29.9:
        print("you are overweight")
    else:
        print("you are obese")
    


name_label = tkinter.Label(window, text="Enter your name here: ")
name_label.grid(row=0, column=0)
name_entry = tkinter.Entry(window)
name_entry.grid(row=0, column=1,padx=5,pady=5)

height_label = tkinter.Label(window, text="Enter your height here: ")
height_label.grid(row=1, column=0)
height_entry = tkinter.Entry(window)
height_entry.grid(row=1, column=1,padx=5,pady=5)

# height = float(height_entry.get())

weight_label = tkinter.Label(window, text="Enter your weight here: ")
weight_label.grid(row=2, column=0)
weight_entry = tkinter.Entry(window)
weight_entry.grid(row=2, column=1,padx=5,pady=5)

# weight = float(weight_entry.get())

ttk.Button(window, text="Calculate BMI", command=calculate).grid(row=3, column=1, padx=5, pady=5)


# Do some while loop down here
# Add a way to display different options.
# Allow user to choose what they'd like to do.

# Change the label text 
def show(): 
    label.config( text = choices[0] )
    if clicked.get() == "Underweight":
        print(choices[0])

choices = [
    "If you're underweight you have two options, eat or eat.",
    "If you're normal weight etc."
]

# Dropdown menu options 
options = [ 
    "Underweight", 
    "Tuesday", 
    "Wednesdaya", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"
] 
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "BMI outcomes." ) 
  
# Create Dropdown menu 
drop = OptionMenu( window , clicked , *options ) 
drop.grid(row=6,column=1) 
  
# Create button, it will change label text 
button = Button( window , text = " " , command = show ).grid(row=7,column=1) 
  
# Create Label 
label = Label( window , text = " " ) 
label.grid(row=8,column=1)  

class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data
lst = [((), "BMI", "Weight Status"),
       (1,'Less than 18.5','Underweight',19),
       (2,'between 18.5 and 24.9','Normal Weight',18),
       (3,'between 24.9 and 29.9','Underweight',20),
       (4,'Over 30','Obese',21)]
 
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
 
# create root window

t = Table(window)


window.mainloop()

"""
from tkinter import *
 
 
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data
lst = [((), "BMI", "Weight Status"),
       (1,'Less than 18.5','Underweight',19),
       (2,'between 18.5 and 24.9','Normal Weight',18),
       (3,'between 24.9 and 29.9','Underweight',20),
       (4,'Over 30','Obese',21)]
 
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
 
# create root window
root = Tk()
t = Table(root)
root.mainloop()
"""