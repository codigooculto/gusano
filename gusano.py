import os, sys #importo el modulo para interactuar con el sistema operativo
import shutil #importo el modulo para copiar el archivo a otra direccion 

print("""  _______  __    __       _______.     ___      .__   __.   ______   
 /  _____||  |  |  |     /       |    /   \     |  \ |  |  /  __  \  
|  |  __  |  |  |  |    |   (----`   /  ^  \    |   \|  | |  |  |  | 
|  | |_ | |  |  |  |     \   \      /  /_\  \   |  . `  | |  |  |  | 
|  |__| | |  `--'  | .----)   |    /  _____  \  |  |\   | |  `--'  | 
 \______|  \______/  |_______/    /__/     \__\ |__| \__|  \______/  
                                                                     """)

print("""▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
""")

def funcion_gusano():
	global nombre #nombre creo una variable global para usarla fuera de la funcion
	if os.path.exists("archivo_gusano.py"): #creo una condicion que busque la existencia del archivo
		os.remove("archivo_gusano.py")#si encuentra el archivo lo elimina
	else:
		nombre = input("NOMBRE DEL ARCHIVO + LA EXT EXAMPLE.PY: ") #si no encuentra el archivo crea el arhivo pidiendole los datos al usuario
		abriendo_gusano = open(nombre,"x") #creando el archivo
		abriendo_gusano.close()
		escribiendo_Archivo = open(nombre,"a")
		escribiendo_Archivo.write("""
print("hola mundo")
print("has creado un script dentro de otro script")
input("PRESIONA ENTER PARA CONTINUAR...")""")
		abriendo_gusano.close()


def infeccion():
	#moviendo el archivo a otra direccion y propagando el malware
	shutil.copy(nombre , "C:/Users/Gigabyte/Desktop")
	ruta = os.access("C:/Users/Gigabyte/Desktop/"+nombre, os.F_OK)#compruebo la existencia de la ruta
	ruta = os.access("C:/Users/Gigabyte/Desktop", os.X_OK)#compruebo si la ruta es ejecutable
	if ruta == True:
		print("RUTA EXISTE Y ES EJECUTABLE".center(80))
	else:
		print("ERROR EL ARCHIVO NO SE HA GENERADO")

if __name__ == '__main__':
	funcion_gusano()
	infeccion()