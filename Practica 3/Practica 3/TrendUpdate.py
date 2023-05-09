import time
import rrdtool

from getSNMP import consultaSNMP
carga_CPU = 0
carga_RAM = 0
carga_HDD = 0

while 1:
    carga_CPU = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.25.3.3.1.2.196608'))
    totalRAM = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.25.2.3.1.5.1'))
    libreRAM = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.25.2.3.1.5.11'))

    carga_RAM = int(((totalRAM-libreRAM)/ totalRAM) * 100)
    totalHDD = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.25.2.3.1.5.36'))
    libreHDD = int(consultaSNMP('comunidadSNMP','localhost','1.3.6.1.2.1.25.2.3.1.6.36'))
    carga_HDD = int((libreHDD / totalHDD) * 100)

    valor = "N:" + str(carga_CPU) + ":" + str(carga_RAM) + ":" + str(carga_HDD)
    print (valor)
    rrdtool.update('trend.rrd', valor)
    time.sleep(5)

if ret:
    print (rrdtool.error())
    time.sleep(300)
