import webbrowser
import time
import pyautogui as pls
"""
while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
"""
webbrowser.open('http://tanksw.com/piano-tiles/')

time.sleep(3)

pls.click(x=755, y=350)
pls.click(clicks=2, interval=0.5)

time.sleep(2)

while True:
	if pls.pixelMatchesColor(544,630,(17,17,17),tolerance=10):
		pls.click(x=544, y=630)
	elif pls.pixelMatchesColor(624,630,(17,17,17),tolerance=10):
		pls.click(x=624, y=630)
	elif pls.pixelMatchesColor(718,630,(17,17,17),tolerance=10):
		pls.click(x=718, y=630)	
	elif pls.pixelMatchesColor(810,630,(17,17,17),tolerance=10):
		pls.click(x=810, y=630)
		
