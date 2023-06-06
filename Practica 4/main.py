import telnetlib
from ftplib import FTP
def Generar():
    host = input("Introduce una ip ")
    with telnetlib.Telnet(host) as tn:
        tn.read_until(b"User: ")
        tn.write('rcp'.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write('rcp'.encode('ascii') + b"\n")
        tn.write(b"enable\r")
        tn.write('copy run start'.encode('ascii') + b"\r")
        tn.write(b"exit\r")
        tn.write(b"exit\r")
        tn.read_all()
        print('Configuracion actualizada'.format(host))
def Descargar():
    host = input("Introduce una ip ")
    username = 'rcp'
    password = 'rcp'
    try:
        ftp = FTP(host)
        ftp.login(username,password)
        archivos = 'startup-config'
        with open(archivos,'wb') as archivo:
            ftp.retrbinary('RETR '+ archivos, archivo.write)
        ftp.quit();
        print("El archivo se ha descargado correctamente")
    except ConnectionRefusedError:
        print("No se pudo establecer la conexion")
def Importar():
    host = input("Introduce una ip ")
    username = 'rcp'
    password = 'rcp'
    try:
        ftp = FTP(host)
        ftp.login(username,password)
        archivos = 'startup-config'
        with open(archivos,'rb') as archivo:
            ftp.storbinary('STOR '+ archivos, archivo)
        ftp.quit();
        print("El archivo se ha importado correctamente")
    except ConnectionRefusedError:
        print("No se pudo establecer la conexion")

opciones = {"1": Generar, "2": Descargar, "3": Importar}

while 1:
    print("Practica 4 - Administracion de configuracion \n "
          "Flores Escalona David 4CM14 2020630128 \n"
          "Elige una opciòn: \n"
          "1) Generar configuracion\n"
          "2) Descargar configuracion\n"
          "3) Importar configuracion\n")

    elegir = input("")
    if elegir in opciones:
        opciones[elegir]()
    else:
        print("Opcion invalida")