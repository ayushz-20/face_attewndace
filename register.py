import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


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

        # Register Labels
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

        # Register Button
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

                # Check if username already exists
                query = "SELECT * FROM users WHERE username=%s"
                cursor.execute(query, (self.txtuser.get(),))
                row = cursor.fetchone()
                if row:
                    messagebox.showerror("Error", "Username already exists, please choose another")
                else:
                    # Insert new user
                    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                    cursor.execute(insert_query, (self.txtuser.get(), self.Password.get()))
                    connection.commit()
                    messagebox.showinfo("Success", "Registration Successful")
                    self.root.destroy()  # Close registration window
                connection.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")


if __name__ == "__main__":
    root = Tk()
    app = Register_Window(root)
    root.mainloop()
