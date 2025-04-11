from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2.face
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import face_recognition


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_1 = Image.open("images\\face_left.jpg").resize((650, 700), Image.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)
        Label(self.root, image=self.photoimg_1).place(x=0, y=55, width=650, height=700)

        img_2 = Image.open("images\\face_right.png").resize((950, 700), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        Label(self.root, image=self.photoimg_2).place(x=650, y=55, width=950, height=700)

        b1_1 = Button(
            self.root, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"),
            bg="darkblue", fg="white", command=self.face_recog
        )
        b1_1.place(x=1055, y=700, width=200, height=40)

        # Predefined routines for different semesters
        self.routines = {
            "3rd": {
                "09:00-10:00": "Python",
                "10:00-11:00": "Data Structure",
                "11:00-12:00": "C programming",
                "12:00-13:00": "CSO",
                "20:00-21:00": "Algorithm",
            },
            "4th": {
                "09:00-10:00": "Operating Systems",
                "10:00-11:00": "OOP in Java",
                "11:00-12:00": "Computer Networks",
                "12:00-13:00": "Software Engineering",
                "14:00-15:00": "Introduction to DBMS",
            },
            "5th": {
                "09:00-10:00": "Theory of Automata",
                "10:00-11:00": "IoT",
                "11:00-12:00": "Computer Graphics",
                "12:00-13:00": "Mobile Computing",
                "15:50-16:50": "Microprocessor and Microcontroller",
            },
        }

        # Tracks last subject attended for each student
        self.last_marked_subject = {}

    # Attendance logic with semester and subject integration
    def mark_attendance(self, face_id, dept, name, reg_no, semester):
        today_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M")

        def format_semester(semester):
            # Remove 'semester' and strip extra spaces
            semester = semester.lower().replace("semester", "").strip()
            
            # Remove any existing suffixes (e.g., 'rd', 'th', etc.)
            semester_number = int(''.join(filter(str.isdigit, semester)))
            
            # Determine the correct suffix
            if 10 <= semester_number % 100 <= 20:  # Handle exceptions like 11th, 12th, 13th
                suffix = "th"
            else:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(semester_number % 10, "th")
            
            return f"{semester_number}{suffix}"

        semester = format_semester(semester)
        # Retrieve the routine for the given semester
        routine = self.routines.get(semester)
        if not routine:
            print("No routine found for the semester:", semester)
            return

        # Check if the current time falls within any subject's slot
        subject = None
        for time_range, subject_name in routine.items():
            start_time, end_time = time_range.split("-")
            start_time_dt = datetime.strptime(start_time, "%H:%M")
            end_time_dt = datetime.strptime(end_time, "%H:%M")

            current_time_dt = datetime.strptime(current_time, "%H:%M")
            if start_time_dt <= current_time_dt < end_time_dt:
                subject = subject_name
                break

        if not subject:
            print("No subject is scheduled at this time:", current_time)
            return

        # Check if this student has already been marked for this subject
        last_subject = self.last_marked_subject.get(face_id)
        if last_subject == subject:
            print(f"Attendance already marked for {name} in subject: {subject}")
            return

        # Mark attendance with subject
        try:
            with open("attendance.csv", "a", newline="\n") as f:
                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{face_id},{name},{dept},{reg_no},{today_date},{dtString},{semester},{subject},Present")
            print(f"Attendance marked successfully for {name} in subject: {subject}")

            # Update last marked subject for this student
            self.last_marked_subject[face_id] = subject
        except Exception as e:
            print("Failed to write to attendance.csv:", e)

    # Face recognition logic
    def face_recog(self):
        def draw_boundary(img, face_locations, face_encodings, known_faces, known_ids):
            coords = []

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.6)
                name = "Unknown"
                id = None

                # Find the closest match
                if True in matches:
                    first_match_index = matches.index(True)
                    id = known_ids[first_match_index]

                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Ayush1980", database="face_attendance"
                    )
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT name, reg_no, dept, semester FROM student WHERE Student_id=" + str(id))
                    student_data = my_cursor.fetchone()

                    if student_data:
                        name, reg_no, dept, semester = student_data

                        # Display recognized information
                        cv2.putText(img, f"ID: {id}", (left, top - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {name}", (left, top - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"reg_no: {reg_no}", (left, top - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {dept}", (left, top - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                        # Mark attendance
                        self.mark_attendance(id, dept, name, reg_no, semester)

                    conn.close()
                else:
                    # For unknown faces
                    cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (left, top - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                # Draw a rectangle around the face
                cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
                coords.append((left, top, right, bottom))

            return coords

        def recognize(img, known_faces, known_ids):
            # Convert BGR to RGB
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Detect face locations and encodings
            face_locations = face_recognition.face_locations(rgb_img)
            face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

            draw_boundary(img, face_locations, face_encodings, known_faces, known_ids)
            return img

        # Load trained face encodings and IDs
        data = np.load("classifier.npz", allow_pickle=True)
        known_faces = data["faces"]
        known_ids = data["ids"]

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, known_faces, known_ids)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

