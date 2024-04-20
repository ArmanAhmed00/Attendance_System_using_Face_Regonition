from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

import get_faces_from_camera_tkinter


class Face_Recognition_System:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        face = get_faces_from_camera_tkinter.Face_Register


        #first image 1
        img1 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/images.jpeg")
        img1 = img1.resize((500,130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)



        #second image 2
        img2 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/r1.jpg")
        img2 = img2.resize((500, 130))

        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

        #third image 3
        img3 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/r2.jpeg")
        img3 = img3.resize((500, 130))

        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)



        #background image
        img4 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/bg.jpeg")
        img4 = img4.resize((1530, 710))

        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl = Label(bg_img,text="Attendance Monitoring System", font=("Arial", 35, "bold"),bg="white",fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #detect face button

        img5 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/b1.jpeg")
        img5 = img5.resize((220, 220))

        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img,image=self.photoimg5, command=self.get_faces_from_camera_tkinter.Face_Register, cursor="hand")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, command=self.student_page, text="Student Details", cursor="hand", font=("Arial", 15, "bold"),bg="darkblue",fg="red")
        b1_1.place(x=200, y=300, width=220, height=40)


        #Detect face
        img6 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/b1.jpeg")
        img6 = img6.resize((220, 220))

        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Detect Face", cursor="hand", font=("Arial", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=500, y=300, width=220, height=40)


        #Attendane face button
        img7 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/b1.jpeg")
        img7 = img7.resize((220, 220))

        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendence", cursor="hand", font=("Arial", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=800, y=300, width=220, height=40)


        #Train face button
        img8 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/b1.jpeg")
        img8 = img8.resize((220, 220))

        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train ", cursor="hand", font=("Arial", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=200, y=580, width=220, height=40)


        #photo Face button
        img9 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/b1.jpeg")
        img9 = img9.resize((220, 220))

        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9, cursor="hand")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand", font=("Arial", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=500, y=580, width=220, height=40)

        #Exit Button
        img10 = Image.open("/Users/armanahmed/Desktop/Face_recognition/resource/b1.jpeg")
        img10= img8.resize((220, 220))

        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimg10, cursor="hand")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand", font=("Arial", 15, "bold"), bg="darkblue", fg="red")
        b1_1.place(x=800, y=580, width=220, height=40)

        # ========== functional button ===========

    def student_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)









if __name__ == "__main__":
    root =Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()