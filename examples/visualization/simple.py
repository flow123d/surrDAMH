#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:02:19 2021

@author: simona
"""

import os
import sys
import json
sys.path.append(os.getcwd())
from surrDAMH.modules import visualization_and_analysis as va

saved_samples_name = "simple"
conf_path = "examples/simple.json"

with open(conf_path) as f:
    conf = json.load(f)

if len(sys.argv)>1:
    no_samplers = int(sys.argv[1]) # number of MH/DAMH chains
else:
    no_samplers = 4

### SAMPLES VISUALIZATION:
S = va.Samples()
no_parameters = conf["no_parameters"]
S.load_notes('saved_samples/' + saved_samples_name,no_samplers)
S.load_MH('saved_samples/' + saved_samples_name,no_parameters)

# Which part of the sampling process is analyzed? 0/1/2 = MH/DAMH-SMU/DAMH
setnumber = 2;
S.calculate_properties()
S.print_properties()
chains_disp = range(setnumber*no_samplers,(setnumber+1)*no_samplers)
S.plot_hist_grid(chains_disp = chains_disp, bins1d=30, bins2d=30)
S.plot_average(chains_disp = chains_disp, show_legend = True)