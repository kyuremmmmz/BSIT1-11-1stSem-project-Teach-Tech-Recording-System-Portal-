from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import registration_form#I imported this to appear the registration form
import databasedesign
import forgot_password
import mysql.connector
import time
counter=0



try:
    db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="for_login",
        )
    
except mysql.connector.Error as err:
    messagebox.showerror("Connection Error", f"Error: {err}")
    exit()  # Exit the program in case of a connection error

def init():
    #START OF ROOT
    root = Tk()
    bgimage = Image.open('FOR REG.jpg')
    bg_photo = ImageTk.PhotoImage(bgimage)
    root.iconphoto(False, PhotoImage(file="LOGO.png"))
    label_photo = Label(root, image=bg_photo)
    label_photo.place(relheight=1, relwidth=1)

    root.geometry("1920x1080")
    root.title("Login your account")

    
    
    label = LabelFrame(root, text=("Teacher Login Form"), font=("Helvitica", 18, 'bold'), pady=10, padx=10,border=0, bg='#333333', fg='white')
    
    label.place(relx=0.5,rely=0.5, anchor=CENTER)
    
    


    #LABELS
    User =  Label(label, text="User name", font=("Helvitica", 12, 'bold'), cursor='ibeam', bg='#333333', fg='white' )
    User.grid(row=0, column=1, sticky=W, padx=0, pady=0)
    Or =  Label(label, text="_____________________or______________________", bg='#333333', fg='white')
    Or.grid(row=6, column=1,sticky= W, padx=6, pady=0 )
    
    Password = Label(label, text="Password", font=("Helvitica", 12, 'bold') , bg='#333333', fg='white')
    Password.grid(row=2, column=1, padx=0, pady=0, sticky=W)

    #HOVER FOR LOGIN
    def on_hover_open(event):
        button.config(bg='blue',fg='white', relief=SOLID)

    def on_horver_leave(event):
        button.config(bg='#1877F2', fg='white', relief=FLAT)

    #HOVER FOR FORGOT PASSWORD
    def hover_forgot_password(event):
         forgot_password2.config(bg='white', fg='blue', relief=SOLID)
    def hover_forgot_password_close(event):
         forgot_password2.config(bg='#333333', fg='#1877F2', relief=FLAT)
    #HORVER FOR SIGN-UP
    def horver_signup_open(event):
         registration_button.config(bg='darkgreen', fg='white', relief='solid')

    def horver_signup_leave(event):
         registration_button.config(bg='#008000', fg='white', relief=FLAT)    
        

    
            

    #PLACE HOLDER
    def user_enter(event):
        if entry1.get() == "User name":
            entry1.delete(0, END)
            entry1.config(fg='black')
        
             

    def user_password(event):
        if entry2.get() == "Password":
            entry2.delete(0, END)
            entry2.config(fg='black', show='*')
        
    #TEXTBOX
    entry1 = Entry(label, fg='grey', width=40)
    entry1.insert(0, "User name")
    entry1.bind('<FocusIn>', user_enter)
    entry1.bind('<Return>', lambda event: click())
    entry1.grid(row=1, column=1, sticky=W, padx=0, pady=0)
    
    entry2 = Entry(label, fg='grey', width=40)
    entry2.insert(0, "Password")
    entry2.bind('<FocusIn>', user_password)
    entry2.bind('<Return>', lambda event: click())
    entry2.grid(row=3, column=1,  sticky=W, padx=0, pady=0)
    
    



 #BUTTON FUNCTIONALITY
    def click():
        global counter
        user_enter = entry1.get()#get the function of the entry
        password_enter = entry2.get()#get the function of the entry
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM for_signup WHERE u_name = %s AND pass = %s', (user_enter, password_enter))
            results = cursor.fetchone()
            # Clear the input fields
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry1.config(fg='black')
            entry2.config(fg='black', show="*")
            #CONDITIONAL FOR LOGIN
            if counter >=10:
                messagebox.showinfo("Please wait", "Too many attempts please wait for 10 seconds")
                button.config(state='disabled')
                time.sleep(9)
                button.configure(state='active')
                entry2.config(show="*")
                counter-=10
        
            if results:
                messagebox.showinfo("Login", "Login Success")
                root.destroy()
                databasedesign.database()
        
            else:
                messagebox.showerror("Error", "Wrong password and user name please try again")
                entry1.delete(0, END)
                entry2.delete(0, END)
                counter+=1
            

        except mysql.connector.Error as err:
            messagebox.showerror("Connection Error", f"Error: {err}")
            entry1.delete(0, END)
            entry2.delete(0, END)

           
           #FUNCTIONALITY FOR REGISTRATION BUTTON
    def open_registration_form():
        root.destroy()
        registration_form.registration_form()#function for registration form
        
        #FUNCTIONALITY FOR FORGOT PASSWORD
    def forgotpassword():
       root.destroy()
       forgot_password.init()
       
       
        
        
           
        
        

   
            

        
    
    #BUTTON FOR LOGIN
    button = Button(label,text="Login", command=click, bd=0, bg='#1877F2', padx=55, fg='white', cursor="hand2", activebackground='#1877F2', activeforeground="white")
    button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    button.bind(click)
    button.bind("<Enter>", on_hover_open)
    button.bind("<Leave>", on_horver_leave)
    
    #DISPLAY REGISTRATION BUTTON
    registration_button = Button(label, text="Sign-up", command=open_registration_form, bg='green', fg='white', bd=0, padx=50, cursor="hand2", activebackground='green', activeforeground='white')
    registration_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    registration_button.bind("<Enter>", horver_signup_open)
    registration_button.bind("<Leave>", horver_signup_leave)
    
    
    ##BUTTON FOR FORGOT PASSWORD
    forgot_password2 = Button(label, text= "Forgot password?", command=(forgotpassword), fg='#1877F2', bd=0, bg='#333333', highlightcolor='#333333',highlightbackground='#333333', cursor="hand2")
    forgot_password2.bind("<Enter>", hover_forgot_password)
    forgot_password2.bind("<Leave>", hover_forgot_password_close)
    forgot_password2.grid(row=8, column=1, columnspan=1)

    #CHECK BOX FOR REMEMBER ME
    #CHECK BOX FOR REMEMBER ME
    check = IntVar()
    remember_me = Checkbutton(label, text="Remember me", bg='#333333', fg='white', highlightbackground='#333333', highlightcolor='#333333', selectcolor='#333333',variable=check, activebackground='orange', activeforeground='white')
    remember_me.grid(row=10, column=1, columnspan=5, rowspan=5, pady=6)


    

    
    
    
    #END OF WINDOW
    root.mainloop()

#CALL THE FUNCTION OF THE WHOLE WINDOW
if __name__ == "__main__":
 init()   