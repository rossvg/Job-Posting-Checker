# Job-Posting-Checker
Python script to check if a job posting is still available on a website, and then pushes a windows 10 notification. Run from a batch file with minimized command window.

## Dependencies
* Windows 10 OS
* Python 3.8.2

## Python Packages
* Beautiful Soup
* Plyer

## Setup 
1. [Download and install Python 3.8.2](https://www.python.org/downloads/)

2. Use PIP to download the following packages from the command line:
* ```pip install beautifulsoup4```
* ```pip install plyer```

3. Download script and batch file

4(Optional). Change the 'CheckJob' method arguments in JobNotification.py to prefered website URL and job title. Must match website exactly. Reference comments for help.
The script comes pre-loaded with example job postings from google. Can also customize notifications.

5. Change run_python_script.bat to the file location of python and the script as seen below
```
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
"<python.exe path goes here!>" "<JobNotification.py file path goes here!>"
exit
```

## Usage
Execute run_python_script.bat
