#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
df=pd.read_pickle("hubway_trips.pkl")
stn_df=pd.read_pickle("hubway_stations.pkl")