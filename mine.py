from tkinter import *
import requests
import zipfile
import os




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

    os.system('nssm.exe install SatisfactoryServerService %CD%\satisfactoryserver\FactoryServer.exe -unattended')

def click_button4():
    os.startfile('nssm.exe', 'open', 'start SatisfactoryServerService')

def click_button5():
    os.startfile('nssm.exe', 'open', 'stop SatisfactoryServerService')

def click_button6():
    os.startfile('nssm.exe', 'open', 'remove SatisfactoryServerService')







root = Tk()
root.title("Easy install Satisfactory server")
root.geometry("300x500")

btn = Button(text="Install", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button)
btn.place(relx=.5, rely=.1, anchor="c", height=30, width=130, bordermode=OUTSIDE)

btn1 = Button(text="run", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button1)
btn1.place(relx=.5, rely=.2, anchor="c", height=30, width=130, bordermode=OUTSIDE)

btn2 = Button(text="update", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button2)
btn2.place(relx=.5, rely=.3, anchor="c", height=30, width=130, bordermode=OUTSIDE)

btn3 = Button(text="install service", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button3)
btn3.place(relx=.5, rely=.4, anchor="c", height=30, width=130, bordermode=OUTSIDE)

btn4 = Button(text="Start Service", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button4)
btn4.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

btn5 = Button(text="Stop Service", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button5)
btn5.place(relx=.5, rely=.6, anchor="c", height=30, width=130, bordermode=INSIDE)

btn6 = Button(text="delete service", background="#555", foreground="#ccc",
             padx="20", pady="11", font="16", command=click_button6)
btn6.place(relx=.5, rely=.7, anchor="c", height=30, width=130, bordermode=OUTSIDE)



root.mainloop()


