from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        
        # Title label
        title_lbl = Label(self.root, text="Developer", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and display the first image
        img_1 = Image.open("images\\developer.png").resize((1530, 720), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)
        Label(self.root, image=self.photoimg_1).place(x=0, y=55, width=1530, height=720)
        
        # frame
        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=1000, y=0, width=500, height=600)
        
        # Load and display the first image
        img_me= Image.open("images\\Ayush.jpg").resize((200, 235), Image.LANCZOS)
        self.photoimg_me = ImageTk.PhotoImage(img_me)
        Label(main_frame, image=self.photoimg_me).place(x=300, y=0, width=200, height=300)
        
        # developer info
        Label(main_frame, text="Wssup...!! I am Ayush", font=("times new roman", 18, "bold"), bg="white").place(x=0,y=5)
        Label(main_frame, text="I am a Computer Science student", font=("times new roman", 16, "bold"), bg="white").place(x=0,y=40)
        Label(main_frame, text="Here's My Gmail for any queries :", font=("times new roman", 15, "bold"), bg="white").place(x=0,y=75)
        Label(main_frame, text="theayushchakraborty@gmail.com", font=("times new roman", 15, "bold"), bg="white").place(x=0,y=110)
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
        