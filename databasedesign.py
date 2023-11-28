from tkinter import*
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter import messagebox
import loginform
import for_announcement
import for_grade_calculator
from PIL import Image, ImageTk
import mysql.connector
db = mysql.connector.connect(host = 'localhost',
                             user = 'root',
                             password = 'admin',
                             database = 'for_teacher_form')
messagebox.showinfo("Database", "Database connected")


def database():
    root = Tk()
    root.geometry("2000x1000")
    root.iconphoto(False, PhotoImage(file="LOGO.png"))
    root.title("Teach Tech")
    
    #CREATE A LABEL FOR USER NAME. LAST NAME, MIDDLE NAME, GIVEN NAME, AGE, PASSWORD
    #================================================================================FRAME FOR STUDENT DATA============================================================
    bg_for_student_data = Frame(root, bg='#333333', bd=20, relief=RIDGE)
    bg_for_student_data.place(x=0, y=100, width=1000, height=380)

    #================================================================================FRAME FOR SEARCH============================================================
    bg_for_search = Frame(root, bg='#333333', bd=20, relief=RIDGE)
    bg_for_search.place(x=1010, y=100, width=913, height=380)

    recording_system = Label(root, 
                             
                             text=" RECORDING SYSTEM (TEACH TECH TEACHER FORM)", 
                             
                             font=("Helvitica", 20, 'bold'), 
                             
                             width=20,bg='#333333', 
                             
                             fg='white' ,
                             
                             bd=40,
                             
                             borderwidth=30, 
                             
                             relief=RIDGE, padx=765)
    recording_system.grid(row=0, column=1,  sticky=W)
    
    #=============================================================================================FRAME FOR INFOS==========================================================================
    bg_for_student_data2 = Frame(root, bg='#333333', bd=20, relief=RIDGE)
    bg_for_student_data2.place(x=0, y=500, width=1920, height=500)



    #=========================================================================================hover for search button======================================================================
    def hover_search_button_enter(event):
        search_buttom.config(bg='white', fg='#333333', relief=SOLID)
    
    def hover_search_button_leave(event):
        search_buttom.config( bg='#333333',fg='white', )


    #===========================================================================================hover for sign out=============================================================================
    def hover_signout_enter(event):
        sign_out.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_signout_leave(event):
        sign_out.config(bg='green', fg='white', relief=FLAT, bd=1)
    #===============================================================================================hover for save btn=============================================================
    def hover_save_enter(event):
        button_for_save_data_to_db.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_save_leave(event):
        button_for_save_data_to_db.config(bg='green', fg='white', relief=FLAT)

    #================================================================================================hover for clear button==============================================================
    def hover_clear_enter(event):
        button_for_clear_entry_to_db.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_clear_leave(event):
        button_for_clear_entry_to_db.config(bg='green', fg='white', relief=FLAT)

    #==============================================================================================hover for add button=================================================================
    def hover_add_enter(event):
        button_for_add_entry_to_db.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_add_leave(event):
        button_for_add_entry_to_db.config(bg='green', fg='white', relief=FLAT)

    #=========================================================================================hover for grade calcu button=====================================================
    def hover_calcu_enter(event):
        button_for_grade_calcu.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_calcu_leave(event):
        button_for_grade_calcu.config(bg='green', fg='white', relief=FLAT)

    #=========================================================================================hover for grade tracker=====================================================
    def hover_tracker_enter(event):
        button_for_grade_tracker.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_tracker_leave(event):
        button_for_grade_tracker.config(bg='green', fg='white', relief=FLAT)


    #==============================================================================================HOVER FOR ATTENDANCE TRACKER================================================
    def hover_attendance_tracker_enter(event):
        attendance_tracker_btn.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_attendace_tracker_leave(event):
        attendance_tracker_btn.config(bg='green', fg='white', relief=FLAT)


     #=========================================================================================hover for ANNOUNCEMENT=====================================================
    def hover_attdnce_trcker_enter(event):
        button_for_attendance_tracker.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_attdnce_trcker_leave(event):
        button_for_attendance_tracker.config(bg='green', fg='white', relief=FLAT)
    
    #===========================================================================================hover for about=====================================================================
    def hover_about_enter(event):
        about_button.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_about_leave(event):
        about_button.config(bg='green', fg='white', relief=FLAT)

    #=====================================================================================HOVER FOR HELP============================================================================
    def hover_help_enter(event):
        button_for_help.config(bg='darkgreen', fg='white', relief=SOLID)

    def hover_help_leave(event):
        button_for_help.config(bg='green', fg='white', relief=FLAT)

    #=========================================================================================Placeholder=======================================================================
    def placeholder_forsearch(event):
        if search_entry.get()=="Search Student ID...":
            search_entry.delete(0, END)
            search_entry.config(foreground='black')
    

    
    def placeholder_forleave(event):
        if not search_entry.get():
            search_entry.insert(0,"Search Student ID...")
            search_entry.config(foreground='grey')

    #=======================================================================================FUNCTIONALITY FOR DELETEE DB========================================================
    def button_for_save_data():
            delete = messagebox.askyesno("Delete data", "Delete all of these data?")
            if delete:
                 try:
                    cursor_3 = db.cursor()
                    delete_query= "DELETE FROM add_button"
                    cursor_3.execute(delete_query)
                    db.commit()
                    items = display.get_children()
                    for item in items:
                        display.delete(item)
                    messagebox.showinfo("Success", "Data deleted successfully.")
                 except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error: {err}")
        

        
    #=================================================================================================LABELS====================================================================================
    student_ID = Label(bg_for_student_data, text="Student ID: ",
                       font=20, 
                       bg='#333333', 
                       fg='white')
    student_ID.grid(row=1, column=1, sticky=W, padx=200, pady=20)
    
    last_name = Label(bg_for_student_data, text="Last Name: ", font=20, bg='#333333', fg='white')
    last_name.grid(row=2, column=1, padx=200, pady=20, sticky=W)

    given_name = Label(bg_for_student_data, text="Given Name: ", font=20, bg='#333333', fg='white')
    given_name.grid(row=3, column=1, padx=200, pady=20, sticky=W)

    middle_initial = Label(bg_for_student_data, text="Middle Initial: ", font=20, bg='#333333', fg='white')
    middle_initial.grid(row=4, column=1, padx=200, pady=20, sticky=W)

    age = Label(bg_for_student_data, text="Age: ", font=20, bg='#333333', fg='white')
    age.grid(row=5, column=1, padx=200, pady=20, sticky=W)

    number_of_presents = Label(bg_for_student_data, text="Number of presents: ", font=20, bg='#333333', fg='white')
    number_of_presents.grid(row=1, column=1, sticky=W, padx=600, pady=20)

    grade1 = Label(bg_for_student_data, text="P1 Grade: ", font=20, bg='#333333', fg='white')
    grade1.grid(row=2, column=1, sticky=W, padx=600, pady=20)

    grade2 = Label(bg_for_student_data, text="P2 Grade: ", font=20, bg='#333333', fg='white')
    grade2.grid(row=3, column=1, sticky=W, padx=600, pady=20)
    
    grade3 = Label(bg_for_student_data, text="P3 Grade: ", font=20, bg='#333333', fg='white')
    grade3.grid(row=4, column=1, sticky=W, padx=600, pady=20)

    final = Label(bg_for_student_data, text="Final Grade: ", font=20, bg='#333333', fg='white')
    final.grid(row=5, column=1, sticky=W, padx=600, pady=20)
    #===============================================================================ENTRY===============================================================================================
    student_ID_entry = Entry(bg_for_student_data, width=20, font=("arial", 12))
    student_ID_entry.bind('<Return>', lambda event:add_data())
    student_ID_entry.grid(row=1, column=1,columnspan=1, sticky=W, padx=300, pady=20)
    
    last_name_entry = Entry(bg_for_student_data, width=20, font=("arial", 12))
    last_name_entry.bind('<Return>', lambda event:add_data())
    last_name_entry.grid(row=2, column=1,columnspan=1, sticky=W, padx=300, pady=20)

    given_name_entry =  Entry(bg_for_student_data, width=20, font=("arial", 12))
    given_name_entry.bind('<Return>', lambda event:add_data())
    given_name_entry.grid(row=3, column=1,columnspan=1, sticky=W, padx=300, pady=20)

    middle_initial_entry = Entry(bg_for_student_data, width=20, font=("arial", 12))
    middle_initial_entry.bind('<Return>', lambda event:add_data())
    middle_initial_entry.grid(row=4, column=1,columnspan=1, sticky=W, padx=300, pady=20)

    age_entry = Entry(bg_for_student_data, width=20, font=("arial", 12))
    age_entry.bind('<Return>', lambda event:add_data())
    age_entry.grid(row=5, column=1,columnspan=1, sticky=W, padx=300, pady=20)

    number_of_presents_entry = Entry(bg_for_student_data, width=20, font=("arial", 12))
    number_of_presents_entry.bind('<Return>', lambda event:add_data())
    number_of_presents_entry.grid(row=1, column=1,columnspan=1, sticky=W, padx=770, pady=20)

    grade_entry1 = Entry(bg_for_student_data, width=20, font=("arial", 12))
    grade_entry1.bind('<Return>', lambda event:add_data())
    grade_entry1.grid(row=2, column=1,columnspan=1, sticky=W, padx=770, pady=20)

    grade_entry2 = Entry(bg_for_student_data, width=20, font=("arial", 12))
    grade_entry2.bind('<Return>', lambda event:add_data())
    grade_entry2.grid(row=3, column=1,columnspan=1, sticky=W, padx=770, pady=20) 

    grade_entry3 = Entry(bg_for_student_data, width=20, font=("arial", 12))
    grade_entry3.bind('<Return>', lambda event:add_data())
    grade_entry3.grid(row=4, column=1,columnspan=1, sticky=W, padx=770, pady=20)

    final_entry = Entry(bg_for_student_data, width=20, font=("arial", 12))
    final_entry.bind('<Return>', lambda event:add_data())
    final_entry.grid(row=5, column=1,columnspan=1, sticky=W, padx=770, pady=20)      
    #================================================================================SIGN OUT BUTTON FUNCTIONALITY========================================================================
    def signout():
        root.destroy()
        loginform.init()

    #==================================================================================CLEAR BUTTON FUNCTION===========================================================================
    def clearall():
        clear = askyesno("Confirmation", "Are you sure you want to clear all of these data?")
        if clear:
            student_ID_entry.delete(0, END)
            
            last_name_entry.delete(0, END)
            
            given_name_entry.delete(0, END)
            
            middle_initial_entry.delete(0, END)
            
            age_entry.delete(0, END)
            
            number_of_presents_entry.delete(0, END)
            
            grade_entry1.delete(0, END)
            
            grade_entry2.delete(0, END)
            
            grade_entry3.delete(0, END)
            
            final_entry.delete(0, END)










    #============================================================================================SIGN OUT BUTTON=====================================================================
    sign_out = Button(bg_for_student_data, text="Sign out", command=signout, padx=65, font=(20), bd=1, bg='green', activebackground='green', activeforeground='white', fg='white', cursor="hand2")
    sign_out.bind("<Enter>", hover_signout_enter)
    sign_out.bind('<Leave>', hover_signout_leave)
    sign_out.place(x=0, y=310, )

    #=====================================================================================================SEARCH BUTTON FUNCTIONAITY===================================================================
    def search_data():
        student_id = (search_entry.get())
        cursor = db.cursor()
        query = "SELECT * FROM add_button WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        data = cursor.fetchall()
        if data:
             # Clear the Treeview widget
            items = display.get_children()
            for item in items:
                display.delete(item)
            # Populate the Treeview with the search results
            for row in data:
                display.insert('', 'end', values=row)
        else:
            datos = display.get_children()
            for items2 in datos:
                display.delete(items2)
            messagebox.showinfo("No Data in records", "No records found for the given student ID.")




        

        cursor = db.cursor()

        # Fetch data from for_p1 table
        cursor.execute("SELECT student_id, P1_grade FROM for_p1 WHERE student_id = %s", (student_id,))
        data_p1 = cursor.fetchone()

        # Fetch data from for_p2 table
        cursor.execute("SELECT student_id, P2_grade FROM for_p2 WHERE student_id = %s", (student_id,))
        data_p2 = cursor.fetchone()

        # Fetch data from for_p3 table
        cursor.execute("SELECT student_id, P3_grade FROM for_p3 WHERE student_id = %s", (student_id,))
        data_p3 = cursor.fetchone()

        # Clear existing data in the grade_tracker Treeview
        grade_tracker.delete(*grade_tracker.get_children())

        # Check if any data is found
        if data_p1 or data_p2 or data_p3:
            student_id = data_p1[0] if data_p1 else ''
            p1_grade = float(data_p1[1].rstrip('%')) if data_p1 and data_p1[1] else None
            p2_grade = float(data_p2[1].rstrip('%')) if data_p2 and data_p2[1] else None
            p3_grade = float(data_p3[1].rstrip('%')) if data_p3 and data_p3[1] else None

            # Compute the final average for the row
            final_average = sum(grade for grade in [p1_grade, p2_grade, p3_grade] if grade is not None) / 3 if any(grade is not None for grade in [p1_grade, p2_grade, p3_grade]) else None

            combined_data = (
            student_id,
            f"{p1_grade}%" if p1_grade is not None else '',
            f"{p2_grade}%" if p2_grade is not None else '',
            f"{p3_grade}%" if p3_grade is not None else '',
            f"{final_average:.2f}%" if final_average is not None else ''
            )

            grade_tracker.insert('', 'end', values=combined_data)
        else:
            messagebox.showinfo("No Data in grade tracker", "No data found for the given student ID.")
            


        
        
        

    #======================================================================================================SEARCH BUTTON===============================================================
    search_buttom = Button(bg_for_search,text="Search", padx=20, font=('calibri,',12, 'bold'), bg='#333333', fg='white', bd= 0, activeforeground='white', activebackground='#333333',command=search_data)
    search_buttom.bind('<Enter>', hover_search_button_enter)
    search_buttom.bind('<Leave>', hover_search_button_leave)
    search_buttom.grid(row=0, column=1, sticky=W,  )

    #===================================================================SEARCH ENTRY=========================================================================================
    search_entry= ttk.Combobox(bg_for_search, font=('calibri', 12), width=93, foreground='grey')
    search_entry.insert(0, 'Search Student ID...')
    search_entry.bind('<FocusIn>', placeholder_forsearch )
    search_entry.bind("<FocusOut>", placeholder_forleave)
    search_entry.bind('<Return>', lambda event: search_data())
    search_entry.grid(row=0, column=1, sticky=W, padx=100)

    
    #==============================================================BUTTON FOR DELETE DATA TO DB=================================================================================
    button_for_save_data_to_db = Button(bg_for_student_data, text="Delete", padx=75, font=(20), bd=1, bg='green', activebackground='green', activeforeground='white', fg='white', cursor="hand2", command=button_for_save_data)
    button_for_save_data_to_db.bind("<Enter>", hover_save_enter)
    button_for_save_data_to_db.bind("<Leave>", hover_save_leave)
    button_for_save_data_to_db.place(x=230, y=310, )

    #==============================================================BUTTON FOR CLEAR ALL INPUTTED ENTRY TTO ENTRY===========================================================
    button_for_clear_entry_to_db = Button(bg_for_student_data, text="Clear all", padx=70, font=(20), bd=1, bg='green',activebackground='green', activeforeground='white', fg='white', cursor="hand2", command = clearall)
    button_for_clear_entry_to_db.bind("<Enter>", hover_clear_enter)
    button_for_clear_entry_to_db.bind("<Leave>", hover_clear_leave)
    button_for_clear_entry_to_db.place(x=480, y=310, )




#==============================================================BUTTON FUNCTIONALITY FOR ADD=========================================================================================
    def add_data():
        mycursor = db.cursor()
        myquery = ("INSERT INTO add_button(student_id, l_name, m_initial, g_name, age, number_of_presents , p1_grade, p2_grade, p3_grade, final_grade) VALUES(%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (student_ID_entry.get(), last_name_entry.get(), middle_initial_entry.get(), given_name_entry.get(), age_entry.get(),
                number_of_presents_entry.get(),grade_entry1.get(), grade_entry2.get(), grade_entry3.get(), final_entry.get())
        
        try:
            mycursor.execute(myquery, data)
            db.commit()
            messagebox.showinfo("Added", "Successfully added your data")
        except mysql.connector.Error as err:
            messagebox.showerror("Mysql error", f"Error: {err}")
        
        
        items = display.get_children()
        for item in items:
            display.delete(item)

        query = "SELECT student_id, l_name, g_name, m_initial, age, number_of_presents, p1_grade, p2_grade, p3_grade, final_grade FROM add_button  ORDER BY l_name"
        cursor = db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()  
        for row in data:
            display.insert('', 'end', values=row)



   
        
    #================================================================BUTTON FOR ADD DATA===================================================================================
    button_for_add_entry_to_db = Button(bg_for_student_data, 
                                        
                                        text="Add", 
                                        
                                        padx=89, 
                                        
                                        font=(20), 
                                        
                                        bd=1, 
                                        
                                        bg='green',
                                        
                                        activebackground='green', 
                                        
                                        activeforeground='white', 
                                        
                                        fg='white', 
                                        
                                        cursor="hand2", 
                                        
                                        command=add_data)
    button_for_add_entry_to_db.bind("<Enter>", hover_add_enter)
    button_for_add_entry_to_db.bind("<Leave>", hover_add_leave)
    button_for_add_entry_to_db.place(x=742, y=310, )

    #============================================================================FUNCTION FOR SHOW GRADE TRACKER===============================================================
    def specific_delete():
        selected_item = display.selection()  # Get the selected item in the Treeview
        if selected_item:  # Check if an item is selected
            selected_id = display.item(selected_item, "values")[0]  # Assuming the ID is the first column
            if selected_id:  # Check if an ID is retrieved
                confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?")
                if confirmation:
                    try:
                        cursor = db.cursor()
                        # Assuming 'for_p1' is the table name and 'student_id' is the primary key column
                        cursor.execute("DELETE FROM add_button WHERE student_id = %s", (selected_id,))
                        cursor.execute("DELETE FROM add_button WHERE student_id = %s", (selected_id,))
                        cursor.execute("DELETE FROM add_button WHERE student_id = %s", (selected_id,))
                        db.commit()
                        messagebox.showinfo("Deleted", "Record deleted successfully!")

                        # Delete the selected item from the Treeview
                        display.delete(selected_item)
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
            else:
                messagebox.showinfo("No ID", "No ID found for the selected item.")
        else:
            messagebox.showinfo("No Selection", "Please select an item to delete.")
        

    #=================================================================BUTTON FOR GRADE TRACKER==============================================================================
    button_for_grade_tracker =  Button(bg_for_student_data, 
                                       
                                       text="Delete row ", 
                                       
                                        padx=53, font=(20), 
                                       
                                       bd=1, bg='green',
                                       
                                       activebackground='green', 
                                       
                                       activeforeground='white', 
                                       
                                       fg='white', 
                                       
                                       cursor="hand2",
                                       command=specific_delete)
    button_for_grade_tracker.bind("<Enter>", hover_tracker_enter)
    button_for_grade_tracker.bind("<Leave>", hover_tracker_leave)
    button_for_grade_tracker.place(x=0, y=80, )


    #==============================================================BUTTON FUNCTIONALITY FOR GRADE CALCU=========================================================================
    def go_to_calcu():
        root.destroy()
        for_grade_calculator.init()

    



    #===========================================================SHOW DATA BUTTON FUNCTIONALITY=========================================================================================
    def click_showinfo():
            query = "SELECT student_id, l_name, g_name, m_initial, age, number_of_presents, p1_grade, p2_grade, p3_grade, final_grade FROM add_button  ORDER BY l_name"
            cursor = db.cursor()
            cursor.execute(query)
            data = cursor.fetchall()

            items = display.get_children()
            for item in items:
                display.delete(item)

            for row in data:
                display.insert('', 'end', values=row)
                
    #=========================================================hide data button function=================================================================================================
    def click_hide_info():
        items = display.get_children()

        for item in items:
            display.delete(item)

    #==============================================================BUTTON FOR GRADE CALCULATOR==================================================================================
    button_for_grade_calcu = Button(bg_for_student_data, 
                                    text="Grade Calculator", 
                                    padx=32, 
                                    font=(20), 
                                    bd=1, 
                                    bg='green',
                                    activebackground='green', 
                                    activeforeground='white', 
                                    fg='white', 
                                    cursor="hand2",
                                    command=go_to_calcu)
    button_for_grade_calcu.bind("<Enter>", hover_calcu_enter)
    button_for_grade_calcu.bind("<Leave>", hover_calcu_leave)
    button_for_grade_calcu.place(x=0, y=15, )
    #++============================================================ATTENDANCE TRACKER BUTTON=======================================================================================
    attendance_tracker_btn = Button(bg_for_student_data, 
                                    text="Attendance Tracker", 
                                    padx=25, 
                                    font=(20), 
                                    bd=1, 
                                    bg='green',
                                    activebackground='green', 
                                    activeforeground='white', 
                                    fg='white', 
                                    cursor="hand2",
                                    command=go_to_calcu)
    attendance_tracker_btn.bind("<Enter>", hover_attendance_tracker_enter)
    attendance_tracker_btn.bind("<Leave>", hover_attendace_tracker_leave)
    attendance_tracker_btn.place(x=0, y=242, )

    

    
    
    
    def announcement():
        root.destroy()
        for_announcement.announcement()
    #=============================================================BUTTON FOR ANNOUNCEMENT===========================================================================
    button_for_attendance_tracker = Button(bg_for_student_data, 
                                           text="Announcement", 
                                           padx=41, 
                                           font=(20), 
                                           bd=1, 
                                           bg='green',
                                           activebackground='green', 
                                           activeforeground='white', 
                                           fg='white', 
                                           cursor="hand2",
                                           command=announcement)
    button_for_attendance_tracker.bind("<Enter>", hover_attdnce_trcker_enter)
    button_for_attendance_tracker.bind("<Leave>", hover_attdnce_trcker_leave)
    button_for_attendance_tracker.place(x=0, y=145, )

    #===============================================================BUTTON FOR HIDE===========================================================================================
    button_for_help =  Button(bg_for_student_data, 
                              text="Hide Data", 
                              padx=57, font=(20), 
                              bd=1, bg='green',
                              activebackground='green', 
                              activeforeground='white', 
                              fg='white', 
                              cursor="hand2", 
                              command=click_hide_info)
    
    button_for_help.bind("<Enter>", hover_help_enter)
    button_for_help.bind("<Leave>", hover_help_leave)
    button_for_help.place(x=0, y=210, )

    #==================================================================SHOW DATA BUTTON==============================================================================================
    about_button =  Button(bg_for_student_data, 
                           text="Show Data", 
                           padx=55, 
                           font=(20), 
                           bd=1, 
                           bg='green',
                           activebackground='green', 
                           activeforeground='white', 
                           fg='white', cursor="hand2", 
                           command=click_showinfo)
    
    about_button.bind("<Enter>", hover_about_enter)
    about_button.bind("<Leave>", hover_about_leave)
    about_button.place(x=0, y=275, )


    #============================================================SCROLL BARS===========================================================================
    scrollbarY = Scrollbar(bg_for_student_data2, orient="vertical")
    scrollbarY.pack(fill=Y, side="right")

    scrollbarX = Scrollbar(bg_for_student_data2, orient="horizontal", bg='black')
    scrollbarX.pack(fill=X, side="bottom")


    #===========================================================================TREEVIEW=====================================================================================
   
    columns = ('student id', 'last name', 'given name', 'middle initial', 'age', 'number of presents','p1 grade', 'p2 grade', 'p3 grade', 'final grade')
    display = ttk.Treeview(bg_for_student_data2, columns=columns, show='headings',yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
    display.heading('student id', text='Student ID')
    display.heading('last name', text="Last Name")
    display.heading('given name', text='Given Name')
    display.heading('middle initial', text="Middle Initial")
    display.heading('age', text='Age')
    display.heading('number of presents', text = 'Total of presents')
    display.heading('p1 grade', text="P1 Grade")
    display.heading('p2 grade', text="P2 Grade")
    display.heading('p3 grade', text="P3 Grade")
    display.heading('final grade', text="Final Grade")
    
    
    display.column('student id', width=200, anchor='center')
    display.column('last name', width=150,anchor='center')
    display.column('given name', width=150,anchor='center')
    display.column('middle initial', width=150,anchor='center')
    display.column('number of presents', width=150,anchor='center')
    display.column('age', width=200,anchor='center')
    display.column('p1 grade', width=200,anchor='center')
    display.column('p2 grade', width=200,anchor='center')
    display.column('p3 grade', width=210,anchor='center')
    display.column('final grade', width=250, anchor='center')



    display.place(x=0, y =0)

    scrollbarY.config(command=display.yview)
    scrollbarX.config(command=display.xview)
    query = "SELECT student_id, l_name, g_name, m_initial, age, number_of_presents, p1_grade, p2_grade, p3_grade, final_grade FROM add_button ORDER BY l_name"
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        display.insert('', 'end', values=row)

    #===========================================================================================GRADE TRACKER=============================================================================
    columns = ('student id', 'p1 grade', 'p2 grade', 'p3 grade', 'final grade')
    grade_tracker = ttk.Treeview(bg_for_student_data2, columns=columns, show='headings',yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
    grade_tracker.heading('student id', text='Student ID')
    grade_tracker.heading('p1 grade', text="P1 Grade")
    grade_tracker.heading('p2 grade', text="P2 Grade")
    grade_tracker.heading('p3 grade', text="P3 Grade")
    grade_tracker.heading('final grade', text="Final Grade")

    grade_tracker.column('student id', width=350, anchor='center')
    grade_tracker.column('p1 grade', width=400, anchor='center')
    grade_tracker.column('p2 grade', width=400, anchor='center')
    grade_tracker.column('p3 grade', width=360, anchor='center')
    grade_tracker.column('final grade', width=350, anchor='center')

    grade_tracker.place(x=0, y=240, height=200)

    cursor = db.cursor()

    # Fetch data from multiple tables and compute final grades
    cursor.execute("SELECT for_p1.student_id, for_p1.P1_grade, for_p2.P2_grade, for_p3.P3_grade FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id")

    # Clear existing data in the grade_tracker Treeview
    grade_tracker.delete(*grade_tracker.get_children())

    for row_data in cursor.fetchall():
        student_id = row_data[0]
        p1_grade = float(row_data[1].rstrip('%')) if row_data[1] else None
        p2_grade = float(row_data[2].rstrip('%')) if row_data[2] else None
        p3_grade = float(row_data[3].rstrip('%')) if row_data[3] else None

        # Compute the final average for each row
        final_average = sum(grade for grade in [p1_grade, p2_grade, p3_grade] if grade is not None) / 3 if any(
            grade is not None for grade in [p1_grade, p2_grade, p3_grade]) else None

        # Insert combined data into the grade_tracker, mapping each piece of data to the respective column
        combined_data = (student_id, f"{p1_grade}%", f"{p2_grade}%", f"{p3_grade}%", f"{final_average:.2f}%" if final_average is not None else '')

        grade_tracker.insert('', 'end', values=combined_data)
    
    #==========================================================================ATTENDANCE TRACKER==================================================================================



    
    

    root.mainloop()
if __name__ == "__main__":
    database()