# imports

from neuron import *
from geoms import *
h.load_file("nrngui.hoc")
#h.load_file("simgui.hoc")
h.nrnmainmenu()		#	// create main menu
h.nrncontrolmenu()



cells = [] # list of cells
ncl = [] # list of NetCons used to record cell action potentials (spikes)
ltimevec = [] # list of Vectors to record cell spikes
lidvec = []

# make the cells
def makeCells():
    cellID = 0
    cell = WinoSat(0,0,0,cellID) #Winograd Cells
    cells.append(cell)
def makeWinoSat():
    cellID = 0
    cell = WinoSat(0,0,0,cellID)
    cells.append(cell)
def makeWinNon():
    cellID = 0
    cell = WinNonS(0,0,0,cellID)
    cells.append(cell)
def makeWinNonIh():
    cellID = 0
    cell = WinNoIh(0,0,0,cellID)
    cells.append(cell)
def pinit(tstop =66000):
    h.dt=0.1
    h.tstop = tstop
    h.runStopAt = tstop
    h.steps_per_ms = 5
    h.celsius = 36
    h.v_init = -70

def winograph():
   
    h.newPlotS()
    h.newPlotS()
    h.newPlotS()
    
    h.newPlotS()
    h.newPlotS()
    h.newPlotS()
    h.Graph[0].addexpr('p.soma.cai')
    h.Graph[0].size(0,66000,0,.0063)
    h.Graph[1].addexpr('p.cells[0].APC.rate')
    h.Graph[1].size(0,66000,0,60)
    h.Graph[2].addexpr('p.cells[0].curr2.i')
    h.Graph[2].size(0,66000,-.3,.3)
    h.Graph[3].addexpr('p.soma.p1_iar')
    
    h.Graph[3].size(0,66000,0,.1)
    h.Graph[4].addexpr('p.soma.m_iar')
    h.Graph[4].size(0,66000,0,2)
    h.Graph[5].addexpr('p.soma.v')
    h.Graph[5].size(0,66000,-80,20)
    
def winographNoIh():
    h.newPlotS()
    h.newPlotS()
    h.newPlotS()

    h.newPlotS()
    #h.newPlotS()
    #h.newPlotS()
    h.Graph[0].addexpr('p.soma.cai')
    h.Graph[0].size(0,66000,0,.0063)
    h.Graph[1].addexpr('p.cells[0].APC.rate')
    h.Graph[1].size(0,66000,0,60)
    h.Graph[2].addexpr('p.cells[0].curr2.i')
    h.Graph[2].size(0,66000,-.3,.3)
   # h.Graph[3].addexpr('p.soma.p1_iar')

   # h.Graph[3].size(0,66000,0,.1)
   # h.Graph[4].addexpr('p.soma.m_iar')
   # h.Graph[4].size(0,66000,0,2)
    h.Graph[3].addexpr('p.soma.v')
    h.Graph[3].size(0,66000,-80,20)

