import numpy
import tabox
import talib

close = numpy.random.random(100)


close = numpy.array([1,2,3,4,5,6,7,8,9], dtype=numpy.float64)
# output = tabox.SMA(close, timeperiod=3)
output = tabox.ASIN(close)
print(output)
output = talib.ASIN(close)
print(output)