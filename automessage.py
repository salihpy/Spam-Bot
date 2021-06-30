import pyautogui

import time

import colorama

from colorama import Fore, Back, Style

colorama.init()

	import os





#Developer By Salih.dll

print(Fore.RED)

print("1- Spam Botu Başarıyla Çalıştı, Spam Tuşu ESC'dir")
print(Fore.RED)
print("2- Detaylı Kullanım İçin İnstagram: @salih.py")


time.sleep(1)

f=open("message.txt")

for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("Esc")
	
os.system('cls||clear')

	print("Spam İşlemi Bitmiştir")
	




