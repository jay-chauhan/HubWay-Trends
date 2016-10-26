#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def top_stations(df, stn_df):
    fig,axes = plt.subplots(figsize=(15,6))
    top_stn=df.groupby([df["strt_statn"]]).count()
    top_stn.sort_values(by=["hubway_id"], ascending=False,inplace=True)
    top10=top_stn.index.values[0:10]
    station=[]
    for i in range(10):
        station.append(stn_df[stn_df["id"]==top10[i]]["station"].iloc[0])
    x=range(8)
    axes.set_xticklabels(station[0:8])
    axes.bar(x,top_stn["hubway_id"].head(8),align='center')
    plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='center')
    plt.show()    
top_stations(df,stn_df)