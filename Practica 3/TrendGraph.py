import rrdtool
import time

ultima_lectura = int(rrdtool.last("trend.rrd"))
tiempo_final = ultima_lectura + 600
tiempo_inicial = tiempo_final - 1500

rrdtool.graphv("trendCPU.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
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
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )

rrdtool.graphv("trendRAM.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
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
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )

rrdtool.graphv("trendHDD.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_final),
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
                     "GPRINT:cargaLAST:%6.2lf %SLAST" )