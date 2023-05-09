import sys
import rrdtool
import datetime
from  Notify import send_alert_attached
import time

def generarGraficaRAM(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv("deteccionRAM.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=RAM load",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "--title=Carga del RAM del agente Usando SNMP y RRDtools \n Detección de umbrales",
                         "DEF:cargaRAM=trend.rrd:RAMload:AVERAGE",
                         "VDEF:cargaMAX=cargaRAM,MAXIMUM",
                         "VDEF:cargaMIN=cargaRAM,MINIMUM",
                         "VDEF:cargaSTDEV=cargaRAM,STDEV",
                         "VDEF:cargaLAST=cargaRAM,LAST",
                         "CDEF:umbral75=cargaRAM,75,LT,0,cargaRAM,IF",
                         "CDEF:umbral80=cargaRAM,80,LT,0,cargaRAM,IF",
                         "CDEF:umbral85=cargaRAM,85,LT,0,cargaRAM,IF",
                         "AREA:cargaRAM#00FF00:Carga del RAM",
                         "AREA:umbral75#FF9F00:Carga RAM mayor de 75",
                         "AREA:umbral80#FF5E00:Carga RAM mayor de 80",
                         "AREA:umbral85#FF0000:Carga RAM mayor de 85",
                         "HRULE:75#0088FF:Umbral  75%",
                         "HRULE:80#0088FF:Umbral  80%",
                         "HRULE:85#0088FF:Umbral  85%",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST")
    print (ret)

while (1):
    time.sleep(65)
    ultima_actualizacion = rrdtool.lastupdate("trend.rrd")
    timestamp=ultima_actualizacion['date'].timestamp()
    dato=ultima_actualizacion['ds']["RAMload"]
    print(dato)

    if dato >= 75 and dato < 80:
        generarGraficaRAM(int(timestamp))
        send_alert_attached("Umbral Ready en RAM", "deteccionRAM.png")
        print("sobrepasa el umbral")

    if dato >= 80 and dato < 85:
        generarGraficaRAM(int(timestamp))
        send_alert_attached("Umbral Set en RAM", "deteccionRAM.png")
        print("sobrepasa el umbral")

    if dato >= 85:
        generarGraficaRAM(int(timestamp))
        send_alert_attached("Umbral Go en RAM", "deteccionRAM.png")
        print("sobrepasa el umbral")