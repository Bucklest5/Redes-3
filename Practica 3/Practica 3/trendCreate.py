import rrdtool
ret = rrdtool.create("trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPUload:GAUGE:60:0:100",
                     "DS:RAMload:GAUGE:60:0:100",
                     "DS:HDDload:GAUGE:60:0:100",
                     "RRA:AVERAGE:0.5:1:720")
if ret:
    print (rrdtool.error())
