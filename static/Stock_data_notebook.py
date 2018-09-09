
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import bokeh.plotting as bk
import requests

from bokeh.models import HoverTool, Label, BoxZoomTool, PanTool, ZoomInTool, ZoomOutTool, ResetTool, ColumnDataSource
from bokeh.transform import factor_cmap
API_URL = 'https://api.iextrading.com/1.0'


# from bokeh.io import show, output_file


# from bokeh.sampledata.autompg import autompg as df
# from bokeh.transform import factor_cmap


# In[2]:


res = requests.get(f'{API_URL}/stock/TWTR/chart/5y')


# In[3]:


data = res.json()


# In[4]:


df = pd.DataFrame(data)


# In[5]:


# df.sample(20)


# In[6]:


# df.info()


# ### Candlestick Chart Setup

# In[7]:


df.shape


# In[8]:


seqs = np.arange(df.shape[0])
df['seqs'] = pd.Series(seqs)


# In[9]:


df['changePercent'] = df['changePercent'].apply(lambda x:str(x)+'%')


# In[10]:


df['mid'] = df.apply(lambda x: (x['open'] + x['close']) / 2, axis=1)


# In[11]:


df['height'] = df.apply(
    lambda x: x['close'] - x['open'] if x['close'] != x['open'] else 0.001,  
    axis=1)


# In[12]:


inc = df.close > df.open
dec = df.close < df.open
w = .3


# In[13]:


sourceInc = bk.ColumnDataSource(df.loc[inc])
sourceDec = bk.ColumnDataSource(df.loc[dec])


# In[14]:


hover = HoverTool (
    tooltips=[
        ('date', '@date'),
        ('low', '@low'),
        ('high', '@high'),
        ('open', '@open'),
        ('close', '@close'),
        ('percent', '@percent'),
    ]
    
)


# In[15]:


TOOLS = [hover, BoxZoomTool(), PanTool(), ZoomInTool(), ZoomOutTool(), ResetTool()]


# In[16]:


p = bk.figure(plot_width=1500, plot_height=800, tools=TOOLS, title='Microsoft', toolbar_location='above')


# In[17]:


# bk.show(p)


# In[18]:


p.xaxis.major_label_orientation= np.pi/4
p.grid.grid_line_alpha = w


# In[19]:


descriptor = Label(x=70, y=70, text='Your label goes here')
p.add_layout(descriptor)


# In[20]:


p.segment(df.seqs[inc], df.high[inc], df.seqs[inc], df.low[inc], color='green')


# In[21]:


p.segment(df.seqs[dec], df.high[dec], df.seqs[dec], df.low[dec], color='red')


# In[22]:


p.rect(x='seqs', y='mid', width=w, height='height', fill_color='green', line_color='green', source=sourceInc)
p.rect(x='seqs', y='mid', width=w, height='height', fill_color='red', line_color='red', source=sourceDec)


# In[23]:


# f string to name the file after the stock chosen
# bk.save(p, './static/candle_stick.html', title='5yr_candlestick')


# In[24]:


bk.show(p)
#


# In[25]:


# df.head(20)


# ### Chart high prices for last 5 years
# 

# In[26]:


source_bar = bk.figure(plot_width=1500, plot_height=600)

source_bar.vbar(x=df['seqs'], width=1, bottom=0, top=df['high'], color="blue")

# plot = bk.figure(plot_width=400, plot_height=400)
# plot.vbar(x=df.seqs, width=0.5, bottom=0,
#        top=df.low, color="firebrick")

bk.show(source_bar)


# ### Chart volume for the last 5 years

# In[27]:


source_bar2 = bk.figure(plot_width=1500, plot_height=600)
source_bar2.vbar(x=df['seqs'], width=1, bottom=0, top=df['volume'], color="firebrick")

bk.show(source_bar2)


# In[28]:


bk.save(p,source_bar,source_bar2, './charts.html', title='5yr_charts')


# In[ ]:


# bk.save(p, './static/candle_stick.html', title='5yr_candlestick')


# In[29]:


# bk.save(p, './static/5yr_charts.html', title='5yr_charts')

