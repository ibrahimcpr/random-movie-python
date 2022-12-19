import random
import pyautogui as p
import linecache
while True:
    x=random.randint(0,249)
    line = linecache.getline(r"film.txt",x)
    check=p.confirm(line,buttons=["watched!","thanks!"])
    if check!="watched!":
        break
