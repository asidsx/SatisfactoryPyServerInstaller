from tkinter import *
import requests
import zipfile
import os
import tkinter as tk



def click_button():
    url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'
    r = requests.get(url)
    with open("steamcmd.zip", "wb") as code:
        code.write(r.content)
#-----------------------------------------------------------
    fantasy_zip = zipfile.ZipFile('steamcmd.zip')
    fantasy_zip.extractall('steamcmd')
    fantasy_zip.close()
#-----------------------------------------------------------
    os.startfile('steamcmd\steamcmd.exe', 'open', '+login anonymous +force_install_dir ..\SatisfactoryServer +app_update 1690800 -beta public validate +quit')
#-----------------------------------------------------------
    url = 'https://nssm.cc/release/nssm-2.24.zip'
    r = requests.get(url)
    with open("nssm-2.24.zip", "wb") as code:
        code.write(r.content)
#-----------------------------------------------------------
    fantasy_zip = zipfile.ZipFile('nssm-2.24.zip')
    fantasy_zip.extractall('')
    fantasy_zip.close()
#-----------------------------------------------------------
    os.remove("nssm-2.24.zip")
    os.remove("steamcmd.zip")

def click_button1():
    os.startfile('satisfactoryserver\FactoryServer.exe', 'open',
                 '-log -unattended')

def click_button2():
    os.startfile('steamcmd\steamcmd.exe', 'open', '+login anonymous +force_install_dir ..\SatisfactoryServer +app_update 1690800 -beta public validate +quit')

def click_button3():
    T.delete('1.0', END)
    Outputfileobject = os.popen('nssm.exe install SatisfactoryServerService %CD%\satisfactoryserver\FactoryServer.exe -unattended')
    Output = Outputfileobject.read()
    Outputfileobject.close()
    T.insert(tk.END, Output)

def click_button4():
    os.startfile('nssm.exe', 'open', 'start SatisfactoryServerService')

def click_button5():
    T.delete('1.0', END)
    Outputfileobject = os.popen('nssm.exe stop SatisfactoryServerService')
    Output = Outputfileobject.read()
    Outputfileobject.close()
    T.insert(tk.END, Output)

def click_button6():
    os.startfile('nssm.exe', 'open', 'remove SatisfactoryServerService')

def click_button7():

    T.delete('1.0', END)
    Outputfileobject=os.popen('powershell.exe New-NetFirewallRule -DisplayName "Allow-Satisfactory-default-inbound-ports" -Direction Inbound -Action Allow -EdgeTraversalPolicy Allow -Protocol UDP -LocalPort 15000,15777,7777')
    Output=Outputfileobject.read()
    Outputfileobject.close()
    T.insert(tk.END, Output)


root = Tk()
root.title("Easy install Satisfactory server")
root.geometry("660x350")
T = tk.Text(root, height=20, width=55)
T.pack(side=tk.LEFT)
T.pack()
T.place(x=2, y=20)

btn = Button(text="Install", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button)
btn.place(x=450, y=20, height=30, width=130, bordermode=INSIDE)

btn1 = Button(text="run", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button1)
btn1.place(x=450, y=60, height=30, width=130, bordermode=OUTSIDE)

btn2 = Button(text="update", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button2)
btn2.place(x=450, y=100, height=30, width=130, bordermode=OUTSIDE)

btn3 = Button(text="install service", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button3)
btn3.place(x=450, y=140, height=30, width=130, bordermode=OUTSIDE)

btn4 = Button(text="Start Service", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button4)
btn4.place(x=450, y=180, height=30, width=130, bordermode=OUTSIDE)

btn5 = Button(text="Stop Service", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button5)
btn5.place(x=450, y=220, height=30, width=130, bordermode=INSIDE)

btn6 = Button(text="delete service", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button6)
btn6.place(x=450, y=260, height=30, width=130, bordermode=OUTSIDE)

btn7 = Button(text="Open the default UDP ports", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button7)
btn7.place(x=450, y=300, height=30, width=200, bordermode=OUTSIDE)




root.mainloop()


