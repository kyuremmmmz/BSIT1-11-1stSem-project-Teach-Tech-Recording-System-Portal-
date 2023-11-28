from tkinter import*
from PIL import Image, ImageTk
import mysql.connector
import student_login
import For_P1
import For_P2
import For_P3
from tkinter import ttk
from tkinter import messagebox

try:
    connector = mysql.connector.connect(host = 'localhost', user='root', password='admin', database = 'for_teacher_form')
except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Error: {err} ")



def init():
    root = Tk()
    root.title("Student Table")
    root.geometry("2000x1000")
    
    
    frame_student = Label(root, text=f"WELCOME TO STUDENT VIEW BLOCK-11 AY 2324", font=("Helvitica", 20, 'bold'), width=20,bg='#333333', fg='white' ,bd=40,borderwidth=30, relief=RIDGE, padx=760)
    frame_student.grid(row=0, column=1,  sticky=W)



    #=========================================================================hover for signout button===================================================================
    def hover_enter(event):
        Sign_out_button.config(bg='darkgreen', fg='white', relief='solid')

    def hover_leave(event):
        Sign_out_button.config(bg='green', fg='white', relief='flat')

    def hover_P1_enter(event):
        P1_button.config(bg='darkgreen', fg='white', relief='solid')

    def hover_P1_leave(event):
        P1_button .config(bg='green', fg='white', relief='flat')


    def hover_P2_enter(event):
        P2_button.config(bg='darkgreen', fg='white', relief='solid')

    def hover_P2_leave(event):
        P2_button .config(bg='green', fg='white', relief='flat')


    def hover_P3_enter(event):
        P3_button.config(bg='darkgreen', fg='white', relief='solid')

    def hover_P3_leave(event):
        P3_button .config(bg='green', fg='white', relief='flat')



    #==========================================================================SIGNOUT BUTTON FUNCITONALITY==================================================================
    def signout():
        root.destroy()
        student_login.init()    


    #=========================================================================P1 BUTTON FUNCTION=======================================================================================
    def P1():
        root.destroy()
        For_P1.P1()   

    #=========================================================================P2 BUTTON FUNCTION=======================================================================================
    def P2():
        root.destroy()
        For_P2.P2()     


    #=========================================================================P3 BUTTON FUNCTION=======================================================================================
    def P3():
        root.destroy()
        For_P3.P3()     

    #==================================================================FRAME FOR P1=================================================================================================
    frame_for_P1 = Frame(root, bg='#333333',bd=40,borderwidth=30, relief=RIDGE,)
    label_for_P1=Label(frame_for_P1, text="DASHBOARD", font=("Helvitica", 20, 'bold'), width=20,bg='#333333', fg='white' ,bd=40,borderwidth=30, relief=RIDGE, padx=760)
    label_for_P1.pack(anchor=CENTER)
    frame_for_P1.place(x=0, y=100, width=1920, height=900)


    #===================================================================ANNOUNCEMENT=================================================================================================
    announcement = Text(frame_for_P1, state='normal',font=('arial', 14,'bold'))
    announcement.place(x=200, y=95, height=745,width=1660)

    cursor = connector.cursor()
    query = "SELECT announcement FROM for_announcement"
    cursor.execute(query)
    announcement_2 = cursor.fetchall()
    announcement.delete('1.0', 'end')

    if announcement_2:
        for announce in announcement_2:
            announcement.insert('end', announce[0] + "\n")
            announcement.config(state='disabled')
    else:
        announcement.insert('end', "No announcement yet\n")
        announcement.config(state='disabled')


   


    #========================================================================P1 BUTTON===========================================================================================
    P1_button = Button(frame_for_P1, 
                       text="SHOW P1 BREAKDOWN", 
                       
                       font=("Helvitica", 12, 'bold'),
                        
                       padx=1, 
                        
                        pady=5,
                        
                        bd=1,
                        
                        bg='green',
                        
                        activebackground='green',
                        
                        activeforeground='white', 
                        
                        fg='white',
                        
                        cursor="hand2",
                        
                        command=P1)
    
    P1_button.bind("<Enter>", hover_P1_enter )
    
    P1_button.bind("<Leave>", hover_P1_leave)
    
    P1_button.place(x=0, y=100)

    #========================================================================P2 BUTTON===========================================================================================
    P2_button = Button(frame_for_P1, 
                       
                       text="SHOW P2 BREAKDOWN", 
                       
                       font=("Helvitica", 12, 'bold'), 
                       
                       padx=1, 
                       
                       pady=5, 
                       
                       bd=1, 
                       
                       bg='green',
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       fg='white', 
                       
                       cursor="hand2",
                       
                       command=P2)
    
    P2_button.bind("<Enter>", hover_P2_enter )
    
    P2_button.bind("<Leave>", hover_P2_leave)
    
    P2_button.place(x=0, y=150)

    #========================================================================P3 BUTTON===========================================================================================
    P3_button = Button(frame_for_P1, 
                       
                       text="SHOW P3 BREAKDOWN", 
                       
                       font=("Helvitica", 12, 'bold'), 
                       
                       padx=1, 
                       
                       pady=5, 
                       
                       bd=1, 
                       
                       bg='green',
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       fg='white', 
                       
                       cursor="hand2",
                       
                       command=P3)
   
    P3_button.bind("<Enter>", hover_P3_enter )
   
    P3_button.bind("<Leave>", hover_P3_leave)
   
    P3_button.place(x=0, y=200)


    #========================================================================SIGNOUT BUTTON=====================================================================================
    Sign_out_button = Button(frame_for_P1, text="Signout", font=("Helvitica", 12, 'bold'), padx=65, pady=5, bd=1, bg='green',activebackground='green', activeforeground='white', fg='white', cursor="hand2",command=signout)
    Sign_out_button.bind("<Enter>", hover_enter )
    Sign_out_button.bind("<Leave>", hover_leave)


    Sign_out_button.place(x=0, y=800)

    


    

    root.mainloop()
if __name__ == "__main__":
    init()