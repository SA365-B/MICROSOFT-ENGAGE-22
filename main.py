from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student


class face_recignization_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGIZATION SYSTEM)")
        # first image

        img = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\back.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\center.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\head.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # background
        img3 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNIZATION ATTENDANCE SYSTEM SOFTWARE", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # student button
        img4 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\stud.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_t = Button(bg_img, text="STUDENT DETAILS", command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_t.place(x=200, y=300, width=220, height=40)

        # Detect student button
        img5 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\face_detector.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_t = Button(bg_img, text="FACE DETECTION", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_t.place(x=500, y=300, width=220, height=40)

        # attendance

        img6 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\attendance.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_t = Button(bg_img, text="ATTENDANCE", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_t.place(x=800, y=300, width=220, height=40)

        # Help_Desk

        img7 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\help.png")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_t = Button(bg_img, text="HELP", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_t.place(x=1100, y=300, width=220, height=40)

        # Train_Data
        img8 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\train_data.jfif")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=400, width=220, height=220)

        b1_t = Button(bg_img, text="TRAIN DATA", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_t.place(x=200, y=600, width=220, height=40)

        # photos

        img9 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\PHOTO.jfif")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=500, y=400, width=220, height=220)

        b1_t = Button(bg_img, text="PHOTO", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_t.place(x=500, y=600, width=220, height=40)

        # developer

        img_10 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\developer.jpg")
        img_10 = img_10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg_10 = ImageTk.PhotoImage(img_10)

        b1 = Button(bg_img, image=self.photoimg_10, cursor="hand2")
        b1.place(x=800, y=400, width=220, height=220)

        b1_t = Button(bg_img, text="DEVELOPER", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_t.place(x=800, y=600, width=220, height=40)

        # Exit
        img11 = Image.open(
            r"C:\Users\Lenovo\Desktop\face recommandation\images\exit.jfif")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=400, width=220, height=220)

        b1_t = Button(bg_img, text="EXIT", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_t.place(x=1100, y=600, width=220, height=40)

        # function button

        def student_details(self):
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = face_recignization_system(root)
    root.mainloop()
