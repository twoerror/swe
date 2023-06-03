import tkinter as tk
import threading
import os 
import requests #Модуль для открытия ссылок
import io, zipfile

def main_def():
	root = tk.Tk()
	root.geometry("400x300")

	def install_check():
		global t1
		t1 = threading.Thread(target=install)
		t1.start()
		schedule_check(t1)

	global button1
	button1 = tk.Button(root, text = "Скачать лаунчер", font = ("Courier", 15), command = install_check, borderwidth = 0.5)
	button1.place(x = 100, y = 100)

	def schedule_check(t):
		root.after(1000, check_if_done, t1)
	def check_if_done(t):
		if t.is_alive():
			schedule_check(t1)
			button1.destroy()
			label2 = tk.Label(root, text="Идет установка лаунчера...", font = ("Courier", 20))
			label2.place(x = 100, y = 100)
		if not t.is_alive():
			label3 = tk.Label(root, text="Лаунчер установлен", font = ("Courier", 20))
			label3.place(x = 100, y = 100)
	def install():
		url1 = 'https://getfile.dokpub.com/yandex/get/https://disk.yandex.ru/d/Ib3d8F6UR1LowQ' 
		r = requests.get(url1)
		nowpath = os.getcwd()
		z = zipfile.ZipFile(io.BytesIO(r.content))
		z.extractall(nowpath)
	root.mainloop()
main_def()