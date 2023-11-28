from tkinter import*
from tkinter import ttk
import databasedesign
from tkinter.messagebox import askyesno
from tkinter import messagebox
import mysql.connector
db = mysql.connector.connect(host = 'localhost',
                             user = 'root',
                             password = 'admin',
                             database = 'for_teacher_form')
def announcement():
    root = Tk()
    root.geometry("1000x1000")
    root.title("Announcement")
  #================================================================================FRAME FOR SEARCH================================================================================
    frame_for_P1 = Frame(root, bg='#333333',bd=40,borderwidth=30, relief=RIDGE,)
    label_for_P1=Label(frame_for_P1, text="CREATE ANNOUNCEMENT", font=("Helvitica", 20, 'bold'), width=20,bg='#333333', fg='white' ,bd=40,borderwidth=30, relief=RIDGE, padx=830)
    label_for_P1.pack(anchor=CENTER)
    frame_for_P1.place(x=0, y=100, width=1920, height=900,)

    recording_system = Label(root, 
                             
                             text=" RECORDING SYSTEM (TEACH TECH TEACHER FORM)", 
                             
                             font=("Helvitica", 20, 'bold'), 
                             
                             width=20,bg='#333333', 
                             
                             fg='white' ,
                             
                             bd=40,
                             
                             borderwidth=30, 
                             
                             relief=RIDGE, padx=760)
    recording_system.grid(row=0, column=1,  sticky=W)


    #=================================================================================FUNCTION DELETE=====================================================================
    def delete_anouncement():
        messagebox.askyesno("Delete announcement", "Are you sure you want to delete all of these announcements?")
        cursor2 = db.cursor()
        query2 = ("DELETE FROM for_announcement")
        cursor2.execute(query2)
        db.commit()
        messagebox.showinfo("Deleted", "you've been deleted successfully!")
        announcement_entry.config(state='normal')
        announcement_entry.delete("1.0", "end")


    #================================================================================FUNCTION FOR CREATE========================================================================
    def create_announcement():
        announce = announcement_entry.get("1.0", "end-1c")
        cursor = db.cursor()
        query = "INSERT INTO for_announcement(announcement) VALUES (%s)"
        data = (announce,)
        cursor.execute(query, data)
        db.commit()
        messagebox.showinfo("Announced", "You've been announced successfully!")
    
        announcement_entry.config(state='disabled') 
    
        
        announcement_entry.delete("1.0", "end-1c")
        additional_text = "Additional text here"
        announcement_entry.insert("end", additional_text)

    #==============================================================================FUNCTION FOR BACK================================================================================
    def back():
        root.destroy()
        databasedesign.database()



    #================================================================================HOVER BUTTON==============================================================================================
    def hover_for_enter_create(event):
        button_create.config(bg='darkgreen', bd=1, relief='solid')

    def hover_for_leave_create(event):
        button_create.config(bg='green', bd=0, relief='flat')

    def hover_for_enter_delete(event):
        button_delete.config(bg='darkgreen', bd=1, relief='solid')

    def hover_for_leave_delete(event):
        button_delete.config(bg='green', bd=0, relief='flat')

    def hover_for_enter_back(event):
        button_back.config(bg='darkgreen', bd=1, relief='solid')

    def hover_for_leave_back(event):
        button_back.config(bg='green', bd=0, relief='flat')




    #================================================================================BUTTON========================================================================================
    button_create = Button(frame_for_P1, text="Create", 
                          
                          font=("arial", 14, 'bold'), 
                          
                          fg='white', 
                          
                          bg='green',
                          
                          bd=0,

                          padx='50',

                          pady=2,
                          
                          activebackground='green',
                          
                          activeforeground='white',

                          cursor='hand2',
                          
                          command=create_announcement
                          )
    button_create.place(x=0, y=100)
    button_create.bind("<Enter>", hover_for_enter_create)
    button_create.bind("<Leave>", hover_for_leave_create)

    button_delete = Button(frame_for_P1, 
                           
                           text="Delete announcement",
                           
                           font=("arial", 14, 'bold'), 
                          
                           fg='white', 
                          
                           bg='green',
                          
                           bd=0,

                           padx='1',

                           pady=2,
                          
                           activebackground='green',
                          
                           activeforeground='white',

                           cursor='hand2',

                           command=delete_anouncement
                           )
    button_delete.place(y=100, x=200)
    button_delete.bind("<Enter>", hover_for_enter_delete)
    button_delete.bind("<Leave>", hover_for_leave_delete)

    button_back = Button(frame_for_P1, 
                           
                           text="Back",
                           
                           font=("arial", 14, 'bold'), 
                          
                           fg='white', 
                          
                           bg='green',
                          
                           bd=0,

                           padx='70',

                           pady=2,
                          
                           activebackground='green',
                          
                           activeforeground='white',

                           cursor='hand2',

                           command=back
                           )
    button_back.place(y=100, x=450)
    button_back.bind("<Enter>", hover_for_enter_back)
    button_back.bind("<Leave>", hover_for_leave_back)


    #==============================================================================ENTRY========================================================================================
    announcement_entry = Text(frame_for_P1, font=('arial', 14) )
    announcement_entry.place(height=690, x=0, y=150, width=1860)
    cursor = db.cursor()
    query = "SELECT announcement FROM for_announcement"
    cursor.execute(query)
    announcement_2 = cursor.fetchall()
    announcement_entry.delete('1.0', 'end')

    if announcement_2:
        for announce in announcement_2:
            announcement_entry.insert('end', announce[0] + "\n")
    else:
        announcement_entry.insert('end', "No announcement yet\n")

    if announcement_entry == "No announcement yet":
        announcement_entry.delete('1.0', END)
        

    root.mainloop()

if __name__ == "__main__":
    announcement()