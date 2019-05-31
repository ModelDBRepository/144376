from neuron import h
import os
import sys
import datetime
import shutil
import pickle
from math import sqrt, pi
import numpy

h("objref p")
h("p = new PythonObject()")

try:
    import pylab
    from pylab import plot, arange, figure
    my_pylab_loaded = True
except ImportError:
    print "Pylab not imported"
    my_pylab_loaded = False

pr = sys.stdout.write
