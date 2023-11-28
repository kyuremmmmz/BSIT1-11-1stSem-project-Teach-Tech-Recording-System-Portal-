from tkinter import*
import mysql.connector
import student_table
from tkinter import ttk
from tkinter import messagebox
try:
    database = mysql.connector.connect(host = "localhost", 
                                       user = "root", 
                                       password = "admin", 
                                       database ="for_teacher_form")
except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Error: {err}")


def P1():
    root = Tk()
    root.title("P1 Grades")
    root.geometry("1080x1000")
    #========================================================================FRAME FOR THE TITLE================================================================================
    frame_student = Label(root, text=f"P1 GRADES", font=("Helvitica", 20, 'bold'), width=20,bg='#333333', fg='white' ,bd=40,borderwidth=30, relief=RIDGE, padx=760)
    frame_student.grid(row=0, column=1,  sticky=W)
    

    #=========================================================================P1 RECORDS=======================================================================================
    frame_for_P1 = Frame(root, bg='#333333',bd=40,borderwidth=30, relief=RIDGE,)
    label_for_P1=Label(frame_for_P1, text="P1 RECORDS", font=("Helvitica", 20, 'bold'), width=20,bg='#333333', fg='white' ,bd=40,borderwidth=30, relief=RIDGE, padx=730)
    label_for_P1.pack(anchor=CENTER)
    frame_for_P1.place(x=0, y=100, width=1000, height=900)


    #==========================================================================FRAME FOR SEARCH BAR===============================================================================
    frame_for_search_bar = Frame(root,bg='#333333',bd=0,borderwidth=30, relief=RIDGE)
    frame_for_search_bar.place(x=1000, y=100, width=920, height=900)

    #=========================================================================PLACEHOLDER=================================================================================
    def placeholder(event):
       if search_entry.get()== "Enter your id...":
          search_entry.delete(0, END)
          search_entry.config(fg='black')
        
    def placeholder_leave(event):
       if not search_entry.get():
          search_entry.insert(0, "Enter your id...")
          search_entry.config(fg='grey')
    #=========================================================================HOVER BUTTON====================================================================================
    def hover_enter(event):
       search_button.config(bg='white', fg='#333333', relief=SOLID)

    def hover_leave(event):
       search_button.config(bg='#333333', fg='white', relief='flat')   

    def hover_enterback(event):
       back_button.config(bg='darkgreen', fg='white', relief='solid')

    def hover_enterleave(event):
       back_button.config(bg='green', fg='white', relief='flat')
   #===========================================================================SEARCH BUTTON FUNCTION=========================================================================
    def search_data():
         search = search_entry.get()
         cursor = database.cursor()
         query = "SELECT * FROM for_p1 WHERE student_id = %s"
         cursor.execute(query, (search,))
         items = cursor.fetchall()

         data2 = display.get_children()
    # Clear the existing data in the display widget
         for data in data2:
          display.delete(data)

         for row in items:
            display.insert('', 'end', values=row)

           
        

    #=========================================================================SEARCH MY ID=======================================================================================
    search_entry =  Entry(frame_for_search_bar, width=84, font=("helvitica", 12), fg='grey')
    search_entry.insert(0,"Enter your id...")
    search_entry.bind('<FocusIn>', placeholder)
    search_entry.bind('<FocusOut>', placeholder_leave)
    search_entry.bind("<Return>", lambda event: search_data())
    
    search_entry.place(x=90, y=5)


    #===========================================================================SEARCH BUTTON=======================================================================================
    search_button =  Button(frame_for_search_bar, 
                            font=('calibri', 14, 'bold'), 
                            bg='#333333', 
                            fg='white', 
                            bd=0,
                            pady=0, 
                            activeforeground='white', 
                            activebackground='#333333', 
                            text="Search", 
                            cursor="hand2",
                            command=search_data)

    search_button.bind("<Enter>", hover_enter)
    search_button.bind("<Leave>", hover_leave)
    
    search_button.place(x=0, y=0)
     #==========================================================================BACK BUTTON FUNCTION=====================================================================
    def back_button_function():
       root.destroy()
       student_table.init()
    #========================================================================BACK BUTTON===================================================================================
    back_button = Button(frame_for_P1, font=('calibri', 15, 'bold'), bg='green', 
                            fg='white', 
                            bd=0,
                            pady=0, 
                            activeforeground='white', 
                            activebackground='green', 
                            text="Back to dashboard", 
                            cursor="hand2",
                            height=1,
                            command=back_button_function)
    back_button.bind("<Enter>", hover_enterback)
    back_button.bind("<Leave>", hover_enterleave)
    back_button.place(y=786, x=0)
    

    


    #==============================================================================SCROLLBARS==========================================================================
    scrollX = Scrollbar(frame_for_P1, orient='horizontal', bg='#333333')
    scrollX.pack(side='bottom', fill=X)

    scrollY = Scrollbar(frame_for_P1, orient='vertical')
    scrollY.pack(side='right', fill=Y)


    #==============================================================================DISPLAY RECORDS=============================================================================

    #=============================================================================P1 DISPLAY RECORDS============================================================================
    columns = ('student id', 'P1 GRADE', 'activities', 'exam', 'quizzes', 'number of presents')
    display = ttk.Treeview(frame_for_P1, show='headings', columns=columns,  xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
    display.heading('student id', text='Student ID')
    display.heading('P1 GRADE', text='P1 Grade')
    display.heading('activities', text='Activities')
    display.heading('exam', text='Exam')
    display.heading('quizzes', text='Quizzes')
    display.heading('number of presents', text='Number of Presents')

    display.column('student id', width=100, anchor='center')
    display.column('P1 GRADE',  width=100, anchor='center')
    display.column('activities',  width=100, anchor='center')
    display.column('exam',  width=100, anchor='center')
    display.column('quizzes', width=100, anchor='center')
    display.column('number of presents',  width=100, anchor='center')
    scrollX.config(command=display.xview)
    scrollY.config(command=display.yview)
    display.place(x=0, y=95, height=690, width=920)

    query = "SELECT * FROM for_p1"
    cursor = database.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        display.insert('', 'end', values=row)

    root.mainloop()

if __name__ == "__main__":
 P1()
