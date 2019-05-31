Python Simulation of Hyperpolarization-activated graded persistent activity in
the prefrontal cortex

Reference: Winograd M, Destexhe A, Sanchez-Vives, MV.
Hyperpolarization-activated graded persistent activity in 
the prefrontal cortex.  Proc. Natl. Acad. Sci. USA
105: 7298-7303, 2008

Python Translation of: http://senselab.med.yale.edu/ModelDB/ShowModel.asp?model=113997

From Destexhe's Readme, A description of the intrinsic current:

Intrinsic currents: INa, IKd for action potentials, IM for
spike-frequency adaptation, ICaL for calcium currents, 
calcium dynamics and the hyperpolarization-activated current
Ih.  There is also a calcium regulation of Ih, which was 
taken from thalamic neurons (Destexhe et al., J Neurophysiol.,
1996)

demo_HPGA_non_saturating.py:
"non-saturating" model (Fig 4 of the paper)

demo_HPGA_non_saturating_noIh.py: 
"non-saturating" model, no Ih (Fig 4 of the paper)

demo_HPGA_saturating.py: 
"saturating" model (supplementary Fig S7 of the paper)

Usage:
After going to the Directory anr running nrnivmodl 
Autorun by opening the file called simgui.py.
This will give you a dialog box to be able to choose which figure you would like to see.
Choose a figure.  

If you would like to see a different figure, reopen simgui.py

Directions:
Under Linux:
Download the archive.
In the directory type nrnivmodl to compile the mod files
Then type 
nrngui -python
In python import simgui by typing from simgui import *
