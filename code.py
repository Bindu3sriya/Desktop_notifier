from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

t = Tk()
t.title('Notifier')
t.geometry("500x300")
img = Image.open("notify-label.png")
tkimage = ImageTk.PhotoImage(img)

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    get_time2 = time2.get()
    get_time3 = time3.get()
    # print(get_title,get_msg, tt)

    if get_title == "" or get_msg == "" or get_time == "" or get_time2 == "" or get_time3 == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        int_time2 = int(float(get_time2))
        int_time3 = int(float(get_time3))
        min_to_sec = (int_time * 60 * 60) + (int_time2 * 60) + int_time3

        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)

img_label = Label(t, image=tkimage).grid()

# Label - Title
t_label = Label(t, text="Title to Notify",font=("poppins", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="25",font=("poppins", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time

# ENTRY - Time - Hours
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=175)

# ENTRY - Time - Minutes
time2 = Entry(t, width="5", font=("poppins", 13))
time2.place(x=243, y=175)

# ENTRY - Time - Seconds
time3 = Entry(t, width="5", font=("poppins", 13))
time3.place(x=343, y=175)

# Label - Hrs
time_min_label = Label(t, text="Hrs", font=("poppins", 10))
time_min_label.place(x=175, y=180)

# Lable - Min
time_min_label = Label(t, text="Min", font=("poppins", 10))
time_min_label.place(x=300, y=180)

# Lable - Sec
time_min_label = Label(t, text="Sec", font=("poppins", 10))
time_min_label.place(x=400, y=180)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()

