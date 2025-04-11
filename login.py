
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess  # For running main.py

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1550x800+0+0")

        # Background Image
        img4 = Image.open("images\\login_bg.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, width=1530, height=710)

        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open("images/login_icon.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimage1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimage1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="white")
        get_str.place(x=95, y=100)

        # Labels
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="white")
        username_lbl.place(x=70, y=155)
        self.txtuser = Entry(frame, font=("times new roman", 20, "bold"), fg="black", bg="white", borderwidth=1)
        self.txtuser.place(x=40, y=180, width=270)

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password_lbl.place(x=70, y=225)
        self.Password = Entry(frame, font=("times new roman", 20, "bold"), fg="black", bg="white", borderwidth=1, show="*")
        self.Password.place(x=40, y=250, width=270)

        # Buttons
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 20, "bold"),
                          bd=3, relief=RIDGE, fg="black", bg="white", activeforeground="white", activebackground="black")
        loginbtn.place(x=110, y=310, width=120, height=45)

        reg_btn = Button(frame, text="Register Here", command=self.register, font=("times new roman", 15, "bold"),
                         bd=3, relief=RIDGE, fg="black", bg="white", activeforeground="white", activebackground="black")
        reg_btn.place(x=90, y=370, width=160, height=45)

    def login(self):
        if self.txtuser.get() == "" or self.Password.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Ayush1980",  # Replace with your MySQL password
                    database="userdb"         # Replace with your database name
                )
                cursor = connection.cursor()
                query = "SELECT * FROM users WHERE username=%s AND password=%s"
                cursor.execute(query, (self.txtuser.get(), self.Password.get()))
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password")
                else:
                    messagebox.showinfo("Success", "Login Successful")
                    self.open_main_page()
                connection.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")

    def register(self):
        self.new_window = Toplevel(self.root)  # Open a new window
        self.app = Register_Window(self.new_window)

    def open_main_page(self):
        self.root.destroy()  # Close the login window
        subprocess.run(["python", "main.py"])  # Replace 'main.py' with the actual main application script


class Register_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Window")
        self.root.geometry("1550x800+0+0")

        # Background Image
        img4 = Image.open("images\\login_bg.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, width=1530, height=710)

        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)

        register_lbl = Label(frame, text="Register Here", font=("times new roman", 20, "bold"), fg="black", bg="white")
        register_lbl.place(x=90, y=50)

        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="white")
        username_lbl.place(x=40, y=100)
        self.txtuser = Entry(frame, font=("times new roman", 15), fg="black", bg="white", borderwidth=1)
        self.txtuser.place(x=40, y=130, width=250)

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password_lbl.place(x=40, y=170)
        self.Password = Entry(frame, show="*", font=("times new roman", 15), fg="black", bg="white", borderwidth=1)
        self.Password.place(x=40, y=200, width=250)

        confirm_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        confirm_lbl.place(x=40, y=240)
        self.ConfirmPassword = Entry(frame, show="*", font=("times new roman", 15), fg="black", bg="white", borderwidth=1)
        self.ConfirmPassword.place(x=40, y=270, width=250)

        regbtn = Button(frame, text="Register", command=self.register, font=("times new roman", 15, "bold"),
                        bd=3, relief=RIDGE, fg="black", bg="white", activeforeground="white", activebackground="black")
        regbtn.place(x=110, y=320, width=120, height=45)

    def register(self):
        if self.txtuser.get() == "" or self.Password.get() == "" or self.ConfirmPassword.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.Password.get() != self.ConfirmPassword.get():
            messagebox.showerror("Error", "Passwords do not match")
        else:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Ayush1980",  # Replace with your MySQL password
                    database="userdb"         # Replace with your database name
                )
                cursor = connection.cursor()

                query = "SELECT * FROM users WHERE username=%s"
                cursor.execute(query, (self.txtuser.get(),))
                row = cursor.fetchone()
                if row:
                    messagebox.showerror("Error", "Username already exists, please choose another")
                else:
                    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                    cursor.execute(insert_query, (self.txtuser.get(), self.Password.get()))
                    connection.commit()
                    messagebox.showinfo("Success", "Registration Successful")
                    self.root.destroy()
                connection.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
