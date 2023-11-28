from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import databasedesign
import mysql.connector

connect = mysql.connector.connect(host='localhost', user= 'root', password= 'admin', database= 'for_login')



# DEFINE THE FORM FOR REGISTRATION FORM
def registration_form():
    

    def hover_open(event):
        Register.config(bg='blue',fg='white', relief=SOLID)
    
    def hover_close(event):
        Register.config(bg='#1877F2', fg='white', relief=FLAT)
    # FUNCTIONALITY FOR REGISTRATION BUTTON
    def registration_save():
        mycursor = connect.cursor()
        user = name.get()
        password = Password.get()
        number_entry = Number.get()  # Changed to lowercase
        

        # Check if user and password are entered
        myquery = "INSERT INTO for_signup (id, num, u_name, l_name, m_name, g_name, pass) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (id.get(),number_entry, user, last_name_entry.get(), middle_initial_entry.get(), given_name_entry.get(), password )
    #===================================================================PUNTA SA SIGNUP===================================================================================
        try:
            # Execute the query with parameter values
            mycursor.execute(myquery, data)
            connect.commit()  # Commit the transaction to save changes
            messagebox.showinfo("Registered", "Successfully Registered your account")
            root.destroy()  # Close only the registration form window
            databasedesign.database()  # Call the init function from the login form
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to insert data: {err}")
            name.delete(0, END)
            last_name_entry.delete(0, END)
            given_name_entry.delete(0, END)
            middle_initial_entry.delete(0, END)
            Number.delete(0, END)
            Password.delete(0, END)
            id.delete(0, END)

    # FORM FOR REGISTRATION FORM
    root = Tk() 
    root.geometry("500x500")
    bgimage = Image.open('FOR REG.jpg')
    bg_photo = ImageTk.PhotoImage(bgimage)
    for_label_bg = Label(root, image=bg_photo)
    for_label_bg.place(relheight=1, relwidth=1) 
    root.title("Sign-up")

    # Create a frame for the registration form
    registration = LabelFrame(root, text="Sign-up", font=("Helvetica", 18, 'bold'), border=0, bg='#333333', fg='white')
    registration.place(relx=0.5, rely=0.5, anchor=CENTER)
    

    # CREATE LABELS IN DB
    id_label = Label(registration, text="User ID:", bg='#333333', fg='white')
    id_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    name_label = Label(registration, text="Number:", bg='#333333', fg='white')
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    
    number_label = Label(registration, text="User Name:", bg='#333333', fg='white')
    number_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    
    last_name_label = Label(registration, text="Last Name:", bg='#333333', fg='white')
    last_name_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    
    given_name_label = Label(registration, text="Given Name:", bg='#333333', fg='white')
    given_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    
    middle_initial_label = Label(registration, text="Middle Initial:", bg='#333333', fg='white')
    middle_initial_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    
    password_label = Label(registration, text="Password:", bg='#333333', fg='white')
    password_label.grid(row=6, column=0, padx=10, pady=10, sticky=W)

    # CREATE ENTRY FOR DB
    id = Entry(registration)
    id.grid(row=0, column=1, sticky=W)

    Number = Entry(registration)
    Number.grid(row=1, column=1, sticky=W)
    
    
    name = Entry(registration)
    name.grid(row=2, column=1, sticky=W)
    
    last_name_entry = Entry(registration)
    last_name_entry.grid(row=3, column=1,sticky=W)
    
    given_name_entry = Entry(registration)
    given_name_entry.grid(row=4, column=1, sticky=W)
    
    middle_initial_entry = Entry(registration)
    middle_initial_entry.grid(row=5, column=1, sticky=W)
    
    Password = Entry(registration, show='*')
    Password.grid(row=6, column=1, sticky=W)

    # CREATE BUTTON FOR REGISTRATION
    Register = Button(registration, text="Register", command=registration_save, bg='#1877F2', borderwidth=0, relief=FLAT, padx=100, cursor="hand2", fg='white', activebackground='#1877F2', activeforeground='white')
    Register.bind("<Enter>", hover_open)
    Register.bind("<Leave>", hover_close)
    Register.grid(row=7, column=0, columnspan=5, pady=5, padx=10)

    # END OF THE WINDOW
    root.mainloop()

# CALL THE WHOLE FORM OF REGISTRATION FORM
if __name__ == "__main__":
    registration_form()
