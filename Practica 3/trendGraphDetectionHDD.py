import sys
import rrdtool
import datetime
from  Notify import send_alert_attached
import time

def generarGraficaHDD(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv("deteccionHDD.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=HDD load",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "--title=Carga del HDD del agente Usando SNMP y RRDtools \n Detección de umbrales",
                         "DEF:cargaHDD=trend.rrd:HDDload:AVERAGE",
                         "VDEF:cargaMAX=cargaHDD,MAXIMUM",
                         "VDEF:cargaMIN=cargaHDD,MINIMUM",
                         "VDEF:cargaSTDEV=cargaHDD,STDEV",
                         "VDEF:cargaLAST=cargaHDD,LAST",
                         "CDEF:umbral70=cargaHDD,70,LT,0,cargaHDD,IF",
                         "CDEF:umbral80=cargaHDD,80,LT,0,cargaHDD,IF",
                         "CDEF:umbral90=cargaHDD,90,LT,0,cargaHDD,IF",
                         "AREA:cargaHDD#00FF00:Carga del HDD",
                         "AREA:umbral70#FF9F00:Carga HDD mayor de 70",
                         "AREA:umbral80#FF5E00:Carga HDD mayor de 80",
                         "AREA:umbral90#FF0000:Carga HDD mayor de 90",
                         "HRULE:70#0088FF:Umbral  70%",
                         "HRULE:80#0088FF:Umbral  80%",
                         "HRULE:90#0088FF:Umbral  90%",
                         "PRINT:cargaLAST:%6.2lf",
                         "GPRINT:cargaMIN:%6.2lf %SMIN",
                         "GPRINT:cargaSTDEV:%6.2lf %SSTDEV",
                         "GPRINT:cargaLAST:%6.2lf %SLAST")
    print (ret)

while (1):
    time.sleep(60)
    ultima_actualizacion = rrdtool.lastupdate("trend.rrd")
    timestamp=ultima_actualizacion['date'].timestamp()
    dato=ultima_actualizacion['ds']["HDDload"]
    print(dato)

    if dato >= 70 and dato < 80:
        generarGraficaHDD(int(timestamp))
        send_alert_attached("Umbral Ready en HDD", "deteccionHDD.png")
        print("sobrepasa el umbral")

    if dato >= 80 and dato < 90:
        generarGraficaHDD(int(timestamp))
        send_alert_attached("Umbral Set en HDD", "deteccionHDD.png")
        print("sobrepasa el umbral")

    if dato >= 90:
        generarGraficaHDD(int(timestamp))
        send_alert_attached("Umbral Go en HDD", "deteccionHDD.png")
        print("sobrepasa el umbral")