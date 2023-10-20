# SatisfactoryPyServerInstaller(Win only)

Download, run in the folder where you want to deploy the server.


Istall steamCMD+SatisfactoryServer+nssm

Start server

Update Server from steamCMD to beta public + Update Server from steamCMD to beta experimental


Install server as Service nssm

Start Service Server

Stop Service Server

Delete Service Server

Open UDP port 15000,15777,7777

Create shortcuts to save files

**Before creating or launching the service, start the server from the beginning using the "Run" button. Also do this after changing the server version from public to experimental and vice versa.**

![image](https://github.com/asidsx/SatisfactoryPyServerInstaller/assets/106923482/75b32c53-e359-44c3-8821-b9f3340b11f1)






For the service to install and uninstall correctly, open udp port, run the application as an administrator.


Program already compiled go to https://github.com/asidsx/SatisfactoryPyServerInstaller/releases and download last release.

---

Alternatively, you can compile it by installing [Python](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe) and all the dependencies using pip install. For example:
```
pip install wx
pip install requests
pip install zipfile
pip install pywin32
pip install pyinstaller
```

After that, you can compile the program itself using the command in the command line: 
```
pyinstaller satiUp.py --onefile --noconsole
```

Please note that this process may vary depending on your specific setup and requirements. Make sure to consult the documentation of the packages you are using for detailed instructions on installation and compilation.
