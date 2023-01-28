import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"
if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\amanu\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\amanu\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "ModGenix-1 Interviewer",
    options = {"build_exe": {"packages":["tkinter","xlrd","fuzzywuzzy","os","sys"], "include_files":['icon.ico','login.xlsx','tcl86t.dll','tk86t.dll', 'Questions','words_alpha.json']}},
    version = "0.01",
    description = "An interviewing platform",
    executables = executables
    )
