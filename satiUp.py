import wx
import requests
import zipfile
import os
import sys
import subprocess
import pythoncom
import shutil
from win32com.client import Dispatch
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    if sys.platform != 'win32':
        return

    try:
        ASADMIN = 'asadmin'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ASADMIN, None, 1)
    except Exception as e:
        print("Failed to run as admin:", e)
        sys.exit(1)

class SatisfactoryServerInstaller(wx.Frame):
    def __init__(self, parent, title):
        super(SatisfactoryServerInstaller, self).__init__(parent, title=title, size=(222, 420))
        
        panel = wx.Panel(self)
        self.install_button = wx.Button(panel, label="Install", pos=(10, 20))
        self.install_button.Bind(wx.EVT_BUTTON, self.on_install)

        self.run_button = wx.Button(panel, label="Run", pos=(10, 60))
        self.run_button.Bind(wx.EVT_BUTTON, self.on_run)

        self.update_button = wx.Button(panel, label="Update BP", pos=(10, 100))
        self.update_button.Bind(wx.EVT_BUTTON, self.on_update)

        self.to_experimental_button = wx.Button(panel, label="To Experimental", pos=(92, 100))
        self.to_experimental_button.Bind(wx.EVT_BUTTON, self.on_to_experimental)

        self.install_service_button = wx.Button(panel, label="Install Service", pos=(10, 140))
        self.install_service_button.Bind(wx.EVT_BUTTON, self.on_install_service)

        self.start_service_button = wx.Button(panel, label="Start Service", pos=(10, 180))
        self.start_service_button.Bind(wx.EVT_BUTTON, self.on_start_service)

        self.stop_service_button = wx.Button(panel, label="Stop Service", pos=(10, 220))
        self.stop_service_button.Bind(wx.EVT_BUTTON, self.on_stop_service)

        self.delete_service_button = wx.Button(panel, label="Delete Service", pos=(10, 260))
        self.delete_service_button.Bind(wx.EVT_BUTTON, self.on_delete_service)

        self.open_ports_button = wx.Button(panel, label="Open UDP Ports", pos=(10, 300))
        self.open_ports_button.Bind(wx.EVT_BUTTON, self.on_open_ports)

        self.create_shortcuts_button = wx.Button(panel, label="Create Shortcuts", pos=(10, 340))
        self.create_shortcuts_button.Bind(wx.EVT_BUTTON, self.on_create_shortcuts)



    def on_install(self, event):
        url = 'https://nssm.cc/release/nssm-2.24.zip'
        r = requests.get(url)
        with open("nssm-2.24.zip", "wb") as code:
            code.write(r.content)

        fantasy_zip = zipfile.ZipFile('nssm-2.24.zip')
        fantasy_zip.extractall('')
        fantasy_zip.close()

        shutil.copy('nssm-2.24/win64/nssm.exe', '.')

        os.remove("nssm-2.24.zip")
        
        url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'
        r = requests.get(url)
        with open("steamcmd.zip", "wb") as code:
            code.write(r.content)
        fantasy_zip = zipfile.ZipFile('steamcmd.zip')
        fantasy_zip.extractall('steamcmd')
        fantasy_zip.close()
        os.remove("steamcmd.zip")

        command = 'steamcmd/steamcmd.exe'
        args = [
            '+login', 'anonymous',
            '+force_install_dir', '..\SatisfactoryServer',
            '+app_update', '1690800', '-beta', 'public', 'validate', '+quit'
        ]
        subprocess.Popen([command] + args, cwd='steamcmd')


    def on_run(self, event):
        subprocess.Popen(['satisfactoryserver\FactoryServer.exe', '-log', '-unattended'])

    def on_update(self, event):
        command = 'steamcmd/steamcmd.exe'
        args = [
            '+login', 'anonymous',
            '+force_install_dir', '..\SatisfactoryServer',
            '+app_update', '1690800', '-beta', 'public', 'validate', '+quit'
        ]
        subprocess.Popen([command] + args, cwd='steamcmd')

    def on_to_experimental(self, event):
        command = 'steamcmd/steamcmd.exe'
        args = [
            '+login', 'anonymous',
            '+force_install_dir', '..\SatisfactoryServer',
            '+app_update', '1690800', '-beta', 'experimental', 'validate', '+quit'
        ]
        subprocess.Popen([command] + args, cwd='steamcmd')


    def on_install_service(self, event):
        cmd_command = 'nssm.exe install SatisfactoryServerService %CD%\satisfactoryserver\FactoryServer.exe -unattended'
        os.system(f'cmd /C "{cmd_command} & timeout 3"')

    def on_start_service(self, event):
        cmd_command = 'nssm.exe start SatisfactoryServerService'
        os.system(f'cmd /C "{cmd_command} & timeout 3"')


    def on_stop_service(self, event):
        cmd_command = 'nssm.exe stop SatisfactoryServerService'
        os.system(f'cmd /C "{cmd_command} & timeout 3"')

    def on_delete_service(self, event):
        cmd_command = 'nssm.exe remove SatisfactoryServerService'
        os.system(f'cmd /C "{cmd_command} & timeout 3"')

    def on_open_ports(self, event):
        cmd_command = 'powershell.exe New-NetFirewallRule -DisplayName "Allow-Satisfactory-default-inbound-ports" -Direction Inbound -Action Allow -EdgeTraversalPolicy Allow -Protocol UDP -LocalPort 15000,15777,7777'
        os.system(f'cmd /C "{cmd_command} & timeout 5 & exit"')

    def on_create_shortcuts(self, event):
        self.create_desktop_shortcut()
        self.create_service_shortcut()


    def create_desktop_shortcut(self):
        path = os.path.join(os.path.expanduser("~"), "Desktop", "SaveFile.lnk")
        target = os.path.expandvars(r"%LOCALAPPDATA%\FactoryGame\Saved\SaveGames")
        wDir = os.path.expandvars(r"%LOCALAPPDATA%\FactoryGame\Saved\SaveGames")
        icon = os.path.expandvars(r"%LOCALAPPDATA%\FactoryGame\Saved\SaveGames")
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()

    def create_service_shortcut(self):
        path = os.path.join(os.path.expanduser("~"), "Desktop", "ServiceSaveFile.lnk")
        target = os.path.expandvars(r"C:\Windows\System32\config\systemprofile\AppData\Local\FactoryGame\Saved\SaveGames\server")
        wDir = os.path.expandvars(r"C:\Windows\System32\config\systemprofile\AppData\Local\FactoryGame\Saved\SaveGames\server")
        icon = os.path.expandvars(r"C:\Windows\System32\config\systemprofile\AppData\Local\FactoryGame\Saved\SaveGames\server")
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()

if __name__ == '__main__':
    if is_admin():
        pythoncom.CoInitialize()
        app = wx.App()
        frame = SatisfactoryServerInstaller(None, "Easy install Satisfactory server")
        frame.Show()
        app.MainLoop()
    else:
        run_as_admin()
