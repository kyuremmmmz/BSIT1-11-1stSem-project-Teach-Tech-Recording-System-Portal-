from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import student_login
import loginform
import registration_form
import mysql.connector
try:
    connect = (mysql.connector.connect(host = "localhost", 
                                    user= "root", 
                                    password ="admin", 
                                    database = "for_login" ))
except mysql.connector.Error as err:
   messagebox.showerror(f"Error", f"Error: {err} ")
def __init__():
    root = Tk()
    root.geometry("500x500")
    root.iconphoto(False, PhotoImage(file="LOGO.png"))
    root.title("Decision")

    labelbg = Label(root, text="WELCOME TO TEACH TECH", width=30, fg='red', font=("Times new roman", 20, 'bold', ), bd=20, borderwidth=20, relief=RIDGE)
    labelbg.pack(side=TOP, fill=X)
    label_for_d = LabelFrame(root, text="Select your status:", font=("Arial", 12))
    label_for_d.place(relx=0.5, rely=0.5, anchor='center')
    


    #FUNCTIONALITY FOR TEACHER BUTTON
    def teachr():
        root.destroy()
        loginform.init()

    def stdnt():
       root.destroy()
       student_login.init()
    
    btn_for_teacher = Button(label_for_d, text="Teacher", padx=45,command=teachr)
    btn_for_teacher.grid(row=0, column=1)

    btn_for_stdnt =  Button(label_for_d, text="Student", padx=45, command=stdnt)
    btn_for_stdnt.grid(row=2, column=1)

    
    root.mainloop()

if __name__ == "__main__":
 __init__() 