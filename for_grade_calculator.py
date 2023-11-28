from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import databasedesign
import mysql.connector
connector = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin', database = 'for_teacher_form')
cursor2 = connector.cursor() 
cursor3 =connector.cursor()
cursor4 = connector.cursor()


def init():

    root = Tk()
    root.title("Teach tech grade calculator")
    

    root.geometry("1000x1000")
    #============================================================================================TITLE============================================================================
    calculator_and_tracker = Label(root, text=f"GRADE CALCULATOR AND TRACKER", 
                                   font=("Helvitica", 20, 'bold'), 
                                   
                                   width=20,bg='#333333', 
                                   
                                   fg='white' ,
                                   
                                   bd=40,
                                   
                                   borderwidth=30, 
                                   
                                   relief=RIDGE, 
                                   
                                   padx=760)
    calculator_and_tracker.grid(row=0, column=1,  sticky=W)

    #================================================================================FRAME FOR SEARCH============================================================
    bg_for_search = Frame(root, 
                          
                          bg='#333333', 
                          
                          bd=20, 
                          
                          relief=RIDGE)
    bg_for_search.place(x=950, 
                        
                        y=100, 
                        
                        width=970, 
                        
                        height=900)
    #================================================================================FRAME FOR STUDENT GRADES======================================================================
    bg_for_student_data = Frame(root, 
                                
                                bg='#333333', 
                                
                                bd=20, 
                                
                                relief=RIDGE)
    label_for_grade_calcu = Label(bg_for_student_data, 
                                  
                                  text='Grade Calculator', 
                                  
                                  font=('Arial', 18, 'bold'), 
                                  
                                  fg='white', 
                                  
                                  bg='#333333')
    label_for_grade_calcu.pack()
    
    bg_for_student_data.place(x=0, 
                              
                              y=100, 
                              
                              width=936, 
                              
                              height=570)

    
    #===============================================================================FRAME FOR GRADE TRACKER===========================================================================
    bg_for_student_tracker = Frame(root, 
                                   
                                   bg='#333333', 
                                   
                                   bd=20, 
                                   
                                   relief=RIDGE)
    label_for_grade_tracker = Label(bg_for_student_tracker, 
                                    
                                    text='Grade Tracker', 
                                    
                                    font=('Arial', 18, 'bold'), 
                                    
                                    fg='white', 
                                    
                                    bg='#333333')
    label_for_grade_tracker.pack()
    bg_for_student_tracker.place(x=0, 
                                 
                                 y=650, 
                                 
                                 width=936, 
                                 
                                 height=370)
    #=================================================================================FRAME FOR ATTENDANCE TRACKER=====================================================================
    bg_for_attendance_tracker = Frame(root, 
                                      
                                      bg='#333333', 
                                      
                                      bd=20, 
                                      
                                      relief=RIDGE)
    bg_for_attendance_tracker.place(x=950, 
                                    
                                    y=650, 
                                    
                                    width=960, 
                                    
                                    height=350)
    #=================================================================================LABELS FOR GRADE CALCULATOR==================================================================
    student_id = Label(bg_for_student_data, 
                       
                       text="Student ID: ", 
                       
                       font=('arial', 14), 
                       
                       fg='white', 
                       
                       bg='#333333')
    student_id.place(x=0, y=80)

    activity = Label(bg_for_student_data, 
                     
                     text="Activities: ",
                     
                     font=('arial', 14), 
                     
                     fg='white', 
                     
                     bg='#333333')
    activity.place(x=0, y=140)

    exam = Label(bg_for_student_data, 
                 
                 text="Exam: ", 
                 
                 font=('arial', 14), 
                 
                 fg='white', 
                 
                 bg='#333333')
    exam.place(x=0, y=260)

    quiz = Label(bg_for_student_data, 
                 
                 text="Quiz: ", 
                 
                 font=('arial', 14), 
                 
                 fg='white', 
                 
                 bg='#333333')
    quiz.place(x=0, y=200)

    attendance = Label(bg_for_student_data, 
                       
                       text="Attendance: ", 
                       
                       font=('arial', 14), 
                       
                       fg='white', 
                       
                       bg='#333333')
    attendance.place(x=0, y=320)

    final_grade = Label (bg_for_student_data, 
                         
                         text="Final Grade: ", 
                         
                         font=('arial', 14), 
                         
                         fg='white', 
                         
                         bg='#333333')
    
    final_grade_result  = Label(bg_for_student_data, 
                                
                                text="0%", 
                                
                                font=('arial', 14), 
                                
                                fg='white', 
                                
                                bg='#333333' )
    final_grade_result.place(x=120, y=380)
    final_grade.place(x=0, y=380)

    #====================================================================================BACK FUNCTION=========================================================================
    def back():
        root.destroy()
        databasedesign.database()

    #======================================================================================HOVERR BUTTON==========================================================================
    def hover_enter(event):
       search_button.config(bg='white', fg='#333333', relief=SOLID)

    def hover_leave(event):
       search_button.config(bg='#333333', fg='white', relief='flat') 
    #====================================================================================PLACE HOLDER==============================================================================
    def placeholder(event):
       if search_entry.get()== "Enter your id...":
          search_entry.delete(0, END)
          search_entry.config(fg='black')
        
    def placeholder_leave(event):
       if not search_entry.get():
          search_entry.insert(0, "Enter your id...")
          search_entry.config(fg='grey')


    #===================================================================================CALCULATION===================================================================================
    def calculation():
        activities_str = (activity_entry.get())
        quizzes_str = quiz_entry.get()
        exams_str = exam_entry.get()
        attendance_to_str = attendance_entry.get()

        activities = float(activities_str.rstrip('%'))
        quizzes = float(quizzes_str.rstrip("%"))
        exams = float(exams_str)
        attendance_to = float(attendance_to_str.rstrip("%"))
        
        activities = (activities/15)*20
        quizzes = (quizzes/50)*30
        exams =  (exams/50)*40
        attendance_to = (attendance_to/5)*10

        sum = activities + quizzes + exams + attendance_to
        final_grade_result.config(text=f"{sum:.2f}%")


    
    
    #======================================================================================P1 ADD TO FUNCTION=======================================================================
     # Define cursor2 outside the function

    def add_p1():
        cursor = connector.cursor()
        query = ("INSERT INTO for_p1(student_id, P1_grade, activities, exam, quizzes, number_of_presents) VALUES(%s, %s, %s, %s, %s, %s)")
        data = (student_id_entry.get(), final_grade_result.cget("text"), activity_entry.get(),exam_entry.get(), quiz_entry.get(), attendance_entry.get())

        if final_grade_result == '0%':
            messagebox.showinfo("Calculate First", "Oops, you forgot to calculate")
        else:
            try:
                cursor.execute(query, data)
                connector.commit()
                messagebox.showinfo("Added", "Added successfully")
                student_id_entry.delete(0, 'end')
                final_grade_result.config(text="0%")
                activity_entry.delete(0, END)
                exam_entry.delete(0, END)
                quiz_entry.delete(0, END)
                attendance_entry.delete(0, END)

                cursor1 = connector.cursor()
                cursor1.execute("SELECT for_p1.student_id, for_p1.P1_grade, for_p2.P2_grade, for_p3.P3_grade FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id")

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

                    cursor3 = connector.cursor()

                    # Fetch data from multiple tables and compute final grades
                    cursor3.execute("SELECT for_p1.student_id, for_p1.number_of_presents, for_p2.number_of_presents, for_p3.number_of_presents FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id")

                    # Clear existing data in the grade_tracker Treeview
                    attendance_tracker.delete(*attendance_tracker.get_children())

                    for row_data in cursor3.fetchall():
                        student_id = row_data[0]
                        p1_attendance = int(row_data[1]) if row_data[1] else None
                        p2_attendance = int(row_data[2]) if row_data[2] else None
                        p3_attendace = int(row_data[3]) if row_data[3] else None

                        # Compute the final average for each row
                        final_attendance = sum(attendance for attendance in [p1_attendance, p2_attendance, p3_attendace] if attendance is not None) if any(
                            attendance is not None for attendance in [p1_attendance, p2_attendance, p3_attendace]) else None

                        # Insert combined data into the grade_tracker, mapping each piece of data to the respective column
                        combined_data2 = (student_id, f"{p1_attendance}", f"{p2_attendance}", f"{p3_attendace}", f"{final_attendance}" if final_attendance is not None else '')

                        attendance_tracker.insert('', 'end', values=combined_data2)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
            
        
    #======================================================================================P2 ADD TO FUNCTION=======================================================================
    def add_p2():
        cursor = connector.cursor()
        query = ("INSERT INTO for_p2(student_id, P2_grade, activities, exam, quizzes, number_of_presents) VALUES(%s, %s, %s, %s, %s, %s)")
        data = (student_id_entry.get(), final_grade_result.cget("text"), activity_entry.get(),exam_entry.get(), quiz_entry.get(), attendance_entry.get())
        try:
            cursor.execute(query, data)
            connector.commit()
            messagebox.showinfo("Added", "Added successfully")
            student_id_entry.delete(0, 'end')
            final_grade_result.config(text="0%")
            activity_entry.delete(0, END)
            exam_entry.delete(0, END)
            quiz_entry.delete(0, END)
            attendance_entry.delete(0, END)
            cursor1 = connector.cursor()
            cursor1.execute("SELECT for_p1.student_id, for_p1.P1_grade, for_p2.P2_grade, for_p3.P3_grade FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id")

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





            cursor2 = connector.cursor()

            # Fetch data from multiple tables and compute final grades
            cursor2.execute("SELECT for_p1.student_id, for_p1.number_of_presents, for_p2.number_of_presents, for_p3.number_of_presents FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id")

            # Clear existing data in the grade_tracker Treeview
            attendance_tracker.delete(*attendance_tracker.get_children())

            for row_data in cursor.fetchall():
                student_id = row_data[0]
                p1_attendance = int(row_data[1]) if row_data[1] else None
                p2_attendance = int(row_data[2]) if row_data[2] else None
                p3_attendace = int(row_data[3]) if row_data[3] else None

                # Compute the final average for each row
                final_attendance = sum(attendance for attendance in [p1_attendance, p2_attendance, p3_attendace] if attendance is not None) if any(
                    attendance is not None for attendance in [p1_attendance, p2_attendance, p3_attendace]) else None

                    # Insert combined data into the grade_tracker, mapping each piece of data to the respective column
                combined_data2 = (student_id, f"{p1_attendance}", f"{p2_attendance}", f"{p3_attendace}", f"{final_attendance}" if final_attendance is not None else '')

                attendance_tracker.insert('', 'end', values=combined_data2)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
           
    #======================================================================================P3 ADD TO FUNCTION=======================================================================
    def add_p3():
        
        cursor = connector.cursor()
        query = ("INSERT INTO for_p3(student_id, P3_grade, activities, exam, quizzes, number_of_presents) VALUES(%s, %s, %s, %s, %s, %s)")
        data = (student_id_entry.get(), final_grade_result.cget("text"), activity_entry.get(),exam_entry.get(), quiz_entry.get(), attendance_entry.get())
        
        try:
            cursor.execute(query, data)
            connector.commit()
            messagebox.showinfo("Added", "Added successfully")
            student_id_entry.delete(0, 'end')
            final_grade_result.config(text="0%")
            activity_entry.delete(0, END)
            exam_entry.delete(0, END)
            quiz_entry.delete(0, END)
            attendance_entry.delete(0, END)
            
            
            cursor1 = connector.cursor()
            cursor1.execute("SELECT for_p1.student_id, for_p1.P1_grade, for_p2.P2_grade, for_p3.P3_grade FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id")

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

                cursor = connector.cursor()

                # Fetch data from multiple tables and compute final grades
                cursor.execute("SELECT for_p1.student_id, for_p1.number_of_presents, for_p2.number_of_presents, for_p3.number_of_presents FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id")

                    # Clear existing data in the grade_tracker Treeview
                attendance_tracker.delete(*attendance_tracker.get_children())

                for row_data in cursor.fetchall():
                    student_id = row_data[0]
                    p1_attendance = int(row_data[1]) if row_data[1] else None
                    p2_attendance = int(row_data[2]) if row_data[2] else None
                    p3_attendace = int(row_data[3]) if row_data[3] else None

                    # Compute the final average for each row
                    final_attendance = sum(attendance for attendance in [p1_attendance, p2_attendance, p3_attendace] if attendance is not None) if any(
                        attendance is not None for attendance in [p1_attendance, p2_attendance, p3_attendace]) else None

                    # Insert combined data into the grade_tracker, mapping each piece of data to the respective column
                    combined_data2 = (student_id, f"{p1_attendance}", f"{p2_attendance}", f"{p3_attendace}", f"{final_attendance}" if final_attendance is not None else '')

                    attendance_tracker.insert('', 'end', values=combined_data2)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        
        
    
    #=========================================================================================REFRESH DATA============================================================================
    def specific_delete():
        selected_item = grade_tracker.selection()
        selected_attendance = attendance_tracker.selection()  # Get the selected item in the Treeview
        if selected_item and selected_attendance:  # Check if an item is selected
            selected_id = grade_tracker.item(selected_item, "values")[0]  # Assuming the ID is the first column
            selected_id1 = attendance_tracker.item(selected_attendance, "values")[0]
            if selected_id and selected_id1:  # Check if an ID is retrieved
                confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?")
                if confirmation:
                    try:
                        cursor = connector.cursor()
                        # Assuming 'for_p1' is the table name and 'student_id' is the primary key column
                        cursor.execute("DELETE FROM for_p1 WHERE student_id = %s", (selected_id,))
                        cursor.execute("DELETE FROM for_p2 WHERE student_id = %s", (selected_id,))
                        cursor.execute("DELETE FROM for_p3 WHERE student_id = %s", (selected_id,))
                        connector.commit()
                        messagebox.showinfo("Deleted", "Record deleted successfully!")

                        # Delete the selected item from the Treeview
                        grade_tracker.delete(selected_item)
                        attendance_tracker.delete(selected_attendance)
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
            else:
                messagebox.showinfo("No ID", "No ID found for the selected item.")
        else:
            messagebox.showinfo("No Selection", "Please select an item to delete.")

        
    #====================================================================================SEARCH BUTTON FUNCTION======================================================================
    def search():
        searchh = search_entry.get()

        cursor = connector.cursor()

        # Fetch data from for_p1 table
        cursor.execute("SELECT student_id, P1_grade FROM for_p1 WHERE student_id = %s", (searchh,))
        data_p1 = cursor.fetchone()

        # Fetch data from for_p2 table
        cursor.execute("SELECT student_id, P2_grade FROM for_p2 WHERE student_id = %s", (searchh,))
        data_p2 = cursor.fetchone()

        # Fetch data from for_p3 table
        cursor.execute("SELECT student_id, P3_grade FROM for_p3 WHERE student_id = %s", (searchh,))
        data_p3 = cursor.fetchone()
        # Fetch data from multiple tables and compute final grades
        cursor.execute("SELECT for_p1.student_id, for_p1.number_of_presents, for_p2.number_of_presents, for_p3.number_of_presents FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id WHERE for_p1.student_id = %s", (searchh,))
         # Clear existing data in the grade_tracker Treeview
        attendance_tracker.delete(*attendance_tracker.get_children())

        for row_data in cursor.fetchall():
            student_id = row_data[0]
            p1_attendance = int(row_data[1]) if row_data[1] else None
            p2_attendance = int(row_data[2]) if row_data[2] else None
            p3_attendace = int(row_data[3]) if row_data[3] else None

               
       
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
             # Clear existing data in the grade_tracker Treeview
            grade_tracker.delete(*grade_tracker.get_children())
            grade_tracker.insert('', 'end', values=combined_data)

             # Compute the final average for each row
            final_attendance = sum(attendance for attendance in [p1_attendance, p2_attendance, p3_attendace] if attendance is not None) if any(
                    attendance is not None for attendance in [p1_attendance, p2_attendance, p3_attendace]) else None

                # Insert combined data into the grade_tracker, mapping each piece of data to the respective column
            combined_data2 = (student_id, f"{p1_attendance}", f"{p2_attendance}", f"{p3_attendace}", f"{final_attendance}" if final_attendance is not None else '')

            attendance_tracker.insert('', 'end', values=combined_data2)
            


        else:
            messagebox.showinfo("No Data", "No data found for the given student ID.")


    #================================================================================================DELETE FUNCTION===================================================================
    def delete():
        delete_confirmation = messagebox.askyesno("Delete Data", "Are you sure you want to delete all of these data?")
        if delete_confirmation:
            messagebox.showinfo("Deleted", "Deleted Successfully!")
            try:
                cursor2 = connector.cursor()
                cursor2.execute("DELETE FROM for_p1")
                cursor2.execute("DELETE FROM for_p2")
                cursor2.execute("DELETE FROM for_p3")

                # Commit the changes to the database
                connector.commit()

                # Clear data in the grade_tracker widget
                items = grade_tracker.get_children()
                for row in items:
                    grade_tracker.delete(row)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")


  #=====================================================================================HOVER FOR P1=========================================================================
    def p1_enter(event):
        p1.config(bg='darkgreen', 
                  
                  bd=1, 
                
                  fg='white', 
                  
                  relief=SOLID)

    
    def p1_leave(event):
        p1.config(bg='green', 
                  
                  fg='white', 
                  
                  relief=FLAT, 
                  
                  bd=1)
    
     #=====================================================================================HOVER FOR P2========================================================================
    def p2_enter(event):
        p2.config(bg='darkgreen', 
                  
                  bd=1, 
                  
                  fg='white', 
                  
                  relief=SOLID)

    
    def p2_leave(event):
        p2.config(bg='green', 
                  
                  fg='white', 
                  
                  relief=FLAT, 
                  
                  bd=1)
    #=====================================================================================HOVER FOR P3========================================================================
    def p3_enter(event):
        p3.config(bg='darkgreen', 
                  
                  bd=1, 
                  
                  fg='white', 
                  
                  relief=SOLID)

    
    def p3_leave(event):
        p3.config(bg='green', 
                  
                  fg='white', 
                  
                  relief=FLAT, 
                  
                  bd=1)
        
        

    #====================================================================================HOVER TO CALCULATE===========================================================================
    def calculatee(event):
        calculate.config(bg='darkgreen', 
                         
                         bd=1, 
                         
                         fg='white', 
                         
                         relief='solid')
    
    def calculatee_leave(event):
        calculate.config(bg='green',
                         
                         fg='white', 
                         
                         relief='flat')

    #====================================================================================HOVER FOR BACK===============================================================================
    def back_button_enter(event):
        back_to_records.config(bg='darkgreen', 
                               
                               bd=1, 
                               
                               fg='white', 
                               
                               relief='solid')

    def back_button_leave(event):
        back_to_records.config(bg='green', 
                               
                               fg='white', 
                               
                               relief='flat')

     #====================================================================================HOVER FOR REFRESH===============================================================================
    def refresh_button_enter(event):
        refresh_button.config(bg='darkgreen', 
                              
                              bd=1, fg='white', 
                              
                              relief='solid')

    def refresh_button_leave(event):
        refresh_button.config(bg='green', 
                              
                              fg='white', 
                              
                              relief='flat')


     #====================================================================================HOVER FOR REFRESH===============================================================================
    def delete_button_enter(event):
        delete_button.config(bg='darkgreen', 
                             
                             bd=1, fg='white', 
                             
                             relief='solid')

    def delete_button_leave(event):
        delete_button.config(bg='green', 
                             
                             fg='white', 
                             
                             relief='flat')

    
   




    #====================================================================================ENTRIES=======================================================================================
    student_id_entry = Entry(bg_for_student_data, 
                             
                             width=30, 
                             
                             font=('arial', 14))
    student_id_entry.place(x=170, y=80)

    activity_entry = Entry(bg_for_student_data, 
                           
                           width=30, 
                           
                           font=('arial', 14))
    activity_entry.place(x=170, y=140)

    quiz_entry = Entry(bg_for_student_data, 
                       
                       width=30, 
                       
                       font=('arial', 14))
    quiz_entry.place(x=170, y=200)

    exam_entry= Entry(bg_for_student_data, 
                      
                      width=30, 
                      
                      font=('arial', 14))
    exam_entry.place(x=170, y=260)

    attendance_entry = Entry(bg_for_student_data, 
                             
                             width=30, 
                             
                             font=('arial', 14))
    attendance_entry.place(x=170, y=320)

    


    #===================================================================================BUTTON FOR  CALCULATE===========================================================================
    calculate = Button(bg_for_student_data, 
                       
                       text='Calculate', 
                       
                       bg='green', 
                       
                       fg='white', 
                       
                       font=('arial', 12, 'bold'), 
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       bd=0, 
                       
                       width=20,
                       
                       cursor='hand2',
                       command=calculation)
    calculate.bind("<Enter>", calculatee)
    calculate.bind("<Leave>", calculatee_leave)
    
    calculate.place(x=0, y=480)



    #=======================================================================================BUTTON FOR ADD TO P1=======================================================================
    p1 = Button(bg_for_student_data, 
                       
                       text='Add to P1', 
                       
                       bg='green', 
                       
                       fg='white', 
                       
                       font=('arial', 12, 'bold'), 
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       bd=0, 
                       
                      

                       width=20,
                       
                       cursor='hand2',
                       command=add_p1)
    p1.bind("<Enter>", p1_enter)
    p1.bind("<Leave>", p1_leave)
    
    p1.place(x=230, y=480)

     #=======================================================================================BUTTON FOR ADD TO P2=======================================================================
    p2 = Button(bg_for_student_data, 
                       
                       text='Add to P2', 
                       
                       bg='green', 
                       
                       fg='white', 
                       
                       font=('arial', 12, 'bold'), 
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       bd=0, 
                       
                       width=20,

                    
                       
                       cursor='hand2',
                       command=add_p2)
    p2.bind("<Enter>", p2_enter)
    p2.bind("<Leave>", p2_leave)
    
    p2.place(x=460, y=480)

    #=======================================================================================BUTTON FOR ADD TO P3=======================================================================
    p3 = Button(bg_for_student_data, 
                       
                       text='Add to P3', 
                       
                       bg='green', 
                       
                       fg='white', 
                       
                       font=('arial', 12, 'bold'), 
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       bd=0, 
                       
                       width=20,

                     
                       
                       cursor='hand2',
                       command=add_p3)
    p3.bind("<Enter>", p3_enter)
    p3.bind("<Leave>", p3_leave)
    p3.place(x=690, y=480)
    #=================================================================================================REFRESH==================================================================
    refresh_button = Button(bg_for_student_data, 
                       
                       text='Delete Row', 
                       
                       bg='green', 
                       
                       fg='white', 
                       
                       font=('arial', 12, 'bold'), 
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       bd=0, 
                       
                       width=20,
                       cursor='hand2',
                       
                       command=specific_delete)
    refresh_button.bind("<Enter>", refresh_button_enter)
    refresh_button.bind("<Leave>", refresh_button_leave)
    
    refresh_button.place(x=459, y=430)
    #=================================================================================================DELETE==================================================================
    delete_button = Button(bg_for_student_data, 
                       
                       text='Delete all', 
                       
                       bg='green', 
                       
                       fg='white', 
                       
                       font=('arial', 12, 'bold'), 
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       bd=0, 
                       
                       width=20,
                       cursor='hand2',
                       
                       command=delete)
    delete_button.bind("<Enter>", delete_button_enter)
    delete_button.bind("<Leave>", delete_button_leave)
    
    delete_button.place(x=230, y=430)

    #=======================================================================================BUTTON FOR BACK=======================================================================
    back_to_records = Button(bg_for_student_data, 
                       
                       text='Back', 
                       
                       bg='green', 
                       
                       fg='white', 
                       
                       font=('arial', 12, 'bold'), 
                       
                       activebackground='green', 
                       
                       activeforeground='white', 
                       
                       bd=0, 
                       
                       width=20,

                      
                       
                       cursor='hand2',
                       
                       command=back)
    back_to_records.bind("<Enter>", back_button_enter)
    back_to_records.bind("<Leave>", back_button_leave)
    
    back_to_records.place(x=690, y=430)
    #============================================================================================SEARCH================================================================================
    search_entry =  Entry(bg_for_search, width=84, font=("helvitica", 12), fg='grey')
    search_entry.insert(0,"Enter your id...")
    search_entry.bind('<FocusIn>', placeholder)
    search_entry.bind('<FocusOut>', placeholder_leave)
    search_entry.bind("<Return>", lambda event: search())
    
    search_entry.place(x=90, y=5)

    #================================================================================================SEARCH BUTTON====================================================================
    search_button =  Button(bg_for_search, 
                            font=('calibri', 14, 'bold'), 
                            bg='#333333', 
                            fg='white', 
                            bd=0,
                            pady=0, 
                            activeforeground='white', 
                            activebackground='#333333', 
                            text="Search", 
                            cursor="hand2",
                            command=search
                            )
    
    search_button.bind("<Enter>", hover_enter)
    search_button.bind("<Leave>", hover_leave)
    
    search_button.place(x=0, y=0)

    #================================================================================================SCROLLBARS========================================================================
    scrollY = Scrollbar(bg_for_student_tracker, orient='vertical', )
    scrollY.pack(side='right', fill='y')

    scrollX = Scrollbar(bg_for_student_tracker, orient='horizontal')
    scrollX.pack(side='bottom', fill='x')
    #===========================================================================================GRADE TRACKER=============================================================================
    columns = ('student id', 'p1 grade', 'p2 grade', 'p3 grade', 'final grade')
    grade_tracker = ttk.Treeview(bg_for_student_tracker, columns=columns, show='headings',yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)
    grade_tracker.heading('student id', text='Student ID')
    grade_tracker.heading('p1 grade', text="P1 Grade")
    grade_tracker.heading('p2 grade', text="P2 Grade")
    grade_tracker.heading('p3 grade', text="P3 Grade")
    grade_tracker.heading('final grade', text="Final Grade")

    grade_tracker.column('student id', width=126, anchor='center')
    grade_tracker.column('p1 grade', width=150, anchor='center')
    grade_tracker.column('p2 grade', width=200, anchor='center')
    grade_tracker.column('p3 grade', width=200, anchor='center')
    grade_tracker.column('final grade', width=200, anchor='center')

    grade_tracker.place(x=0, y=35, height=280)
    cursor = connector.cursor()

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








        #================================================================================================SCROLLBARS========================================================================
    scrollbarY = Scrollbar(bg_for_attendance_tracker, orient='vertical', )
    scrollbarY.pack(side='right', fill='y')

    scrollbarX = Scrollbar(bg_for_attendance_tracker, orient='horizontal')
    scrollbarX.pack(side='bottom', fill='x')
    #===========================================================================================Attendance TRACKER=============================================================================
    attendance_tracker_label = Label(bg_for_attendance_tracker, text="Attendance Tracker", bd='0', font=("Arial", 18, 'bold'), bg='#333333', fg='white')
    attendance_tracker_label.pack()
    
    columns = ('student id', 'p1 attendance', 'p2 attendance', 'p3 attendance', 'total attendance')
    attendance_tracker = ttk.Treeview(bg_for_attendance_tracker, columns=columns, show='headings',yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
    attendance_tracker.heading('student id', text='Student ID')
    attendance_tracker.heading('p1 attendance', text="P1 Attendance")
    attendance_tracker.heading('p2 attendance', text="P2 Attendance")
    attendance_tracker.heading('p3 attendance', text="P3 Attendance")
    attendance_tracker.heading('total attendance', text="Total Attendance")

    attendance_tracker.column('student id', width=140, anchor='center')
    attendance_tracker.column('p1 attendance', width=160, anchor='center')
    attendance_tracker.column('p2 attendance', width=200, anchor='center')
    attendance_tracker.column('p3 attendance', width=200, anchor='center')
    attendance_tracker.column('total attendance', width=200, anchor='center')

    attendance_tracker.place(x=0, y=35, height=257)
    cursor = connector.cursor()

    # Fetch data from multiple tables and compute final grades
    cursor.execute("SELECT for_p1.student_id, for_p1.number_of_presents, for_p2.number_of_presents, for_p3.number_of_presents FROM for_p1 LEFT JOIN for_p2 ON for_p1.student_id = for_p2.student_id LEFT JOIN for_p3 ON for_p1.student_id = for_p3.student_id")

    # Clear existing data in the grade_tracker Treeview
    attendance_tracker.delete(*attendance_tracker.get_children())

    for row_data in cursor.fetchall():
        student_id = row_data[0]
        p1_attendance = int(row_data[1]) if row_data[1] else None
        p2_attendance = int(row_data[2]) if row_data[2] else None
        p3_attendace = int(row_data[3]) if row_data[3] else None

        # Compute the final average for each row
        final_attendance = sum(attendance for attendance in [p1_attendance, p2_attendance, p3_attendace] if attendance is not None) if any(
            attendance is not None for attendance in [p1_attendance, p2_attendance, p3_attendace]) else None

        # Insert combined data into the grade_tracker, mapping each piece of data to the respective column
        combined_data2 = (student_id, f"{p1_attendance}", f"{p2_attendance}", f"{p3_attendace}", f"{final_attendance}" if final_attendance is not None else '')

        attendance_tracker.insert('', 'end', values=combined_data2)
        
    root.mainloop()



if __name__=="__main__":
    init()


    