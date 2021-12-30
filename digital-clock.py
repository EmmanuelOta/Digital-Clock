from  tkinter import *
import time

root = Tk()
root.title("Clock")
root.geometry("460x150")
root.iconbitmap("C:/Users/U-PC/Codes/Python/Clock/clock.ico")


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")
    label.config(text=hour + ":" + minute + ":" + second + " "+ am_pm)
    label.after(1000, clock)
    label1.config(text=time_zone + ", " + day)




label = Label(root, text="", font=('Consolas', 40), fg="green", bg="black")
label.pack(pady=20)
label1 = Label(root, font=("Consolas", 15), fg="green", bg="black")
label1.pack(pady=0)

clock()

root.config(bg="grey")
root.mainloop()