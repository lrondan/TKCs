from tkinter import messagebox as MBox
import dns.resolver
from os import path

def main():
	if path.exists('subdominios/subdominios.txt'):
		wordlist = open('subdominios/subdominios.txt','r')
		wordlist = wordlist.read().split('\n')
		lista = []
		for s in wordlist:
			try:
				a = dns.resolver.query('{}.google.com'.format(s),'A')
				lista.append('{}.google.com'.format(s))
			except:
				pass
		if len(lista) > 0:
			MBox.showinfo('Subdominios','Numero de subdominios posibles: {}'.format(len(lista)))
			for e in lista:
				print(e)
		else:
			MBox.showerror('Error',"No se encontraron subdominios")
	else:
		MBox.showerror('Error',"No existe el archivo subdominios.txt")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()