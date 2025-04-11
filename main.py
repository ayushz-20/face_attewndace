from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import tkinter
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # 1st Image:
        # Open and resize the image
        img1= Image.open("images\\cruise.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        # Display the image in a label
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)
        
        
        # 2nd Image
        # Open and resize the image
        img2 = Image.open("images\\smart_face.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        # Display the image in a label
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=514, height=130)
        
        
        # 3rd Image
        # Open and resize the image
        img3 = Image.open("images\\smart_face2.jpg")
        img3 = img3.resize((500, 130), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        # Display the image in a label
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=525, height=130)
        
        # Background Image
        # Open and resize the image
        img4 = Image.open("images\\bg_image.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        # Display the image in a label
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        def time():
            string = strftime('%H:%M:%S %p')  # Get the current time as a string
            lbl.config(text=string)  # Update the label's text
            lbl.after(1000, time)  # Call the `time` function again after 1 second

        # Define the label for displaying time
        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=45)

        # Start the time function
        time()
        
        # student button
        img5 = Image.open("images\\students.jpg")
        img5 = img5.resize((250, 220), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.Student,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.Student,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        # Detect Face button
        img6 = Image.open("images\\face_detector.jpg")
        img6 = img6.resize((250, 220), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,command=self.face_data,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        # Attendance button
        img7 = Image.open("images\\attendance_bt.WEBP")
        img7 = img7.resize((250, 220), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,command=self.attendance_data,image=self.photoimg7,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,command=self.attendance_data,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
        # Help Desk button
        img8 = Image.open("images\\Help.webp")
        img8 = img8.resize((250, 220), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        # Train Face button
        img9 = Image.open("images\\train.jpg")
        img9 = img9.resize((250, 220), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=360,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=550,width=220,height=40)
        
        # Photos button
        img10 = Image.open("images\\photo.jpg")
        img10 = img10.resize((250, 220), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=360,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=550,width=220,height=40)
        
        # Developer button
        img11 = Image.open("images\\developer.jpg")
        img11 = img11.resize((250, 220), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,command=self.Developer_data,image=self.photoimg11,cursor="hand2")
        b1.place(x=800,y=360,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",command=self.Developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=550,width=220,height=40)
        
        
        # Exit button
        img12 = Image.open("images\\exit.jpeg")
        img12 = img12.resize((250, 220), Image.LANCZOS)  # Use Image.LANCZOS for newer Pillow versions
        self.photoimg12 = ImageTk.PhotoImage(img12)
        
        b1=Button(bg_img,command=self.iExit,image=self.photoimg6,cursor="hand2")
        b1.place(x=1100,y=360,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=550,width=220,height=40)
        
        
        
    def open_img(self):
        os.startfile("data")
        
        
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Faece Recognition", "Are you sure , you want to exit ?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return
        
        # funtion buttons
        
    def Student(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
        
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
        
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def Developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
