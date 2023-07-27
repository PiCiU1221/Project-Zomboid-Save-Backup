# Project-Zomboid-Save-Backup
Simple Python script that automatically backs up your game saves in case something bad happens (as we know it always does).<br /><br />

Script uses your newest save in the selected gamemode and saves it into the newly created ```Backup``` folder in the ```C:\Users\USERNAME\Zomboid\Saves``` location.

# How to use on your computer?
In order to use this code, you can simply load it into your Visual Studio Code with python installed and launch.<br /><br />

If you want to make it into an .exe file (like i prefer) you need to use ``PyInstaller``.<br />
If you don't have it you can install it using this line in the terminal: ```pip install pyinstaller```,<br />
then simply enter: ```pyinstaller --onefile main.py``` while inside the folder containing the main.py file.<br /><br />

You can find the .exe file in the ```dist``` folder

# Program Usage
![Choosing folder](/screenshots/1.png)

![Choosing interval](/screenshots/2.png)

![Choosing number of folders](/screenshots/3.png)

![Backup in progress](/screenshots/4.png)

![Created backups](/screenshots/5.png)
