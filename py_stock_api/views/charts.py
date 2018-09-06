from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config
import requests
import json
import numpy as np
import pandas as pd
import bokeh.plotting as bk
from bokeh.models import HoverTool, Label, BoxZoomTool, PanTool, ZoomInTool, ZoomOutTool, ResetTool, ColumnDataSource
from bokeh.transform import factor_cmap

API_URL = 'https://api.iextrading.com/1.0'


class ChartsAPIView(APIViewSet):
    def list(self, request):
        """ Lookup a stock by the symbol
        """
        # url = 'https://api.iextrading.com/1.0/stock/{}/company'.format(
        #     request.matchdict['symbol']
        # )
        # # time_url = 'https://api.iextrading.com/1.0/stock/{}}/time-series'.format(
        # #     request.matchdict['time']
        # # )
        # response = requests.get(url)

        # return Response(json=response.json(), status=200)

        res = requests.get(f'{API_URL}/stock/TWTR/chart/5y')

        data = res.json()

        df = pd.DataFrame(data)

        df.shape

        seqs = np.arange(df.shape[0])
        df['seqs'] = pd.Series(seqs)

        df['changePercent'] = df['changePercent'].apply(lambda x:str(x)+'%')

        df['mid'] = df.apply(lambda x: (x['open'] + x['close']) / 2, axis=1)

        df['height'] = df.apply(
            lambda x: x['close'] - x['open'] if x['close'] != x['open'] else 0.001,
            axis=1)

        inc = df.close > df.open
        dec = df.close < df.open
        w = .3

        sourceInc = bk.ColumnDataSource(df.loc[inc])
        sourceDec = bk.ColumnDataSource(df.loc[dec])

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

        TOOLS = [hover, BoxZoomTool(), PanTool(), ZoomInTool(), ZoomOutTool(), ResetTool()]
        p = bk.figure(plot_width=1500, plot_height=800, tools=TOOLS, title='Microsoft', toolbar_location='above')
        p.xaxis.major_label_orientation= np.pi/4
        p.grid.grid_line_alpha = w
        descriptor = Label(x=70, y=70, text='Your label goes here')
        p.add_layout(descriptor)
        p.segment(df.seqs[inc], df.high[inc], df.seqs[inc], df.low[inc], color='green')
        p.segment(df.seqs[dec], df.high[dec], df.seqs[dec], df.low[dec], color='red')
        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='green', line_color='green', source=sourceInc)
        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='red', line_color='red', source=sourceDec)

        # bk.show(p)
        source_bar = bk.figure(plot_width=1500, plot_height=800)
        source_bar.vbar(x=df['seqs'], width=1, bottom=0, top=df['high'], color="blue")
        # bk.show(source_bar)
        source_bar2 = bk.figure(plot_width=1500, plot_height=800)
        source_bar2.vbar(x=df['seqs'], width=1, bottom=0, top=df['volume'], color="firebrick")
        # bk.show(source_bar2)
        # bk.save(p,source_bar,source_bar2, './charts.html', title='5yr_charts')

        bk.save(p, './static/5yr_charts_candle.html', title='5yr_charts')
        bk.save(source_bar, './static/5yr_charts_bar1.html', title='5yr_charts')
        bk.save(source_bar2, './static/5yr_charts_bar2.html', title='5yr_charts')

        response = "Your charts have been saved"

        return Response(json=response, status=200)
