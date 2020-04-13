'''Main script for executing models'''

import numpy as np
import params
import eos
import model

def mr_curve(P0=None, T0=None, x_w=None,mode='adaptive_new'):
    masses = np.arange(params.mass_lower,params.mass_upper,params.mass_step)
    radii = np.zeros_like(masses)
    for i,m in enumerate(masses):
        int_model = model.Model(m,P0,T0,x_w,mode,profiles=True)
        print(m)
        radii[i] = int_model.find_Rp()

    return np.c_[masses,radii]

def get_radius(mass,P0=None, T0=None, x_w=None,mode='adaptive_new',profiles=True):
    int_model = model.Model(mass,P0,T0,x_w,mode,profiles)
    return int_model.find_Rp()

def steps_test():
    int_model = model.Model(0.5)
    steps = np.logspace(2,5,20)
    radii = np.zeros_like(steps)
    for i in range(len(steps)):
        radii[i] = int_model.find_Rp(steps=int(steps[i]))

    return radii
