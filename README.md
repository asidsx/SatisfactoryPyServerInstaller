# SatisfactoryPyServerInstaller(Win only)
![GitHub all releases](https://img.shields.io/github/downloads/asidsx/SatisfactoryPyServerInstaller/total)

Download, run in the folder where you want to deploy the server.


`Istall steamCMD+SatisfactoryServer+nssm`

`Start server`

`Update Server from steamCMD to beta public + Update Server from steamCMD to beta experimental`

`Install server as Service nssm`

`Start Service Server`

`Stop Service Server`

`Delete Service Server`

`Open UDP port 15000,15777,7777`

`Create shortcuts to save files`

**Before creating or launching the service, start the server from the beginning using the "Run" button. Also do this after changing the server version from public to experimental and vice versa.**

![image](https://github.com/asidsx/SatisfactoryPyServerInstaller/assets/106923482/75b32c53-e359-44c3-8821-b9f3340b11f1)




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

`Обновить сервер с помощью steamCMD на публичную бета-версию + Обновить сервер с помощью steamCMD на экспериментальную бета-версию`

`Установить сервер как службу с помощью nssm`

`Запустить службу сервера`

`Остановить службу сервера`

`Удалить службу сервера`

`Открыть UDP-порт 15000, 15777, 7777`

`Создать ярлыки для файлов сохранения`

**Перед созданием или запуском службы, запустите сервер с помощью кнопки "Run". Также сделайте это после изменения версии сервера с публичной на экспериментальную и наоборот.**

![image](https://github.com/asidsx/SatisfactoryPyServerInstaller/assets/106923482/75b32c53-e359-44c3-8821-b9f3340b11f1)


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


