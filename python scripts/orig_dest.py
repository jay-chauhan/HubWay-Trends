#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def orig_dest(df,stn_df):
    fig,axes = plt.subplots(figsize=(15,6))
    top_stn=df.groupby(["strt_statn","end_statn"]).count()
    top_stn.sort_values(by=["hubway_id"], ascending=False,inplace=True)
    orig_stn=[]
    end_stn=[]
    top10orig=top_stn.index.values[0:10]
    for i in range(10):
        orig_stn.append(stn_df[stn_df["id"]==top10orig[i][0]]["station"].iloc[0])
        end_stn.append(stn_df[stn_df["id"]==top10orig[i][1]]["station"].iloc[0])
    x=range(0,8)
    rects=axes.barh(x,top_stn["hubway_id"].head(8),align='center',alpha=0.5)
    axes.xaxis.label.set_size(15)
    rect_labels=[]
    count=-1
    for rect in rects:
        count+=1
        width = int(rect.get_width())
        xloc = width - 30
        clr = 'white'
        align = 'right'
        rankStr = '{} to {}'.format(orig_stn[count],end_stn[count])
        yloc = rect.get_y() + rect.get_height()/2.0
        label = axes.text(xloc, yloc,rankStr, horizontalalignment=align,
                         verticalalignment='center', color=clr,
                         clip_on=True, fontsize=8.2,weight='bold')
        rect_labels.append(label)
    plt.show()
orig_dest(df,stn_df)