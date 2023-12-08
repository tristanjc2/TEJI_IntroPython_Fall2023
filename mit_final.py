# Collect information to plug into .doc template

# Date of Invoice, Invoice no. Start at 0000 and tick up.  

# Date beginning, Date Ending.

# Customers [Name, Address, Phone number, Email]

# Provide job information [Description of work, Materials, Labor [Hours, Rate, Amount], ]

# Payment due by, Payable to.


import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox

def dark_mode():
   window.config(bg= "black")
   frame.config(bg="black")

def light_mode():
   window.config(bg= "white")
   frame.config(bg="white")

def clear_item():
    qty_entry.delete(0, tkinter.END)
    qty_entry.insert(0, "1")
    material_entry.delete(0, tkinter.END)
    rate_entry.delete(0, tkinter.END)
    rate_entry.insert(0, "0.0")
    labor_entry.delete(0, tkinter.END)

invoice_list = []

def add_item():
    qty = int(qty_entry.get())
    if int(qty_entry.get()) < 0:
        tkinter.messagebox.showerror(title=None, message="Please enter a positive number.")
    else:
        material = material_entry.get()
        rate = float(rate_entry.get())
        # Add if else to rate, for negative quantity.
        if float(rate_entry.get()) < 0:
            tkinter.messagebox.showerror(title=None, message="Please enter a positive number.")
        else:
            total_materials = (qty * rate)
            invoice_item = [qty, material, rate, total_materials]
            tree.insert('',0, values=invoice_item)
            clear_item()
            
            invoice_list.append(invoice_item)

labor_list = []

def add_item_labor():
    labor = labor_entry.get()
    hours = float(hours_entry.get())
    labor_rate = float(labor_rate_entry.get())
    if float(labor_rate_entry.get()) < 0:
        tkinter.messagebox.showerror(title=None, message="Please enter a positive number.")
    else:
        if float(hours_entry.get()) < 0:
            tkinter.messagebox.showerror(title=None, message="Please enter a positive number.")
        else:
            labor_total = (hours * labor_rate)
            labor_item = [labor, hours, labor_rate, labor_total]
            tree2.insert('',0, values=labor_item)
            clear_item()
            
            labor_list.append(labor_item)


def new_invoice():
    customer_name_entry.delete(0, tkinter.END)
    phone_number_entry.delete(0, tkinter.END)
    date_of_invoice_entry.delete(0, tkinter.END)
    invoice_number_entry.delete(0, tkinter.END)
    customer_street_entry.delete(0, tkinter.END)
    city_state_zip_entry.delete(0, tkinter.END)
    work_description_entry.delete(0, tkinter.END)
    qty_entry.delete(0, tkinter.END)
    material_entry.delete(0, tkinter.END)
    rate_entry.delete(0, tkinter.END)
    invoice_list.clear() 
    labor_entry.delete(0, tkinter.END)
    hours_entry.delete(0, tkinter.END)
    labor_rate_entry.delete(0, tkinter.END)
    labor_list.clear() 
    for item in tree.get_children():
        tree.delete(item)
    for item in tree2.get_children():
        tree2.delete(item)
    


def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    date_of_invoice = date_of_invoice_entry.get()
    invoice_number = invoice_number_entry.get()
    name = customer_name_entry.get()
    street = customer_street_entry.get()
    city_state_zip = city_state_zip_entry.get()
    phone = phone_number_entry.get()
    work_description = work_description_entry.get()
    qty = qty_entry.get()
    material = material_entry.get()
    rate = float(rate_entry.get())
    subtotal = sum(item[3] for item in invoice_list)
    total_materials = subtotal
    labor = labor_entry.get()
    hours = hours_entry.get()
    labor_rate = labor_rate_entry.get()
    subtotal_labor = sum(item[3] for item in labor_list)
    labor_total = subtotal_labor
    
    
    final_subtotal = subtotal_labor + subtotal
    doc.render({"name":name, 
            "phone":phone,
            "street":street,
            "city_state_zip":city_state_zip,
            "work_description":work_description,
            "date_of_invoice":date_of_invoice,
            "invoice_number":invoice_number,
            "qty":qty,
            "material":material,
            "rate":rate,
            "total_materials":total_materials,
            "invoice_list": invoice_list,
            "subtotal":subtotal,
            "labor":labor,
            "hours":hours,
            "labor_rate":labor_rate,
            "labor_total":labor_total,
            "labor_list":labor_list,
            "subtotal_labor":subtotal_labor,
            "final_subtotal":final_subtotal,
    })
    
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")
    new_invoice()


window = tkinter.Tk()
window.title("MIT Python Final Project")

frame = tkinter.Frame(window)
frame.pack(padx=5, pady=5)


date_of_invoice_label = tkinter.Label(frame, text="Date of invoice")
date_of_invoice_label.grid(row=0, column=0)
date_of_invoice_entry = tkinter.Entry(frame)
date_of_invoice_entry.grid(row=1, column=0)

invoice_number_label = tkinter.Label(frame, text="Invoice number")
invoice_number_label.grid(row=0, column=1)
invoice_number_entry = tkinter.Entry(frame)
invoice_number_entry.grid(row=1, column=1,padx=5,pady=5)

customer_name_label = tkinter.Label(frame, text="Customer's Name")
customer_name_label.grid(row=2, column=0)
customer_name_entry = tkinter.Entry(frame)
customer_name_entry.grid(row=3, column=0)

phone_number_label = tkinter.Label(frame, text="Phone Number")
phone_number_label.grid(row=2, column=1)
phone_number_entry = tkinter.Entry(frame)
phone_number_entry.grid(row=3, column=1,padx=5,pady=5)

customer_street_label = tkinter.Label(frame, text="Customer's Street")
customer_street_label.grid(row=4, column=0)
customer_street_entry = tkinter.Entry(frame)
customer_street_entry.grid(row=5, column=0)

city_state_zip_label = tkinter.Label(frame, text='"City", "State" "Zip"')
city_state_zip_label.grid(row=4, column=1)
city_state_zip_entry = tkinter.Entry(frame)
city_state_zip_entry.grid(row=5, column=1,padx=5,pady=5)

work_description_label = tkinter.Label(frame, text='Description of work to be completed')
work_description_label.grid(row=1, column=2)
work_description_entry = tkinter.Entry(frame,width=50)
work_description_entry.grid(row=5-3, column=2, padx=5,pady=5)

qty_label = tkinter.Label(frame, text="QTY")
qty_label.grid(row=7, column=0)
qty_entry = tkinter.Entry(frame)
qty_entry.grid(row=8, column=0, padx=5, pady=5)

material_label = tkinter.Label(frame, text="Material")
material_label.grid(row=7, column=1)
material_entry = tkinter.Entry(frame,width=50)
material_entry.grid(row=8, column=1)

rate_label = tkinter.Label(frame, text="Rate")
rate_label.grid(row=7, column=2)
rate_entry = tkinter.Entry(frame)
rate_entry.grid(row=8, column=2)

add_item_button = tkinter.Button(frame, text = "Add item", command = add_item)
add_item_button.grid(row=9, column=2, pady=5)

columns = ('qty', 'Material', 'Rate', 'total_materials')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('qty', text='QTY')
tree.heading('Material', text='Material')
tree.heading('Rate', text='Rate')
tree.heading('total_materials', text="total_materials")

    
tree.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

# 

labor_label = tkinter.Label(frame, text="Labor Description")
labor_label.grid(row=7, column=3)
labor_entry = tkinter.Entry(frame,width=50)
labor_entry.grid(row=8, column=3)

hours_label = tkinter.Label(frame, text="Hours")
hours_label.grid(row=7, column=4)
hours_entry = tkinter.Entry(frame)
hours_entry.grid(row=8, column=4)

labor_rate_label = tkinter.Label(frame, text="Rate")
labor_rate_label.grid(row=7, column=5)
labor_rate_entry = tkinter.Entry(frame)
labor_rate_entry.grid(row=8, column=5)


add_item_labor_button = tkinter.Button(frame, text = "Add item", command = add_item_labor)
add_item_labor_button.grid(row=9, column=5, pady=5)

columns = ('labor', 'hours', 'labor_rate', 'total_labor')
tree2 = ttk.Treeview(frame, columns=columns, show="headings")
tree2.heading('labor', text='labor')
tree2.heading('hours', text='hours')
tree2.heading('labor_rate', text='labor_rate')
tree2.heading('total_labor', text="total_labor")

    
tree2.grid(row=6, column=3, columnspan=3, padx=5, pady=5)

ttk.Button(window, text="Dark Mode", command=dark_mode).pack(pady=10)
ttk.Button(window, text="Light Mode", command=light_mode).pack(pady=10)


save_invoice_button = tkinter.Button(frame, text="Generate Invoice", command=generate_invoice)
save_invoice_button.grid(row=10, column=2, columnspan=2, sticky="news", padx=5, pady=5)
new_invoice_button = tkinter.Button(frame, text="New Invoice", command=new_invoice)
new_invoice_button.grid(row=11, column=2, columnspan=2, sticky="news", padx=5, pady=5)

window.mainloop()

