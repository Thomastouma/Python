from tkinter import *
import back2
import excel


# Function that takes data from the listbox and inserts it into entry windows
def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:   # when listbox is empty and pressed an indexerror is raised, we cath it here and pass it
        pass
   

# Function call from back2 where row equals all data in sql database "toumatest" TABLE book
def view_command():
    list1.delete(0, END)  # Updates the view by deleting the old and printing the new one
    for row in back2.view():
        list1.insert(END, row)


# Function call from back2
def add_command():
    back2.insert(datum_text.get(), timmar_text.get(), butiker_text.get(), miltal_text.get())
    list1.delete(0, END)  # Updates the view by deleting the old and printing the new one
    view_command()


def create_excel():
    excel.write_to_default_ws_row_col()


# Function call from back2 where sql code is run to delete from TABLE book
def delete_command():
    back2.delete(selected_tuple[0])


# Function call from back2 where sql code is run to update data in the table book from selected data in the listbox
def update_command():
    back2.update(selected_tuple[0], datum_text.get(), timmar_text.get(), butiker_text.get(), miltal_text.get())


window = Tk()

window.wm_title("Tidsrapportering Gottmix")

# Labels used in the program, packed in and placed with grid
l1 = Label(window, text="Datum", fg="white", bg="black")  # Naming it and choosing colors
l1.grid(row=0, column=0, sticky=N+S+E+W)

l2 = Label(window, text="Timmar", fg="white", bg="black")  # Naming it and choosing colors
l2.grid(row=0, column=2, sticky=N+S+E+W)

l3 = Label(window, text="Butiker", fg="white", bg="black")  # Naming it and choosing colors
l3.grid(row=1, column=0, sticky=N+S+E+W)

l4 = Label(window, text="Milersättning", fg="white", bg="black")  # Naming it and choosing colors
l4.grid(row=1, column=2, sticky=N+S+E+W)

# Entry windows used in the program to make it interactive, packed in with grid.
datum_text = StringVar()  # Enables the program to retrieve and use the user input in the entry
e1 = Entry(window, textvariable=datum_text, bg="grey")
e1.grid(row=0, column=1, sticky=N+S+E+W)  # Sticky stretches the entry window in all directions

timmar_text = StringVar()  # Enables the program to retrieve and use the user input in the entry
e2 = Entry(window, textvariable=timmar_text, bg="grey")
e2.grid(row=0, column=3, sticky=N+S+E+W)  # Sticky stretches the entry window in all directions

butiker_text = StringVar()  # Enables the program to retrieve and use the user input in the entry
e3 = Entry(window, textvariable=butiker_text, bg="grey")
e3.grid(row=1, column=1, sticky=N+S+E+W)  # Sticky stretches the entry window in all directions

miltal_text = StringVar()  # Enables the program to retrieve and use the user input in the entry
e4 = Entry(window, textvariable=miltal_text, bg="grey")
e4.grid(row=1, column=3, sticky=N+S+E+W)  # Sticky stretches the entry window in all directions


# Listbox and scrollbar configuration
list1 = Listbox(window, height=6, width=35, bg="grey")  # Creating the size of the listbox
list1.grid(row=2, column=0, rowspan=6, columnspan=2, sticky=N+S+E+W)  # Sticky stretches the listbox in all directions

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky=N+S+E+W)  # Sticky stretches the scrollbar in all directions

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Runs the function get_selected_row when you click on data in the listbox window
list1.bind('<<ListboxSelect>>', get_selected_row)

# All the buttons used for making the program interactive with the user
b1 = Button(window, text="Visa allt", width=12, command=view_command, fg="black", bg="green")
b1.grid(row=2, column=3, sticky=N+S+E+W)

b3 = Button(window, text="Lägg till", width=12, command=add_command, fg="black", bg="green")
b3.grid(row=4, column=3, sticky=N+S+E+W)

b4 = Button(window, text="Updatera dag", width=12, command=update_command, fg="black", bg="green")
b4.grid(row=5, column=3, sticky=N+S+E+W)

b5 = Button(window, text="Radera dag", width=12, command=delete_command, fg="black", bg="green")
b5.grid(row=6, column=3, sticky=N+S+E+W)

b6 = Button(window, text="Skapa Exceel", width=12, command=create_excel, fg="black", bg="green")
b6.grid(row=7, column=3, sticky=N+S+E+W)

b7 = Button(window, text="Stäng", width=12, command=window.destroy, fg="white", bg="red")
b7.grid(row=8, column=3, sticky=N+S+E+W)

window.mainloop()
