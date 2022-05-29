from tkinter import*

from tkinter import ttk

from PIL import Image, ImageTk

from tkinter import messagebox


class Student:

    def __init__(self, root):
        self.root = root

        self.root.geometry("1730x790+0+0")

        self.root.title("FACE RECOGIZATION SYSTEM)")

        # variable
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

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

        img3 = img3.resize((1730, 710), Image.ANTIALIAS)

        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)

        bg_img.place(x=0, y=130, width=1730, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTM", font=(

            "times new roman", 35, "bold"), bg="white", fg="darkorange")

        title_lbl.place(x=0, y=0, width=1730, height=45)

        main_frame = Frame(bg_img, bd=2)

        main_frame.place(x=5, y=55, width=1700, height=600)

        # left lable frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold")
                                )

        Left_frame.place(x=0, y=10, width=730, height=580)

        img_left = Image.open(

            r"C:\Users\Lenovo\Desktop\face recommandation\images\studentraisehand.jpg")

        img_left = img_left.resize((730, 580), Image.ANTIALIAS)

        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)

        f_lbl.place(x=5, y=0, width=720, height=130)

        # current course

        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course information", font=("times new roman", 12, "bold")
                                         )

        class_student_frame.place(x=5, y=135, width=720, height=117)

        # department
        dep_label = Label(class_student_frame, text="Department",
                          font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0)

        dep_combo = ttk.Combobox(class_student_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly", width=17)

        dep_combo["value"] = ("Select Department",
                              "Computer", "IT", "Mechanical", "Civil")
        dep_combo.current(0)

        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(class_student_frame, text="Course",
                             font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(class_student_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly", width=17)

        course_combo["value"] = ("Select Course",
                                 "FE", "SE", "TE", "BE")
        course_combo.current(0)

        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(class_student_frame, text="Year",
                           font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(class_student_frame, textvariable=self.var_year, font=(
            "times new roman", 13, "bold"), state="readonly", width=17)

        year_combo["value"] = ("Select Year",
                               "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)

        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # student_id
        student_name_label = Label(class_student_frame, text="student_id",
                                   font=("times new roman", 13, "bold"), bg="white")
        student_name_label.grid(row=1, column=2, padx=10, sticky=W)

        student_id_combo = ttk.Combobox(class_student_frame, textvariable=self.var_std_id, font=(
            "times new roman", 12, "bold"), state="readonly", width=17)

        student_id_combo["value"] = ("Select Student_ID",
                                     "student_id-1", "student_id-2")
        student_id_combo.current(0)

        student_id_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student information

        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class student information ", font=("times new roman", 12, "bold")
                                         )

        class_student_frame.place(x=5, y=260, width=720, height=300)
        # Student id
        studentid_label = Label(class_student_frame, text="Student ID",
                                font=("times new roman", 13, "bold"), bg="white")
        studentid_label.grid(row=0, column=0, padx=10, sticky=W)

        studentid_entry = Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        studentid_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student name
        student_name_label = Label(class_student_frame, text="Student name",
                                   font=("times new roman", 13, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10, sticky=W)

        student_name_entry = Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        student_name_entry.grid(row=0, column=3, padx=10, sticky=W)

        # class division

        clas_division_label = Label(class_student_frame, text="Class Division",
                                    font=("times new roman", 13, "bold"), bg="white")
        clas_division_label.grid(row=1, column=0, padx=10, sticky=W)

        class_division_entry = Entry(class_student_frame, textvariable=self.var_div, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        class_division_entry.grid(row=1, column=1, padx=10, sticky=W)

        # roll_no

        roll_no_label = Label(class_student_frame, text="Roll No.",
                              font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, sticky=W)

        roll_no_entry = Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        roll_no_entry.grid(row=1, column=3, padx=10, sticky=W)

        # Gender

        Gender_label = Label(class_student_frame, text="Gender",
                             font=("times new roman", 13, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, sticky=W)

        Gender_entry = Entry(class_student_frame, textvariable=self.var_gender, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        Gender_entry.grid(row=2, column=1, padx=10, sticky=W)

        # DOB

        DOB_label = Label(class_student_frame, text="DOB",
                          font=("times new roman", 13, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, sticky=W)

        DOB_entry = Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        DOB_entry.grid(row=2, column=3, padx=10, sticky=W)

        # email

        email_label = Label(class_student_frame, text="Email",
                            font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, sticky=W)

        email_entry = Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        email_entry.grid(row=3, column=1, padx=10, sticky=W)

        # phone

        phone_label = Label(class_student_frame, text="Phone",
                            font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, sticky=W)

        phone_entry = Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        phone_entry.grid(row=3, column=3, padx=10, sticky=W)

        # address

        address_label = Label(class_student_frame, text="Address",
                              font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, sticky=W)

        address_entry = Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        address_entry.grid(row=4, column=1, padx=10, sticky=W)

        # teacher_name

        teacher_name_label = Label(class_student_frame, text="Teacher name",
                                   font=("times new roman", 13, "bold"), bg="white")
        teacher_name_label.grid(row=4, column=2, padx=10, sticky=W)

        teacher_name_entry = Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=(
            "times new roman", 13, "bold"), bg="white")

        teacher_name_entry.grid(row=4, column=3, padx=10, sticky=W)

        # radio button
        radiobutton1 = Radiobutton(
            class_student_frame, text="take Photo sample", value="Yes")
        radiobutton1.grid(row=5, column=0)

        radiobutton2 = Radiobutton(
            class_student_frame, text="No Photo sample", value="Yes")
        radiobutton2.grid(row=5, column=1)

        # bbutton frame

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=70)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=1)

    # right lable frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold")
                                 )

        right_frame.place(x=750, y=10, width=720, height=580)
        img_right = Image.open(

            r"C:\Users\Lenovo\Desktop\face recommandation\images\groupstudy.jpeg")

        img_right = img_right.resize((720, 130), Image.ANTIALIAS)

        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)

        f_lbl.place(x=5, y=0, width=720, height=130)

        # search system

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search Box", font=("times new roman", 12, "bold")
                                  )

        search_frame.place(x=5, y=135, width=700, height=70)
        search_label = Label(search_frame, text="Search by",
                             font=("times new roman", 13, "bold"), bg="red", fg="black")
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12, "bold"), state="readonly", width=17)

        search_combo["value"] = ("Select Department",
                                 "Roll no.", "Phone No.")
        search_combo.current(0)

        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = Entry(search_frame, width=15, font=(
            "times new roman", 13, "bold"), bg="white")

        search_entry.grid(row=0, column=2, padx=10, sticky=W)

        search_btn = Button(search_frame, text="Searh", width=12, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All", width=12, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)

        table_frame.place(x=5, y=210, width=710, height=135)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                                          "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teachers")
        self.student_table.heading("photo", text="PhotoSamplStatus")

        self.student_table.column("dep", width=100)

        self.student_table.column("course", width=100)

        self.student_table.column("year", width=100)

        self.student_table.column("sem", width=100)

        self.student_table.column("id", width=100)

        self.student_table.column("name", width=100)

        self.student_table.column("roll", width=100)

        self.student_table.column("gender", width=100)

        self.student_table.column("div", width=100)

        self.student_table.column("dob", width=100)

        self.student_table.column("email", width=100)

        self.student_table.column("address", width=100)

        self.student_table.column("teacher", width=100)

        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)

        # function declaration
        def add_data(self):
            if self.vardep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
                messagebox.showerror("Error", "All Fields are required")


if __name__ == "__main__":

    root = Tk()

    obj = Student(root)
    root.mainloop()
