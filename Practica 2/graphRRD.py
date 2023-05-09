import sys
import rrdtool
import time

def Imagenes(tiempo_inicial, tiempo_final):
    rrdtool.graph( "traficoMulticast.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Bytes/s",
                         "--title=Paquetes multicast que ha recibido \n la interfaz de red de un agente",
                         "DEF:traficoEntrada=trafico.rrd:Mul:AVERAGE",
                         "CDEF:escalaIn=traficoEntrada,8,*",
                         "LINE1:escalaIn#FF0000:Paquetes multicast recibidos")

    rrdtool.graph( "traficoIP.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Bytes/s",
                         "--title=Paquetes recibidos exitosamente \n entregados a protocolos IP",
                         "DEF:traficoEntrada=trafico.rrd:IP:AVERAGE",
                         "CDEF:escalaIn=traficoEntrada,8,*",
                         "LINE1:escalaIn#FF0000:Paquetes recibidos")

    rrdtool.graph( "traficoICMP.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Bytes/s",
                         "--title=Mensajes de respuesta ICMP \n que ha enviado el agente",
                         "DEF:traficoEntrada=trafico.rrd:ICMP:AVERAGE",
                         "CDEF:escalaIn=traficoEntrada,8,*",
                         "LINE1:escalaIn#FF0000:Mensajes de respuesta")

    rrdtool.graph( "traficoEnviados.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Bytes/s",
                         "--title=Segmentos enviados que excluyen los \n octetos retransmitidos",
                         "DEF:traficoEntrada=trafico.rrd:Enviados:AVERAGE",
                         "CDEF:escalaIn=traficoEntrada,8,*",
                         "LINE1:escalaIn#FF0000:Segmentos enviados")

    rrdtool.graph( "traficoDatagramas.png",
                         "--start", str(tiempo_inicial),
                         "--end", str(tiempo_final),
                         "--vertical-label=Bytes/s",
                         "--title=Datagramas recibos que no pudieron \n ser entregados ",
                         "DEF:traficoEntrada=trafico.rrd:Datagramas:AVERAGE",
                         "CDEF:escalaIn=traficoEntrada,8,*",
                         "LINE1:escalaIn#FF0000:Datagramas recibidos")