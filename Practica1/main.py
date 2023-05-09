from getSNMP import consultaSNMP

def Agregar():
    archivo = open("SNMP.txt", "r")
    inf = archivo.readlines()
    archivo2 = open("SNMP.txt", "w")
    for i in range(len(inf)):
        linea = str(i) + inf[i][1:]
        archivo2.write(linea)
    comunidad = input("Comunidad: ")
    version = input("Versiòn SNMP: ")
    puerto = input("Puerto: ")
    ip = input("IP: ")
    archivo2.write(str(len(inf))+'-')
    archivo2.write(comunidad + ',')
    archivo2.write(version + ',')
    archivo2.write(puerto + ',')
    archivo2.write(ip + '\n')
    archivo2.close()
    archivo.close()

def Cambiar():
    archivo = open("SNMP.txt", "r")
    inf = archivo.readlines()
    print(inf)
    agente = input("Elige un agente a modificar: ")
    archivo2 = open("SNMP.txt", "w")

    for linea in inf:
        if linea[0] == agente:
            comunidad = input("Comunidad: ")
            version = input("Versiòn SNMP: ")
            puerto = input("Puerto: ")
            ip = input("IP: ")
            archivo2.write(linea[0] + '-')
            archivo2.write(comunidad + ',')
            archivo2.write(version + ',')
            archivo2.write(puerto + ',')
            archivo2.write(ip + '\n')
        else:
            archivo2.write(linea)
    archivo.close()
    archivo2.close()



def Eliminar():
    archivo = open("SNMP.txt", "r")
    inf = archivo.readlines()
    print(inf)
    agente = input("Elige un agente: ")
    archivo2 = open("SNMP.txt", "w")
    for linea in inf:
        if linea[0] != agente:
            archivo2.write(linea)
    archivo.close()
    archivo2.close()
    archivo = open("SNMP.txt", "r")
    inf = archivo.readlines()
    archivo2 = open("SNMP.txt", "w")
    for i in range(len(inf)):
        linea = str(i) + inf[i][1:]
        archivo2.write(linea)


def Reporte():
    estados = {" 1": "Up", " 2": "Down", " 3": "Testing", " 4": "Unknown", " 5": "Dormant", " 6": "NotPresent",
               "7": "LoweLayerDown"}
    archivo = open("SNMP.txt", "r")
    informacion = archivo.read()
    print(informacion)
    lista = informacion.split("\n")
    agente = input("Elige un agente: ")
    for i in range(len(lista)):
        opcion = lista[i].split("-")
        if opcion[0] == agente:

            from reportlab.pdfgen import canvas
            from reportlab.platypus import Table
            from reportlab.lib import colors
            partes = opcion[1].split(",")
            pdf = canvas.Canvas("Reporte.pdf")
            pdf.setFont("Helvetica", 32)
            pdf.drawString(60, 750, "Administraciòn de Servicios en Red")
            pdf.drawString(60, 710, "Practica 1")
            pdf.drawString(60, 670, "Flores Escalona David 4CM14")

            SO = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.1.1.0').split("-")
            nombre = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.1.5.0')
            contacto = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.1.4.0')
            ubicacion = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.1.6.0')
            interfaces = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.2.1.0')
            pdf.setFont("Helvetica", 12)
            pdf.drawString(56, 600, SO[0])
            pdf.drawString(56, 580, SO[1])
            if " Windows" in SO[0] or " Windows" in SO[1]:
                pdf.drawImage("Windows.jpg", 410, 450, width=100, height=100)
            else:
                pdf.drawImage("Ubuntu.jpg", 390, 450, width=200, height=160)

            pdf.drawString(60, 560, "Nombre del dispositivo: "+nombre)
            pdf.drawString(60, 540, "Informacion de contacto: "+contacto)
            pdf.drawString(60, 520, "Ubicacion: "+ubicacion)
            pdf.drawString(60, 500, "Numero de interfaces: "+interfaces)
            datos = [["Descripcion","Estado"]]
            if int(interfaces) > 5:
                for i in range(1, 6):
                    desc = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.2.2.1.2.'+str(i))
                    estado = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.2.2.1.7.'+str(i))
                    datos.append((desc, estados[estado]))
            else:
                for i in range(1,int(interfaces)+1):
                    desc = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.2.2.1.2.' + str(i))
                    estado = consultaSNMP(partes[0], partes[3], '1.3.6.1.2.1.2.2.1.7.' + str(i))
                    datos.append((desc, estados[estado]))

            tabla = Table(datos)
            tabla.setStyle([
                ("BACKGROUND", (0,0), (1,0), colors.grey)
            ])
            tabla.wrapOn(pdf, 0, 0)
            tabla.drawOn(pdf, 60, 250)
            pdf.save()
            break
    archivo.close


opciones = {"1": Agregar, "2": Cambiar, "3": Eliminar, "4": Reporte}

while 1:
    print("Practica 1 -Adquisiciòn de Informaciòn \n "
          "Flores Escalona David 4CM14 2020630128 \n"
          "Elige una opciòn: \n"
          "1) Agregar dispositivo\n"
          "2) Cambiar informacion de dispositivo\n"
          "3) Eliminar dispositivo\n"
          "4) Generar reporte\n")

    elegir = input("")
    if elegir in opciones:
        opciones[elegir]()
    else:
        print("Opcion invalida")
