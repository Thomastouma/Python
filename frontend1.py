from tkinter import *
import back2


# Function that takes data from the listbox and inserts it into entry windows
def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
   

# Function call from back2 where row equals all data in sql database "toumatest" TABLE book
def view_command():
    list1.delete(0, END)  # Updates the wiew by deleting the old and printing the new one
    for row in back2.view():
        list1.insert(END, row)


# Function call from back2
def add_command():
    back2.insert(title_text.get(), author_text.get(), year_text.get())
    list1.delete(0, END)  # Updates the wiew by deleting the old and printing the new one
    view_command()


# Function call from back2 where sql code is run to delete from TABLE book
def delete_command():
    back2.delete(selected_tuple[0])


# Function call from back2 where sql code is run to update data in the table book from selected data in the listbox
def update_command():
    back2.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get())


window = Tk()

window.wm_title("BookStore")

# Labels used in the program, packed in and placed with grid
l1 = Label(window, text="Title", fg="blue", bg="White")  # Naming it and choosing colors
l1.grid(row=0, column=0, sticky=N+S+E+W)

l2 = Label(window, text="Author", fg="blue", bg="white")  # Naming it and choosing colors
l2.grid(row=0, column=2, sticky=N+S+E+W)

l3 = Label(window, text="Year", fg="blue", bg="white")  # Naming it and choosing colors
l3.grid(row=1, column=0, sticky=N+S+E+W)

# Entry windows used in the program to make it interactive, packed in with grid.
title_text = StringVar()  # Enables the program to retrieve and use the user input in the entry
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1, sticky=N+S+E+W)  # Sticky stretches the entry window in all directions

author_text = StringVar()  # Enables the program to retrieve and use the user input in the entry
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3, sticky=N+S+E+W)  # Sticky stretches the entry window in all directions

year_text = StringVar()  # Enables the program to retrieve and use the user input in the entry
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1, sticky=N+S+E+W)  # Sticky stretches the entry window in all directions

# Listbox and scrollbar configuration
list1 = Listbox(window, height=6, width=35)  # Creating the size of the listbox
list1.grid(row=2, column=0, rowspan=6, columnspan=2, sticky=N+S+E+W)  # Sticky stretches the listbox in all directions

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky=N+S+E+W)  # Sticky stretches the scrollbar in all directions

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Runs the function get_selected_row when you click on data in the listbox window
list1.bind('<<ListboxSelect>>', get_selected_row)

# All the buttons used for making the program interactive with the user
b1 = Button(window, text="View all", width=12, command=view_command, fg="white", bg="blue")
b1.grid(row=2, column=3, sticky=N+S+E+W)

b3 = Button(window, text="Add Book", width=12, command=add_command, fg="white", bg="blue")
b3.grid(row=4, column=3, sticky=N+S+E+W)

b4 = Button(window, text="Update Book", width=12, command=update_command, fg="white", bg="blue")
b4.grid(row=5, column=3, sticky=N+S+E+W)

b5 = Button(window, text="Delete Book", width=12, command=delete_command, fg="white", bg="blue")
b5.grid(row=6, column=3, sticky=N+S+E+W)

b6 = Button(window, text="Close", width=12, command=window.destroy, fg="black", bg="red")
b6.grid(row=7, column=3, sticky=N+S+E+W)

window.mainloop()
