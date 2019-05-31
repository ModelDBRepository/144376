from neuron import *
from geoms import *
from winograd import *
#ngraph=0
pinit()
makeWinNonIh()

soma = cells[0].soma
winographNoIh()
h.tstop = 66000
h.run()
