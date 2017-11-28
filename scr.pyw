from PIL import ImageGrab
import win32api
import win32console
import win32gui
import time
#win = win32console.GetConsoleWindow()
#win32gui.ShowWindow(win, 0)
def take_screenshot(tm):
	c = 0
	while True:
		time.sleep(tm)
		ImageGrab.grab().save("E:\img"+str(c)+".jpg", "JPEG")
		c += 1

if __name__ == '__main__':
	take_screenshot(10)