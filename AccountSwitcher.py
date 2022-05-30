import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess
import time
import pyautogui
from functools import partial

root = tk.Tk()
root.title('Valorant Account Selector')
Loc = 0
accounts = []
user = tk.StringVar()
pas = tk.StringVar()

if os.path.isfile('sve.txt'):
    with open('sve.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        accounts = [x for x in tempApps if x.strip()]
with open('Loc.txt','r') as f:
    Loc = f.read() 


def login(username,password):
    subprocess.Popen(Loc)
    time.sleep(5)
    pyautogui.typewrite(username, interval = 0.01)
    pyautogui.press('tab')
    pyautogui.typewrite(password,interval = 0.01)
    pyautogui.press('enter')
    time.sleep(3)
    #selects valorant
    pyautogui.moveTo(445,445)
    pyautogui.click()
    time.sleep(2)
    #clicks play button
    pyautogui.moveTo(330,920)
    pyautogui.click()   
def submit():
    action = partial(poo,(user.get() + ' ' + pas.get()))
    account = tk.Button(frame, text = (user.get() + ' ' + pas.get()), command = action)
    account.pack()
    
    accounts.append(user.get() + ' '+ pas.get())
def poo(use):
    for i in range(len(use) - 2 ):
        if use[i] == ' ' :
            first = use[:i]
            last = use[i+1:]
    login(username = first,password = last)  



canvas = tk.Canvas(root, height = 700, width = 500, bg = "#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight = 0.8,relx = 0.1,rely=0.1)





name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = user, font=('calibre',10,'normal'))

passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
passw_entry=tk.Entry(root, textvariable = pas, font = ('calibre',10,'normal'), show = '*')

Submit=tk.Button(root,text = 'Submit', command = submit)

name_label.pack()
name_entry.pack()
passw_label.pack()
passw_entry.pack()
Submit.pack()

for account in accounts:
    action = partial(poo, account)
    label = tk.Button(frame, text = account,command = action)
    label.pack()

if Loc == 0:
    
    Loc = filedialog.askopenfilename(initialdir = "/",title = "Select File",
    filetypes = (("executables" , "*.exe"),("all files","*.*")))
    with open('Loc.txt','w') as f:
        f.write(Loc)


root.mainloop()

with open('sve.txt', 'w') as f:
    for account in accounts:
        f.write(account+',')

        
