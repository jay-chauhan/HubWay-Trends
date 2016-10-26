#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def peak_hours(df):
    fig,axes = plt.subplots(figsize=(15,3))
    x=range(24)
    peak=df.groupby([df["start_date"].dt.hour]).count()
    axes.set_xticks(x)
    axes.set_xticklabels(["12am","1am","2am","3am","4am","5am","6am","7am","8am","9am","10am","11am","12pm","1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm","10pm","11pm"])
    axes.plot(x,peak["start_date"])
    show()
peak_hours(df)