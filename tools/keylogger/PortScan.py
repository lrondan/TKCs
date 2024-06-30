#!/usr/bin/env python

from concurrent.futures import ThreadPoolExecutor as executor
import socket
import time
import sys
import argparse

start = time.time()

def printer(shit):
	sys.stdout.write(shit+"               \r")
	sys.stdout.flush()
	return True


def scan(ip,port,l):
	printer("Testing Port: "+str(port))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	space = 10 - l
	space = " " * space
	if s.connect_ex((ip,port)):
		return None
	else :
		try:
			service = socket.getservbyport(port)
			print(str(port) + "/TCP" + space + service)
		except socket.error:
			print(str(port) + "/TCP" + space + "Unknown")

		except KeyboardInterrupt:
			print("[-] Exiting!")
			exit(1)

	return True




def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", help="Target IP/Host", type=str)
	parser.add_argument("-d", "--thread", help="threads number (Default 5)", type=int)
	parser.add_argument("-p", "--port", help="Ports range (Example: -p 20-1024)", type=str)
	args = parser.parse_args()

	target = str(args.target)
	thread = args.thread
	ports = str(args.port)

	if target == "None":
		parser.print_help()
		exit(1)
	if thread == None:
		thread = 5

	if ports == "None":
		ports = range(65535)
		p = "1-65535"
	else:
		try:
			p = ports
			ports = ports.split("-")
			ports = range(int(ports[0]), int(ports[1]))
		except IndexError:
			print("-p/--port, should be a range of ports, Example: -p 20-1024")
			exit(1)

	print("[+] Target: ",target)
	print("[+] Threads: "+str(thread))
	print("[+] Ports: "+p)
	print("\n[+] Start The Scan\n")
	print("PORT          SERVICE")
	print("----          -------")

	with executor(max_workers=int(thread)) as exe:
		try:
			[exe.submit(scan, target, port, len(str(port))) for port in ports]
		except KeyboardInterrupt:
			print("[-] Exiting!")
			exit(1)



	took = time.time() - start
	t = str(took).split('.')[0]
	m = int(t) / 60
	s = int(t) % 60
	
	print("                            \r")
	print("[+] Took: "+str(m)+":"+str(s))

	intdas= input('')


if __name__ == '__main__':
	main()
