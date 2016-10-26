#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reg_vs_cas(df,stn_df):
    fig = plt.figure(figsize=(15,10))
    ax = plt.subplot(111)
    reg=df[df["subsc_type"]=="Registered"]["subsc_type"].count()
    cas=df[df["subsc_type"]=="Casual"]["subsc_type"].count()
    labels=["Registered","Casual"]
    reg_frac=reg/(reg+cas)*100
    cas_frac=cas/(reg+cas)*100
    stn=df.groupby([df["strt_statn"]]).count()
    stn.sort_values(by=["subsc_type"], ascending=False,inplace=True)
    top3=stn.index.values[0:3]
    stn_reg=[]
    stn_cas=[]
    stn_reg_frac=[]
    stn_cas_frac=[]
    for x in range(3):
        stn_reg.append(df[(df["subsc_type"]=="Registered") & (df["strt_statn"]==top3[x])]["subsc_type"].count())
        stn_cas.append(df[(df["subsc_type"]=="Casual") & (df["strt_statn"]==top3[x])]["subsc_type"].count())
        stn_reg_frac.append(stn_reg[x]/(stn_reg[x]+stn_cas[x])*100)
        stn_cas_frac.append(stn_cas[x]/(stn_reg[x]+stn_cas[x])*100)
    plt.subplot(221)
    plt.title("Registered vs Causals All Hubway Stations")
    plt.pie(x=[reg_frac,cas_frac],labels=labels,autopct='%1.1f%%',explode=[0.05,0],colors=['lightcoral','lightskyblue'])
    plt.subplot(222)
    station=stn_df[stn_df["id"]==top3[0]]["station"]
    plt.title("Registered vs Causals #1: {}".format(station.iloc[0]))
    plt.pie(x=[stn_reg_frac[0],stn_cas_frac[0]],labels=labels,autopct='%1.1f%%',explode=[0.05,0],colors=['lightcoral','lightskyblue'])
    plt.subplot(223)
    station=stn_df[stn_df["id"]==top3[1]]["station"]
    plt.title("Registered vs Causals #2: {}".format(station.iloc[0]))
    plt.pie(x=[stn_reg_frac[1],stn_cas_frac[1]],labels=labels,autopct='%1.1f%%',explode=[0.05,0],colors=['lightcoral','lightskyblue'])
    plt.subplot(224)
    station=stn_df[stn_df["id"]==top3[2]]["station"]
    plt.title("Registered vs Causals #3: {}".format(station.iloc[0]))
    plt.pie(x=[stn_reg_frac[2],stn_cas_frac[2]],labels=labels,autopct='%1.1f%%',explode=[0.05,0],colors=['lightcoral','lightskyblue'])    
    plt.show()

reg_vs_cas(df,stn_df)