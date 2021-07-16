from tkinter import *
from backend import Database

database = Database("deals.db")

class Window():
    def __init__(self,window):
        self.window = window
        self.window.wm_title("Deals Completed")
        # labels
        l1 = Label(window,text = 'Name')
        l1.grid(row = 0, column = 0)

        l2 = Label(window,text = 'Email')
        l2.grid(row = 1, column = 0)

        l3 = Label(window,text = 'Country')
        l3.grid(row = 2, column = 0)

        l4 = Label(window,text = 'Product')
        l4.grid(row = 3, column = 0)

        l5 = Label(window,text = 'Sales Amount')
        l5.grid(row = 4, column = 0)

        l6 = Label(window,text = 'Phone')
        l6.grid(row = 5, column = 0)

        l7 = Label(window,text = 'Date')
        l7.grid(row = 6, column = 0)

        # Entries
        self.name_entry = StringVar()
        self.e1 = Entry(window, textvariable = self.name_entry) 
        self.e1.grid(row = 0, column = 1)

        self.email_entry = StringVar()
        self.e2 = Entry(window, textvariable = self.email_entry)
        self.e2.grid(row = 1, column = 1)

        self.country_entry = StringVar()
        self.e3 = Entry(window, textvariable = self.country_entry)
        self.e3.grid(row = 2, column = 1)

        self.product_entry= StringVar()
        self.e4 = Entry(window, textvariable = self.product_entry)
        self.e4.grid(row = 3, column = 1)

        self.sales_amount_entry = StringVar()
        self.e5 = Entry(window, textvariable = self.sales_amount_entry)
        self.e5.grid(row = 4, column = 1)

        self.phone_entry = StringVar()
        self.e6 = Entry(window, textvariable = self.phone_entry)
        self.e6.grid(row = 5, column = 1)

        self.date_entry = StringVar()
        self.e7 = Entry(window, textvariable = self.date_entry)
        self.e7.grid(row = 6, column = 1)

        #listbox and scrollbar
        self.listbox = Listbox(window, height = 20, width = 30)
        self.listbox.grid(row = 0, rowspan = 6, column = 2, columnspan = 2)
        self.scroll = Scrollbar(window, orient = VERTICAL)
        self.scroll.grid(row = 0, rowspan = 6, column = 4)
        #link scrollbar with the listbox
        self.scroll.config(command = self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        self.listbox.bind('<<ListboxSelect>>',self.get_selected_row)

        #bottons
        b1 = Button(window, text = "View all", width = 12, command = self.view_command)
        b1.grid(row = 7, column = 2)

        b2 = Button(window, text = "Search", width = 12, command = self.search_command)
        b2.grid(row = 7, column = 3)

        b3 = Button(window, text = "Add Entry", width = 12, command = self.add_command)
        b3.grid(row = 7, column = 4)

        b4 = Button(window, text = "Update selected", width = 12, command = self.update_command)
        b4.grid(row = 8, column = 2)

        b5 = Button(window, text = "Delete selected", width = 12, command = self.delete_command)
        b5.grid(row = 8, column = 3)

        b6 = Button(window, text = "Close", width = 12, command = window.destroy)
        b6.grid(row = 8, column = 4)

    #for bind method of listbox
    def get_selected_row(self,event):
        index = self.listbox.curselection()[0]
        self.selected_tuple = self.listbox.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4])
        self.e5.delete(0,END)
        self.e5.insert(END,self.selected_tuple[5])
        self.e6.delete(0,END)
        self.e6.insert(END,self.selected_tuple[6])
        self.e7.delete(0,END)
        self.e7.insert(END,self.selected_tuple[7])
    
    #wrapper functions
    def view_command(self):
        #first, empty the listbox
        self.listbox.delete(0,END)
        for row in database.view():
            self.listbox.insert(END,row)

    def search_command(self):
        self.listbox.delete(0,END)
        for row in database.search(self.name_entry.get(),self.email_entry.get(),self.country_entry.get(), self.product_entry.get(), self.sales_amount_entry.get(), self.phone_entry.get(), self.date_entry.get()):
            self.listbox.insert(END, row)

    def add_command(self):
        database.add(self.name_entry.get(),self.email_entry.get(),self.country_entry.get(), self.product_entry.get(), self.sales_amount_entry.get(), self.phone_entry.get(), self.date_entry.get())
        self.listbox.delete(0,END)
        self.listbox.insert(END,(self.name_entry.get(),self.email_entry.get(),self.country_entry.get(), self.product_entry.get(), self.sales_amount_entry.get(), self.phone_entry.get(), self.date_entry.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        

    def update_command(self):
        database.update(self.name_entry.get(),
            self.email_entry.get(),self.country_entry.get(), 
            self.product_entry.get(), 
            self.sales_amount_entry.get(), self.phone_entry.get(), self.date_entry.get())




window = Tk()
Window(window)
window.mainloop()
