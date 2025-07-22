import smtplib
import random
import tkinter as tk
from tkinter import messagebox,Label,Entry,Grid

sender = " " #sender email address
receiver = " " #receiver email address
password = " " #sender password
OTP = random.randint(1000,9999)

def check() :  
    entered = int(user_input.get())
    if entered == OTP :
        messagebox.showinfo(title = "Success" , message = "Your OTP has been verified")

#mail sender
response = smtplib.SMTP("smtp.gmail.com",587)
response.starttls()
response.login(user=sender,password=password)
response.sendmail(from_addr = sender , to_addrs = receiver , msg = f"Your OTP is {OTP}")
response.close()

window  = tk.Tk()
window.title("Login Credentials")
window.configure(padx=50,pady=50)

#GUI
text_label = Label(text = "Enter Your OTP :")
user_input = Entry()
text_label.grid(row=0,column=0)
user_input.grid(row=0,column=1)
tk.Button(window,text="Verify",command=check,width=15).grid(row=1,column=1)
window.mainloop()
