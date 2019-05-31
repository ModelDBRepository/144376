#from neuron import *
from geoms import *
from winograd import *
#ngraph=0
pinit()
makeWinNon()

soma = cells[0].soma
winograph()
h.tstop = 66000
h.run()
