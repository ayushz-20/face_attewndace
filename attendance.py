from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

        # Text variables
        self.var_student_id = StringVar()
        self.var_dept = StringVar()
        self.var_name = StringVar()
        self.var_reg_no = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_semester = StringVar()
        self.var_subject = StringVar()
        self.var_status = StringVar()

        # Top Images
        img1 = Image.open("images\\students_1.jpg").resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=500, height=130)

        img2 = Image.open("images\\students_2.jpg").resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=500, y=0, width=514, height=130)

        img3 = Image.open("images\\students_3.jpg").resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimg3).place(x=1000, y=0, width=525, height=130)

        # Background Image
        img4 = Image.open("images\\bg_image.jpg").resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=55, width=1500, height=600)

        # Left Frame for Student Attendance Details
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 14, "bold")
        )
        left_frame.place(x=10, y=10, width=780, height=580)

        img_left = Image.open("images\\ITGPC.jpg").resize((770, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=5, y=0, width=770, height=130)

        left_inside_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Attendance Details",
            font=("times new roman", 14, "bold")
        )
        left_inside_frame.place(x=10, y=135, width=700, height=370)

        # Labels and entry fields
        labels = [
            ("Attendance ID:", self.var_student_id, 0, 0),
            ("Name:", self.var_name, 0, 2),
            ("Department:", self.var_dept, 1, 0),
            ("Reg_no:", self.var_reg_no, 1, 2),
            ("Date:", self.var_date, 2, 0),
            ("Time:", self.var_time, 2, 2),
            ("Subject:", self.var_subject, 3, 2)
        ]

        for text, var, row, col in labels:
            Label(left_inside_frame, text=text, font=("times new roman", 14, "bold"), bg="white").grid(row=row, column=col, padx=10, pady=5, sticky=W)
            ttk.Entry(left_inside_frame, textvariable=var, font=("times new roman", 14, "bold")).grid(row=row, column=col+1, padx=5, pady=5, sticky=W)

        # ComboBoxes
        sem_combo = ttk.Combobox(
            left_inside_frame,
            textvariable=self.var_semester,
            font=("times new roman", 12, "bold"),
            state="readonly",
            width=17
        )
        sem_combo["values"] = ("3rd Semester", "4th Semester", "5th Semester")
        sem_combo.current(0)
        sem_combo.grid(row=4, column=1, padx=2, pady=10, sticky=W)

        status_combo = ttk.Combobox(
            left_inside_frame,
            textvariable=self.var_status,
            font=("times new roman", 12, "bold"),
            state="readonly",
            width=17
        )
        status_combo["values"] = ("Status", "Present", "Absent")
        status_combo.current(0)
        status_combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # Buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=300, width=698, height=35)

        Button(btn_frame, text="Import CSV", command=self.importCSV, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export CSV", command=self.exportCSV, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Update", command=self.update_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        # Right Frame for Attendance Details
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 14, "bold"))
        right_frame.place(x=750, y=10, width=730, height=580)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=0, width=710, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            columns=("Student_id", "name", "dept", "reg_no", "date", "time", "semester", "subject", "status"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Student_id", text="Attendance ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("reg_no", text="Reg_no")
        self.student_table.heading("date", text="Date")
        self.student_table.heading("time", text="Time")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("subject", text="Subject")
        self.student_table.heading("status", text="Status")
        self.student_table["show"] = "headings"
        self.student_table.column("Student_id", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("dept", width=100)
        self.student_table.column("reg_no", width=100)
        self.student_table.column("date", width=170)
        self.student_table.column("time", width=150)
        self.student_table.column("semester", width=90)
        self.student_table.column("subject", width=170)
        self.student_table.column("status", width=120)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

    def fetchData(self, rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("", END, values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=[("CSV File", "*.csv"), ("ALL Files", "*.*")]
        )
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCSV(self):
        try:
            rows = self.student_table.get_children()
            if len(rows) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=[("CSV File", "*.csv"), ("ALL Files", "*.*")],
                parent=self.root
            )
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                
                # Write column headers
                headers = ("Attendance ID", "Name", "Department", "Reg_no", "Date", "Time", "Semester", "Subject", "Status")
                exp_write.writerow(headers)
                
                # Write all rows
                for row in rows:
                    row_data = self.student_table.item(row)['values']
                    exp_write.writerow(row_data)

            messagebox.showinfo("Data Exported", f"Data Exported to {os.path.basename(fln)} Successfully!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Due To :{str(e)}", parent=self.root)

    def reset_data(self):
        self.var_student_id.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_reg_no.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_semester.set("")
        self.var_subject.set("")
        self.var_status.set("Status")

    def update_data(self):
        selected = self.student_table.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return

        self.student_table.item(selected, values=(
            self.var_student_id.get(),
            self.var_name.get(),
            self.var_dept.get(),
            self.var_reg_no.get(),
            self.var_date.get(),
            self.var_time.get(),
            self.var_semester.get(),
            self.var_subject.get(),
            self.var_status.get()
        ))

        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content["values"]
        self.var_student_id.set(row[0])
        self.var_name.set(row[1])
        self.var_dept.set(row[2])
        self.var_reg_no.set(row[3])
        self.var_date.set(row[4])
        self.var_time.set(row[5])
        self.var_semester.set(row[6])
        self.var_subject.set(row[7])
        self.var_status.set(row[8])


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
