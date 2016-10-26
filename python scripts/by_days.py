#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def by_days(df):
    fig,axes = plt.subplots(figsize=(8,4))
    x=range(7)
    peak=df.groupby([df["start_date"].dt.weekday]).count()
    axes.set_xticks(x)
    axes.set_xticklabels(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
    axes.bar(x,peak["start_date"], align='center')
    plt.show()
by_days(df)
