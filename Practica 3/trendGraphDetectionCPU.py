import sys
import rrdtool
import datetime
from  Notify import send_alert_attached
import time

def generarGraficaCPU(ultima_lectura):
    tiempo_final = int(ultima_lectura)
    tiempo_inicial = tiempo_final - 1800
    ret = rrdtool.graphv("deteccionCPU.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Cpu load",
                         '--lower-limit', '0',
                         '--upper-limit', '100',
                         "--title=Carga del CPU del agente Usando SNMP y RRDtools \n Detección de umbrales",
                         "DEF:cargaCPU=trend.rrd:CPUload:AVERAGE",
                         "VDEF:cargaMAX=cargaCPU,MAXIMUM",
                         "VDEF:cargaMIN=cargaCPU,MINIMUM",
                         "VDEF:cargaSTDEV=cargaCPU,STDEV",
                         "VDEF:cargaLAST=cargaCPU,LAST",
                         "CDEF:umbral70=cargaCPU,70,LT,0,cargaCPU,IF",
                         "CDEF:umbral80=cargaCPU,80,LT,0,cargaCPU,IF",
                         "CDEF:umbral90=cargaCPU,90,LT,0,cargaCPU,IF",
                         "AREA:cargaCPU#00FF00:Carga del CPU",
                         "AREA:umbral70#FF9F00:Carga CPU mayor de 70",
                         "AREA:umbral80#FF5E00:Carga CPU mayor de 80",
                         "AREA:umbral90#FF0000:Carga CPU mayor de 90",
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
    dato=ultima_actualizacion['ds']["CPUload"]
    print(dato)

    if dato >= 70 and dato < 80:
        generarGraficaCPU(int(timestamp))
        send_alert_attached("Umbral Ready en CPU", "deteccionCPU.png")
        print("sobrepasa el umbral")

    if dato >= 80 and dato < 90:
        generarGraficaCPU(int(timestamp))
        send_alert_attached("Umbral Set en CPU", "deteccionCPU.png")
        print("sobrepasa el umbral")

    if dato >= 90:
        generarGraficaCPU(int(timestamp))
        send_alert_attached("Umbral Go en CPU", "deteccionCPU.png")
        print("sobrepasa el umbral")