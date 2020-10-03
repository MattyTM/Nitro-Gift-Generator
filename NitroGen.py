#Nitro Generator by Matty#8952
#Discord server: https://discord.gg/UgJhHu7
import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes,re, os.path
import colorama
from colorama import Fore, init, Style, Back

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
def MainMenu():
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                   Generador De Discord Nitro - By Matty#8952")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [1] "+Fore.BLUE+"Generar")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [2] "+Fore.BLUE+"Creditos")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [3] "+Fore.BLUE+"Salir")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	pass
MainMenu()
opcion = int(input("Opcion: "))

if opcion==1:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                   Generador De Discord Nitro - By Matty#8952")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	cantidad= int(input("Cantidad a generar: "))
	while(int(count)<int(cantidad)):
	    Generated = "https://discord.gift/"+random.choice(string.ascii_letters + string.digits)+"".join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
	    f= open(current_path+"/"+str("Codigos Nitro")+str("")+".txt","a") 
	    f.write(Generated+"\n")
	    print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Codigo Generado :> "+Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK+ Generated)
	    count+=1
	input(Style.BRIGHT + Fore.RED + Back.BLACK+"\nSe generaron los codigos correctamente.\nGracias por usar mi generador! Ya podes cerrar esta ventana")
	pass

if opcion==2:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                   Generador Discord Nitro"+Fore.WHITE+" Hecho por "+Fore.RED+"Matty#8952\n")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [Github] "+Fore.RED+"MattyTM")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [Discord] "+Fore.RED+"Matty#8952")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [Server] "+Fore.RED+"https://discord.gg/nKME7C7")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	input(Style.BRIGHT + Fore.RED + Back.BLACK +"\nEnter para cerrar el programa...")
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                  Cerrando!")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	time.sleep(2)
	sys.exit()
	pass

if opcion==3:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                  Cerrando!")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	time.sleep(2)
	sys.exit()
	pass
