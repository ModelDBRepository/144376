# $Id: geom.py,v 1.30 2011/01/02 19:56:14 samn modified by yosefs Exp $ 

from pyinit import *

class Synapse:
	def __init__(self, sect, loc, tau1, tau2, e):
		self.syn		= h.MyExp2SynBB(loc, sec=sect)
		self.syn.tau1	= tau1
		self.syn.tau2	= tau2
		self.syn.e		= e 
		
class SynapseNMDA:
	def __init__(self, sect, loc, tau1, tau2, tau1NMDA, tau2NMDA, r, e):
		self.syn			= h.MyExp2SynNMDABB(loc, sec=sect)
		self.syn.tau1		= tau1
		self.syn.tau2		= tau2
		self.syn.tau1NMDA	= tau1NMDA
		self.syn.tau2NMDA	= tau2NMDA 
		self.syn.r			= r
		self.syn.e			= e 
		
###############################################################################
#
# General Cell
#
###############################################################################
class Cell:
	"General cell"
	
	def __init__(self,x,y,z,id):
		self.x=x
		self.y=y
		self.z=z
		self.id=id
		self.all_sec = []
		self.add_comp('soma',True)
		self.set_morphology()
		self.set_conductances()
		self.set_synapses()
		self.set_inj()
		self.calc_area()
		
	def set_morphology(self):
		pass
			
	def set_conductances(self):
		pass
		
	def set_synapses(self):
		pass
		
	def set_inj(self):
		self.somaInj = h.IClamp(0.5, sec=self.soma)	
		
	def add_comp(self, name, rec):
		self.__dict__[name] = h.Section()
		self.all_sec.append(self.__dict__[name])
		# Record voltage
		if rec:
			self.__dict__[name+"_volt"] = h.Vector(int(h.tstop/h.dt)+1)
			self.__dict__[name+"_volt"].record(self.__dict__[name](0.5)._ref_v)
	
	def plot_volt(self, name, fig=1):
		figure(fig)
		volt = self.__dict__[name+"_volt"].to_python()
		plot(arange(len(volt))*h.dt, volt)
		
	def calc_area(self):
		self.total_area = 0
		self.n = 0
		for sect in self.all_sec:
			self.total_area += h.area(0.5,sec=sect)
			self.n+=1
#############################################################################
#
# Winograd Cell - Saturating
#
#############################################################################			
class WinoSat(Cell):
	"Winograd cell"
	
	def set_morphology(self):
		total_area = 3488.3129795210225 # um2
		self.soma.nseg  = 1
		self.soma.cm    = 1      # uF/cm2
		diam = 18.8#sqrt(total_area) # um
		L    = 18.8#diam/pi # um
		self.soma.Ra = 123

					
		h.pt3dclear(sec=self.soma)
		h.pt3dadd(self.x, self.y, self.z,   diam, sec=self.soma)
		h.pt3dadd(self.x, self.y, self.z+L, diam, sec=self.soma)
			
	def set_conductances(self):
		self.soma.insert('ppasi')
		self.soma.e_ppasi = -70     # mV
		self.soma.g_ppasi = .001  # S/cm2 
	  
		self.soma.insert('hh3')
		self.soma.gnabar_hh3=0.07 
		self.soma.gkbar_hh3=0.007
		self.soma.insert('im')
		self.soma.gkbar_im = 4e-6 
		h.taumax_im = 4000
		 
		self.soma.insert('iL')
		self.soma.pca_iL = 2.76e-4
		self.soma.insert('cada')
		h.taur_cada = 20
		h.depth_cada = 1 
		self.soma.insert('iar')
		self.soma.ghbar_iar=0.00002
		h.cac_iar = 0.006
		h.k2_iar = 1e-4 #change to 1e-5 for non-saturating model
		h.k4_iar = 0.008 #change to .001
		self.soma.eh = -20
	def set_inj(self):
		self.curr2 = h.Ipulse3(.5,sec=self.soma)
		self.curr2.delay = 10000
		self.curr2.dur=4000
		self.curr2.per = self.curr2.delay + self.curr2.dur
		self.curr2.num = 100
		for i in range(0,int(self.curr2.num -1)):
			self.curr2.amp[i] = -.3
		self.curr2.dc = .232
		self.APC = h.APCounter2(.5,sec =self.soma)
		#self.eh = -20

#############################################################################
#
# Winograd Cell - Non-Saturating
#
#############################################################################			
class WinNonS(Cell):
	"Winograd cell"
	
	def set_morphology(self):
		total_area = 3488.3129795210225 # um2
		self.soma.nseg  = 1
		self.soma.cm    = 1      # uF/cm2
		diam = 18.8#sqrt(total_area) # um
		L    = 18.8#diam/pi # um
		self.soma.Ra = 123

					
		h.pt3dclear(sec=self.soma)
		h.pt3dadd(self.x, self.y, self.z,   diam, sec=self.soma)
		h.pt3dadd(self.x, self.y, self.z+L, diam, sec=self.soma)
			
	def set_conductances(self):
		self.soma.insert('ppasi')
		self.soma.e_ppasi = -70     # mV
		self.soma.g_ppasi = .001  # S/cm2 
	  
		self.soma.insert('hh3')
		self.soma.gnabar_hh3=0.07 
		self.soma.gkbar_hh3=0.007
		self.soma.insert('im')
		self.soma.gkbar_im = 4e-6 
		h.taumax_im = 4000
		 
		self.soma.insert('iL')
		self.soma.pca_iL = 2.76e-4
		self.soma.insert('cada')
		h.taur_cada = 20
		h.depth_cada = 1 
		self.soma.insert('iar')
		self.soma.ghbar_iar=0.00002
		h.cac_iar = 0.006
		h.k2_iar = 1e-5 #change to 1e-5 for non-saturating model
		h.k4_iar = 0.001 #change to .001
		self.soma.eh = -20
	def set_inj(self):
		self.curr2 = h.Ipulse3(.5,sec=self.soma)
		self.curr2.delay = 10000
		self.curr2.dur=4000
		self.curr2.per = self.curr2.delay + self.curr2.dur
		self.curr2.num = 100
		for i in range(0,int(self.curr2.num -1)):
			self.curr2.amp[i] = -.3
		self.curr2.dc = .232
		self.APC = h.APCounter2(.5,sec =self.soma)
		#self.eh = -20

#############################################################################
#
# Winograd Cell - Non-Saturating No-Ih
#
#############################################################################			
class WinNoIh(Cell):
	"Winograd cell"
	
	def set_morphology(self):
		total_area = 3488.3129795210225 # um2
		self.soma.nseg  = 1
		self.soma.cm    = 1      # uF/cm2
		diam = 18.8#sqrt(total_area) # um
		L    = 18.8#diam/pi # um
		self.soma.Ra = 123

					
		h.pt3dclear(sec=self.soma)
		h.pt3dadd(self.x, self.y, self.z,   diam, sec=self.soma)
		h.pt3dadd(self.x, self.y, self.z+L, diam, sec=self.soma)
			
	def set_conductances(self):
		self.soma.insert('ppasi')
		self.soma.e_ppasi = -70     # mV
		self.soma.g_ppasi = .001  # S/cm2 
	  
		self.soma.insert('hh3')
		self.soma.gnabar_hh3=0.07 
		self.soma.gkbar_hh3=0.007
		self.soma.insert('im')
		self.soma.gkbar_im = 4e-6 
		h.taumax_im = 4000
		 
		self.soma.insert('iL')
		self.soma.pca_iL = 2.76e-4
		self.soma.insert('cada')
		h.taur_cada = 20
		h.depth_cada = 1 
		#self.soma.insert('iar')
		#self.soma.ghbar_iar=0.00002
		#h.cac_iar = 0.006
		#h.k2_iar = 1e-4 #change to 1e-5 for non-saturating model
		#h.k4_iar = 0.008 #change to .001
		#self.soma.eh = -20
	def set_inj(self):
		self.curr2 = h.Ipulse3(.5,sec=self.soma)
		self.curr2.delay = 10000
		self.curr2.dur=4000
		self.curr2.per = self.curr2.delay + self.curr2.dur
		self.curr2.num = 100
		for i in range(0,int(self.curr2.num -1)):
			self.curr2.amp[i] = -.3
		self.curr2.dc = .232
		self.APC = h.APCounter2(.5,sec =self.soma)
		#self.eh = -20
###############################################################################
#
# Basket Cell -- Bwb
#
###############################################################################

class Bwb(Cell):
	"Basket cell"
	
	def set_morphology(self):
		total_area = 10000 # um2
		self.soma.nseg  = 1
		self.soma.cm    = 1      # uF/cm2
		diam = sqrt(total_area) # um
		L    = diam/pi  # um
			
		h.pt3dclear(sec=self.soma)
		h.pt3dadd(self.x, self.y, self.z,   diam, sec=self.soma)
		h.pt3dadd(self.x, self.y, self.z+L, diam, sec=self.soma)
			
	def set_conductances(self):
		self.soma.insert('pas')
		self.soma.e_pas = -65     # mV
		self.soma.g_pas = 0.1e-3  # S/cm2 
	  
		self.soma.insert('Nafbwb')
		self.soma.insert('Kdrbwb')
	   
	def set_synapses(self):
		self.somaAMPAf 	= Synapse(sect=self.soma, loc=0.5, tau1=0.05, tau2=5.3, e=0)
		self.somaGABAf 	= Synapse(sect=self.soma, loc=0.5, tau1=0.07, tau2=9.1, e=-80)
		self.somaGABAss	= Synapse(sect=self.soma, loc=0.5, tau1=20,   tau2=40, e=-80)#only for septal input
		self.somaNMDA 	= SynapseNMDA(sect=self.soma, loc=0.5, tau1=0.05, tau2=5.3, tau1NMDA=15, tau2NMDA=150, r=1, e=0)
