from multiprocessing.pool import INIT
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import student_login
import mysql.connector

def init2():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="for_student_signup",
        )

    except mysql.connector.Error as err:
        messagebox.showerror("Connection Error", f"Error: {err}")
        exit()

    root = Tk()
    root.geometry("1920x1080")
    root.iconbitmap('')
    root.title("Change your password")
    bgimage = (Image.open("FOR REG.jpg"))

    bg_photo = ImageTk.PhotoImage(bgimage)
    label_photo = Label(root, image=bg_photo)
    label_photo.place(relheight=1, relwidth=1)

    label = LabelFrame(root, text="Change your password", font=("Helvetica", 18, 'bold'), pady=10, padx=10, border=0, bg='#333333', fg='white')
    label.place(relx=0.5, rely=0.5, anchor=CENTER)
  #=====================================================================FUNCTIONALITIES PLACEHOLDER=================================================================================
    def current_password_enter(event):
        if entry1.get() == "Old password...":
            entry1.delete(0, END)
            entry1.config(fg='black', show='')

    def new_password_enter(event):
        if entry2.get() == "New password...":
            entry2.delete(0, END)
            entry2.config(fg='black', show='')

    def confirm_password_enter(event):
        if entry3.get() == "Confirm password...":
            entry3.delete(0, END)
            entry3.config(fg='black', show='')


    #=========================================================================================================LABELS=====================================================================
    label1 = Label(label, text="Old Password", font=("Helvetica", 12, 'bold'), bg='#333333', fg='white')
    label1.grid(row=0, column=1, padx=0, pady=0, sticky=W)

    label2 = Label(label, text="New Password", font=("Helvetica", 12, 'bold'), bg='#333333', fg='white')
    label2.grid(row=2, column=1, padx=0, pady=0, sticky=W)

    label3 = Label(label, text="Confirm Password", font=("Helvetica", 12, 'bold'), bg='#333333', fg='white')
    label3.grid(row=4, column=1, padx=0, pady=0, sticky=W)
    #==================================================================================================ENTRY======================================================================
    entry1 = Entry(label, fg='grey', width=40)
    entry1.insert(0, "Old password...")
    entry1.bind('<Return>', lambda event: click())
    entry1.bind('<FocusIn>', current_password_enter)
    entry1.grid(row=1, column=1, sticky=W)

    entry2 = Entry(label, fg='grey', width=40)
    entry2.insert(0, "New password...")
    entry2.bind('<Return>', lambda event: click())
    entry2.bind('<FocusIn>', new_password_enter)
    entry2.grid(row=3, column=1, sticky=W)

    entry3 = Entry(label, fg='grey', width=40)
    entry3.insert(0, "Confirm password...")
    entry3.bind('<Return>', lambda event: click())
    entry3.bind('<FocusIn>', confirm_password_enter)
    entry3.grid(row=5, column=1, sticky=W)


  #==========================================================================================================functionality for button======================================================
    def click():
        current_password = entry1.get()
        new_password = entry2.get()
        confirm_password = entry3.get()

        cursor = db.cursor()
        cursor.execute('SELECT pass FROM for_student_signup WHERE pass = %s', (current_password,))
        result = cursor.fetchone()

        if result is not None:
            cursor.execute('UPDATE for_student_signup SET pass = %s WHERE pass = %s', (new_password, current_password))
            db.commit()
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry1.config(fg='black', show='*')
            entry2.config(fg='black', show='*')
            entry3.config(fg='black', show='*')

            messagebox.showinfo("Password Changed", "Password changed successfully!")
            root.destroy()
            student_login.init()
        else:
            entry1.delete(0, END)
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry1.config(fg='black')
            entry2.config(fg='black')
            entry3.config(fg='black')
            messagebox.showerror("Invalid Password", "Invalid current password.")

    #====================================================================================hover for update password=====================================================================
    def on_hover_open(event):
        button.config(bg='blue',fg='white', relief=SOLID)

    def on_horver_leave(event):
        button.config(bg='#1877F2', fg='white', relief=FLAT)


    #======================================================================================BUTTON FOR UPDATE PASSWORD==========================================================================

    button = Button(label, text="Update Password", command=click, bd=0, bg='#1877F2', padx=55, fg='white', cursor="hand2", activebackground='#1877F2', activeforeground="white")
    button.bind("<Enter>", on_hover_open)
    button.bind("<Leave>", on_horver_leave)
    button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    init2()
