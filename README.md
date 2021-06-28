# PC Butler :coffee:
Voice controlled PC butler 

## Index
[Installation](https://github.com/enterlineconnor/pc_butler#installation) \
[Usage](https://github.com/enterlineconnor/pc_butler#usage) 
# Installation
PyAudio doesn't seem to install successfully on windows via the pip installer. (not tested on Linux/Mac)

Download the version cooresponding to your python version, cd to the download directory and pip install it seperately.

Installation versions of [PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)


Ex:
```
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```

All other modules can be installed from the requirements.txt

```
pip install -r requirements.txt
```

# Usage

The butler will not run any action until explicitly addressed.

for example, the phrase below will only trigger the bot when it hears it's name. In this case his name is Roger.

```
I Would Like You To Do Something For Me Roger
```

Once addressed, the butler will ask you to fulfill a service.

You may respond with any of the following requests:

- "Play" or "Start" 
  - This will attempt to run an application addressed after the keywords
  - seems to only work for applications installed on the same drive as Python
  
Example:

```
play dead by daylight
```

- "Restart"
  - This will reboot your pc immediately

```
restart my PC
```

- "Shut Down"
  - This will shut down your pc immediately

```
shut down my PC
```