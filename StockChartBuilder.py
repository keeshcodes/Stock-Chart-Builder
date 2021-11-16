#import databases
import datetime as dt
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style

#set graph style - options here: https://www.dunderdata.com/blog/view-all-available-matplotlib-styles
style.use("bmh")

#start/end dates
start = dt.datetime(2019,12,31)
end = dt.datetime.now()

#Enter Stock Ticker in ""
#If International use "ticker"."stockExchange"
#i.e. Avast PLC (London) = AVST.L
#Reference Guide: https://help.yahoo.com/kb/SLN2310.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAL8WnOj-I2UQJnpHK83SUYny-XoIJ9DdO0-UTgzDxhz_aHrJaniUo2lFzgw3LtLAbroWicGEs1n_P1F3vgC3y6DiM3R-usiaMa70Ou__yk5WmBajzP8UyQPRnldsBN8AsDdbqRW7tQwvQ3ZqcSdetij0vyIaallcnDrmKFlw_iWN

df=web.get_data_yahoo("BRSAN.IS",start,end)
#Plot Stock based on Adj. Close
#rcParams['figure.figsize'] = 10, 6

df["Adj Close"].plot()
plt.xlabel('Date')
plt.ylabel('Stock Price')
#Your Company Here ""
plt.title("Borusan" + " Stock Chart")

plt.show()