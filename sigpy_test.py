import sigpy as sp
import sigpy.mri as mr
import sigpy.mri.rf as rf
import numpy as np
import sigpy.plot as pl
import matplotlib

dim = 32
Nc = 8
img_shape = [dim, dim]
sens_shape = [Nc, dim, dim]
sens = mr.birdcage_maps(sens_shape)
pl.ImagePlot(sens)

fov = 0.55  # FOV in m
N = dim  # matrix size
gts = 6.4e-6  # hardware dwell time, s
gslew = 150  # gradient slew rate in mT/m/ms
gamp = 30 # maximum gradient amplitude in mT/m
densamp = 10000  # duration of full density sampling (in samples)
dentrans = 10000  # duration of transition from low-high density (in samples)
R = 1/2  # degree of undersampling of outer region of trajectory- let's oversample by a factor of 2
dx = 0.025 # in m
rewinder = False
# construct a trajectory
g, k, t, s = rf.spiral_arch(fov/R,dx,gts,gslew,gamp)

#Note that this trajectory is a spiral-out trajectory. 
#We will simply time-reverse it to create a spiral-in.
k = np.flipud(k)
g = np.flipud(g)
