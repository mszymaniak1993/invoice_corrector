from tkinter import *
from tkinter import messagebox
from db import Database
from grouped_functions import *

db = Database('invoice.db')

def populate_list():
    invoice_list.delete(0, END)
    for row in db.fetch():
        invoice_list.insert(END, row)

def add_item():
    if invoice_number_text.get()=='':
        messagebox.showerror("Wykryto błąd","Nie podano numeru faktury!")
        return
    db.insert(invoice_number_text.get())
    invoice_list.delete(0, END)
    invoice_list.insert(END, (invoice_number_text.get()))
    invoice_number_entry.delete(0, END)
    populate_list()

def select_invoice(event):
    global selected_invoice
    index = invoice_list.curselection()[0]
    selected_invoice = invoice_list.get(index)
    
    invoice_number_entry.delete(0, END)
    invoice_number_entry.insert(END, selected_invoice[1])

def edit_item():
    db.edit(selected_invoice[0], invoice_number_text.get())
    populate_list()

def remove_item():
    db.remove(selected_invoice[0])
    populate_list()

def start():
    window.iconify()
    preparation(login_text.get(), password_text.get())
    for invoice in db.fetch():
        id = invoice[0]
        number = invoice[1]
        create_correction_invoice(id, number, db)

#Create window object
window = Tk()

#Login
login_text = StringVar()
login_label = Label(window, text='Login', font=('bold', 14), pady=20)
login_label.grid(row=0, column=0, sticky=W)
login_entry = Entry(window, textvariable=login_text)
login_entry.grid(row=0, column=1)

#Password
password_text = StringVar()
password_label = Label(window, text='Hasło', font=('bold', 14))
password_label.grid(row=0, column=2, sticky=W)
password_entry = Entry(window, textvariable=password_text, show='*')
password_entry.grid(row=0, column=3)

#Invoice number
invoice_number_text = StringVar()
invoice_number_label = Label(window, text='Numer faktury', font=('bold', 14))
invoice_number_label.grid(row=0, column=4, sticky=W)
invoice_number_entry = Entry(window, textvariable=invoice_number_text)
invoice_number_entry.grid(row=0, column=5)

#Buttons
add_btn = Button(window, text='Dodaj', width=12, command=add_item)
add_btn.grid(row=1, column=0, pady=20)

edit_btn = Button(window, text='Edytuj', width=12, command=edit_item)
edit_btn.grid(row=1, column=1)

remove_btn = Button(window, text='Usuń', width=12, command=remove_item)
remove_btn.grid(row=1, column=2)

start_btn = Button(window, text='Start', width=12, command=start)
start_btn.grid(row=1, column=3)

#Invoice List (Listbox)
invoice_list = Listbox(window, height=8, width=50, border=1)
invoice_list.grid(row=2, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Create scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=3)

#Set scroll to listbox
invoice_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=invoice_list.yview)

#Bind select
invoice_list.bind('<<ListboxSelect>>', select_invoice)

window.title("Korektor faktur")
window.geometry("")

#Populate data
populate_list()

#Start program
window.mainloop()