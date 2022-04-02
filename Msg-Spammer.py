import random 
import pyautogui as pg 
import time

animal = ('ablahm','ahmagh','kooni')

time.sleep(8)

for i in range(100):
    a = random.choice(animal)
    pg.write("you are a " + a )
    pg.press('enter')
