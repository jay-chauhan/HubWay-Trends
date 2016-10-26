#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
df = pd.read_csv("http://localhost:8888/tree/Documents/HubWay/hubway_trips.csv")
stn_df=pd.read_csv("http://localhost:8888/tree/Documents/HubWay/hubway_stations.csv")
df['start_date'] = pd.to_datetime(df['start_date'], format='%m/%d/%Y %H:%M:%S')
df['end_date'] = pd.to_datetime(df['start_date'], format='%m/%d/%Y %H:%M:%S')
df.to_pickle("hubway_trips.pkl")
stn_df.to_pickle("hubway_stations.pkl")