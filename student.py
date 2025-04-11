from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
        
        # textvariables
        self.var_student_id = StringVar()
        self.var_dept = StringVar()
        self.var_semester = StringVar()
        self.var_Subject = StringVar()
        self.var_reg = StringVar()
        self.var_name = StringVar()
        self.var_DOB=StringVar()
        self.var_phone = StringVar()
        
        
        
        

        # Top Images
        img1 = Image.open("C:\\python projects\\attendance system\\images\\students_1.jpg").resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)
        
        img2 = Image.open("C:\\python projects\\attendance system\\images\\students_2.jpg").resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=500, y=0, width=514, height=130)
        
        img3 = Image.open("C:\\python projects\\attendance system\\images\\students_3.jpg").resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=525, height=130)

        # Background Image
        img4 = Image.open("C:\\python projects\\attendance system\\images\\bg_image.jpg").resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=55, width=1500, height=600)

        # Left Frame for Student Details
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=780, height=580)

        img_left = Image.open("C:\\python projects\\attendance system\\images\\ITGPC.jpg").resize((770, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=5, y=0, width=770, height=130)
        
        # Current Course Information
        current_course = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course.place(x=5, y=135, width=770, height=150)

        # Department Label and Combobox
        Label(current_course, text="Department", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course,textvariable=self.var_dept, font=("times new roman", 12, "bold"), state="readonly", width=17)
        dep_combo["values"] = ("Select Department", "C.S.T.", "E.E.", "E.T.C.E")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Semester Label and Combobox
        Label(current_course,text="Semester", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, sticky=W)
        sem_combo = ttk.Combobox(current_course,textvariable=self.var_semester,font=("times new roman", 12, "bold"), state="readonly", width=17)
        sem_combo["values"] = ("Select Semester", "Semester 3", "Semester 4", "Semester 5")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        

        # Subject Label and Combobox
        Label(current_course, text="Subjects", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, sticky=W)
        sub_combo = ttk.Combobox(current_course,textvariable=self.var_Subject, font=("times new roman", 12, "bold"), state="readonly", width=17)
        sub_combo["values"] = ("Select Subject",)
        sub_combo.current(0)
        sub_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)
        
        # Student ID
        std_ID = Label(current_course,text="Student ID:",font=("times new roman", 12, "bold"), bg="white")
        std_ID.grid(row=0, column=2, padx=10, pady=5,sticky=W)
        
        std_style_ID=ttk.Entry(current_course,textvariable=self.var_student_id,font=("times new roman", 12, "bold"))
        std_style_ID.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        # Function to update subjects based on department and semester selection
        def update_subjects(event=None):
            department = dep_combo.get()
            semester = sem_combo.get()
            if department == "C.S.T.":
                if semester == "Semester 3":
                    sub_combo["values"] = ("Select Subject", "Python", "Data Structure", "C programming", "CSO", "Algorithm")
                elif semester == "Semester 4":
                    sub_combo["values"] = ("Select Subject", "Operating Systems", "OOP in Java", "Computer Networks", "Software Engineering", "Introduction to DBMS")
                elif semester == "Semester 5":
                    sub_combo["values"] = ("Select Subject", "Theory of Automata", "IoT", "Computer Graphics", "Mobile Computing", "Microprocessor and Microcontroller")
                else:
                    sub_combo["values"] = ("Select Subject",)
            else:
                sub_combo["values"] = ("Select Subject",)
            sub_combo.current(0)

        # Bind the update_subjects function to department and semester dropdowns
        dep_combo.bind("<<ComboboxSelected>>", update_subjects)
        sem_combo.bind("<<ComboboxSelected>>", update_subjects)

        # Class Student Information
        class_student = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student.place(x=5, y=290, width=770, height=260)
        
        std_name = Label(class_student,text="Student Name:",font=("times new roman", 12, "bold"), bg="white")
        std_name.grid(row=0, column=0, padx=10, pady=5,sticky=W)
        
        std_style_name=ttk.Entry(class_student,textvariable=self.var_name,font=("times new roman", 12, "bold"))
        std_style_name.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        std_DOB = Label(class_student,text="Student DOB:",font=("times new roman", 12, "bold"), bg="white")
        std_DOB.grid(row=0, column=2, padx=10, pady=5,sticky=W)
        
        std_style_DOB=ttk.Entry(class_student,textvariable=self.var_DOB,font=("times new roman", 12, "bold"))
        std_style_DOB.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        std_reg = Label(class_student,text="Registration No. :",font=("times new roman", 12, "bold"), bg="white")
        std_reg.grid(row=1, column=0, padx=10, pady=5,sticky=W)
        
        std_style_reg=ttk.Entry(class_student,textvariable=self.var_reg,font=("times new roman", 12, "bold"))
        std_style_reg.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        
        std_phn=Label(class_student,text="Phone No. : ",font=("times new roman", 12, "bold"), bg="white")
        std_phn.grid(row=1, column=2, padx=10, pady=5,sticky=W)
        
        std_style_phn=ttk.Entry(class_student,textvariable=self.var_phone,font=("times new roman", 12, "bold"))
        std_style_phn.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        
        
        
        

        # Radio Buttons for Photo Sample
        self.photo_sample= StringVar()
        
        take_photo_radio = ttk.Radiobutton(class_student,variable=self.photo_sample, text="Take Photo Sample",  value="Yes")
        take_photo_radio.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        
        no_photo_radio = ttk.Radiobutton(class_student, variable=self.photo_sample,text="No Photo Sample",  value="No")
        no_photo_radio.grid(row=3, column=1, padx=10, pady=10, sticky=W)
        
        
        
        # Buttons Frame in class_student section
        btn_frame = Frame(class_student, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=150, width=715, height=70)  # Adjusted the y-coordinate to reduce the space above

        save_btn = Button(btn_frame, text="Save", command=self.add_data,width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data,width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Separate Frame for Take Photo Sample Button
        
        photo_btn_frame = Frame(class_student, bd=2, bg="white", relief=RIDGE)
        photo_btn_frame.place(x=0, y=200, width=715, height=35)  # Adjusted the y-coordinate to align better with other components
        
        # take_photo_btn = Button(photo_btn_frame,command=self.generate_images_for_selected_student, text="Take Photo Sample", width=16, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        # take_photo_btn.grid(row=0, column=0)
        
        update_photo_btn = Button(photo_btn_frame,command=self.generate_images_for_selected_student, text="Update Photo Sample", width=39, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)
        
        generate_images_btn = Button(photo_btn_frame, command=self.generate_images_for_selected_student, text="Generate Images by ID", width=39, font=("times new roman", 12, "bold"), bg="green", fg="white")
        generate_images_btn.grid(row=0, column=0)
        
        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=730, height=580)
        
        img_right = Image.open("C:\\python projects\\attendance system\\images\\right_frame.webp").resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(right_frame, image=self.photoimg_right).place(x=5, y=0, width=720, height=130)
        
        
        # Searching System
        search_student = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_student.place(x=5, y=135, width=710, height=70)

        # "Search By:" Label
        Label(search_student, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white", width=10, anchor="w").grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Dropdown for search criteria
        search_combo = ttk.Combobox(search_student, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Department", "Name", "Semester", "Subject", "reg_no", "DOB", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Entry box for search input
        search_entry = ttk.Entry(search_student, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        # "Search" button
        search_btn = Button(search_student, text="Search", width=11, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        # "Show All" button
        showALL_btn = Button(search_student, text="Show All", width=11, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showALL_btn.grid(row=0, column=4, padx=4)

        
        
        # Table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        # Scroll bars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Treeview setup with columns
        self.student_table = ttk.Treeview(
            table_frame,
            columns=("student_id", "dept", "sem", "Subject", "name", "dob", "reg_no", "phn", "photo_sample"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
            )

        # Configure scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Define headings
        self.student_table.heading("student_id", text="Student ID")
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("Subject", text="Subject")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("reg_no", text="Registration no.")
        self.student_table.heading("phn",text="Phone No.")
        self.student_table.heading("photo_sample",text="photo_sample")
        

        # Display only the headings
        self.student_table['show'] = 'headings'

        # Set column widths
        self.student_table.column("student_id", width=100)
        self.student_table.column("dept", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("Subject", width=150)
        self.student_table.column("name", width=150)
        self.student_table.column("dob", width=100)
        self.student_table.column("reg_no", width=150)
        self.student_table.column("phn", width=170)
        self.student_table.column("photo_sample",width=150)


        # Pack the table to expand within the frame
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        # function declaration
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_reg.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",
                                            username="root",
                                            password="Ayush1980",
                                            database="face_attendance")
                my_cursor=conn.cursor()
                
                # Check if the table is empty and reset AUTO_INCREMENT if it is
                my_cursor.execute("SELECT COUNT(*) FROM student")
                count = my_cursor.fetchone()[0]
                if count == 0:
                    my_cursor.execute("ALTER TABLE student AUTO_INCREMENT = 1")
                    conn.commit()
                
                
                my_cursor.execute("INSERT INTO student (dept, semester, subject, name, dob, reg_no, phone, photo_sample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                                                                
                                                                                                                                                
                                                                                                                                                self.var_dept.get(),
                                                                                                                                                self.var_semester.get(),
                                                                                                                                                self.var_Subject.get(),
                                                                                                                                                self.var_name.get(),
                                                                                                                                                self.var_DOB.get(),
                                                                                                                                                self.var_reg.get(),
                                                                                                                                                self.var_phone.get(),
                                                                                                                                                self.photo_sample.get()
                                                                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error Due To : {str(es)}",parent=self.root)
                
                
    # fetching data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",
                                            username="root",
                                            password="Ayush1980",
                                            database="face_attendance")
        my_cursor=conn.cursor()
        my_cursor.execute("select  * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END,values=i)
                conn.commit()
            conn.close()
            
            
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_student_id.set(data[0]),
        self.var_dept.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_Subject.set(data[3]),
        self.var_name.set(data[4]),
        self.var_DOB.set(data[5]),
        self.var_reg.set(data[6]),
        self.var_phone.set(data[7]),
        self.photo_sample.set(data[8])
            
            
    # update function
    def update_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_reg.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",
                                            username="root",
                                            password="Ayush1980",
                                            database="face_attendance")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET dept=%s, subject=%s, semester=%s, name=%s, dob=%s, phone=%s, photo_sample=%s WHERE `reg_no`=%s",
                    (
                        self.var_dept.get(),
                        self.var_Subject.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_DOB.get(),
                        self.var_phone.get(),
                        self.photo_sample.get(),
                        self.var_reg.get(),
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("success","student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"dues to : {str(es)}",parent=self.root)
                
    # delete function
    def delete_data(self):
        if self.var_reg.get()=="":
            messagebox.showerror("Error","Please select student registration number",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",
                                            username="root",
                                            password="Ayush1980",
                                            database="face_attendance")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"dues to : {str(es)}",parent=self.root)
            
    # reset function
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_semester.set("Select Semester")
        self.var_Subject.set("Select  Subject")
        self.var_name.set("")
        self.var_DOB.set("")
        self.var_reg.set("")
        self.var_phone.set("")
        self.photo_sample.set("")
        
            
            
            
            
    def generate_images_for_selected_student(self):
        if self.var_student_id.get() == "" or not self.var_reg.get():
            messagebox.showerror("Error", "Please select a student record first", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Ayush1980",
                    database="face_attendance"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (self.var_student_id.get(),))
                student_data = my_cursor.fetchone()
                conn.close()

                if not student_data:
                    messagebox.showerror("Error", "No student record found for the given ID", parent=self.root)
                    return

                # Load pre-defined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        extra_padding = 39  # Adjust padding as needed
                        x = max(x - extra_padding, 0)
                        y = max(y - extra_padding, 0)
                        w = min(w + 2 * extra_padding, img.shape[1] - x)
                        h = min(h + 2 * extra_padding, img.shape[0] - y)
                        return img[y:y + h, x:x + w]

                cap = cv2.VideoCapture(0)
                img_id = 0
                student_id = self.var_student_id.get()  # Use student ID from selected record
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        # Use Student ID to generate filenames
                        file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

                        # Display the image
                        cv2.namedWindow("Face Cropper", cv2.WINDOW_NORMAL)
                        cv2.resizeWindow("Face Cropper", 800, 600)
                        cv2.imshow("Face Cropper", face)

                    if cv2.waitKey(1) == 13 or img_id == 35:  # Stop after 100 images or pressing Enter
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Image generation for selected student completed successfully!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
