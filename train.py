from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import face_recognition
import mysql.connector
import os
import numpy as np


class Train:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Images of Attendance System")

        # Title label
        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Load and display the first image
        img_1 = Image.open("images\\train_face_1.png").resize((510, 325), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)
        Label(self.root, image=self.photoimg_1).place(x=0, y=55, width=510, height=325)

        # Load and display the second image
        img_2 = Image.open("images\\train_face_2.jpg").resize((510, 325), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        Label(self.root, image=self.photoimg_2).place(x=510, y=55, width=510, height=325)

        # Load and display the third image
        img_3 = Image.open("images\\train_face_3.jpeg").resize((510, 325), Image.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)
        Label(self.root, image=self.photoimg_3).place(x=1020, y=55, width=510, height=325)

        # Add the train button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                    font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        # Load and display the bottom image
        img_bottom = Image.open("images\\train_face_bottom.webp").resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(x=0, y=440, width=1530, height=330)

    def train_classifier(self):
        # Directory where face data is stored
        data_dir = "data"
        # Get paths of all image files in the directory
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]

        faces = []  # To store encodings of face data
        ids = []    # To store corresponding user IDs

        for image in path:
            # Load the image and convert it to RGB
            img = cv2.imread(image)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the face encodings using face_recognition
            face_encodings = face_recognition.face_encodings(rgb_img)

            # Check if exactly one face is detected and proceed
            if face_encodings:
                # Extract user ID from the file name
                id = int(os.path.split(image)[1].split('.')[1])
                faces.append(face_encodings[0])  # Store the first encoding
                ids.append(id)

                # Display the training process
                cv2.imshow("Training", img)
                cv2.waitKey(1)

        # Save encodings and IDs into numpy arrays
        faces = np.array(faces)
        ids = np.array(ids)

        # Save the trained face encodings and IDs to a file
        np.savez_compressed("classifier.npz", faces=faces, ids=ids)

        # Close all OpenCV windows
        cv2.destroyAllWindows()

        # Display success message
        messagebox.showinfo("Result", "Training dataset has been completed!")

if __name__ == "__main__":
    # Run the application
    root = Tk()
    obj = Train(root)
    root.mainloop()