#### Так же не проходите мимо проекта по управлению сервера через API.
#### Also, don't miss the project for server management via API.
[satisfactory-python-cli](https://github.com/Feyr/satisfactory-python-cli)

---
# SatisfactoryPyServerInstaller(Win only)
![GitHub all releases](https://img.shields.io/github/downloads/asidsx/SatisfactoryPyServerInstaller/total)

Download, run in the folder where you want to deploy the server.


`Istall steamCMD+SatisfactoryServer+nssm`

`Start server`

`Update Server from steamCMD to Release + Update Server from steamCMD to beta experimental`

`Install server as Service nssm`

`Start Service Server`

`Stop Service Server`

`Delete Service Server`

`Open UDP/TCP 7777 Ports`

`Create shortcuts to save files`

**Before creating or launching the service, start the server from the beginning using the "Run" button. Also do this after changing the server version from public to experimental and vice versa.**

![image](https://github.com/user-attachments/assets/2ee5d990-7ba2-46b4-b516-942ad5d60e2d)





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


---
---

# SatisfactoryPyServerInstaller (Только для Windows)

Скачайте и запустите в папке, где вы хотите развернуть сервер.


`Установить steamCMD + SatisfactoryServer + nssm`

`Запустить сервер`

`Обновить сервер с помощью steamCMD на Релизную версию + Обновить сервер с помощью steamCMD на экспериментальную бета-версию`

`Установить сервер как службу с помощью nssm`

`Запустить службу сервера`

`Остановить службу сервера`

`Удалить службу сервера`

`Открыть UDP/TCP-порт 7777`

`Создать ярлыки для файлов сохранения`

**Перед созданием или запуском службы, запустите сервер с помощью кнопки "Run". Также сделайте это после изменения версии сервера с публичной на экспериментальную и наоборот.**

![image](https://github.com/user-attachments/assets/2ee5d990-7ba2-46b4-b516-942ad5d60e2d)


Программа уже скомпилирована, перейдите по ссылке https://github.com/asidsx/SatisfactoryPyServerInstaller/releases и скачайте последний релиз.

---

Кроме того, вы можете скомпилировать ее, установив [Python](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe) и все зависимости с помощью pip install. Например:

```
pip install wx
pip install requests
pip install zipfile
pip install pywin32
pip install pyinstaller
```


После этого вы можете скомпилировать саму программу с помощью команды в командной строке:
```
pyinstaller satiUp.py --onefile --noconsole
```


