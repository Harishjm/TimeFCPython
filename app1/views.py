from django.shortcuts import render
from matplotlib import pyplot as plt
# Create your views here.
from django.http import HttpResponse
from io import BytesIO
import statsmodels.api as sm
import base64
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
data = pd.read_excel('app1/Sample-data sheet.xlsx')

def index(request):
    return render(request,'app1/index.html')

def records1(request):


    print(data.dtypes)
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    print(data['Order Date'].shape)
    data.sort_values(by='Order Date')
    # print(con.sort_values(by='Order Date'))
    # print()
    data.sort_values(by='Order Date', inplace=True)
    data.set_index('Order Date', inplace=True)
    print(data.tail(40))
    # plt.plot(data['Order Date'])
    # plt.show()
    data.plot(figsize=(10, 5), linewidth=3, fontsize=10)
    plt.xlabel('Year', fontsize=20);
    # plt.show()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'app1/graphic.html', {'graphic': graphic,'message':'A bit of Exploratory Data Analysis of all Records'})


def records2(request):
    # print(data.head())
    #print(data.dtypes)
    data=data = pd.read_excel('app1/Sample-data sheet.xlsx')
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    print(data['Order Date'].shape)
    data.sort_values(by='Order Date')
    # print(con.sort_values(by='Order Date'))
    # print()
    data.sort_values(by='Order Date', inplace=True)
    data.set_index('Order Date', inplace=True)
    print(data.tail(40))
    from matplotlib import pyplot as plt
    Profit = data[['Profit']]
    Profit.rolling(12).mean().plot(figsize=(20, 10), linewidth=5, fontsize=20)
    plt.xlabel('Year', fontsize=20);
   # plt.show()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'app1/graphic.html', {'graphic': graphic,'message':'Rolling mean for Profit'})


def records3(request):
    # print(data.head())
    #print(data.dtypes)
    data=data = pd.read_excel('app1/Sample-data sheet.xlsx')
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    print(data['Order Date'].shape)
    data.sort_values(by='Order Date')
    # print(con.sort_values(by='Order Date'))
    # print()
    data.sort_values(by='Order Date', inplace=True)
    data.set_index('Order Date', inplace=True)
    print(data.tail(40))
    from matplotlib import pyplot as plt
    sales = data[['Sales']]
    sales.rolling(12).mean().plot(figsize=(20, 10), linewidth=5, fontsize=20)
    plt.xlabel('Year', fontsize=20);
   # plt.show()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'app1/graphic.html', {'graphic': graphic,'message':'Rolling mean for Sales'})





def records4(request):
    # print(data.head())
    #print(data.dtypes)
    data=data = pd.read_excel('app1/Sample-data sheet.xlsx')
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    print(data['Order Date'].shape)
    data.sort_values(by='Order Date')
    # print(con.sort_values(by='Order Date'))
    # print()
    data.sort_values(by='Order Date', inplace=True)
    data.set_index('Order Date', inplace=True)
    print(data.tail(40))

    sales = data[['Sales']]  ##bcz extracting sales data as dataframe
    profit = data[['Profit']]

    ff= pd.concat([sales.rolling(12).mean(), profit.rolling(12).mean()], axis=1)
    ff.plot(figsize=(20,10), linewidth=5, fontsize=20)
    plt.xlabel('Year', fontsize=20);
    #plt.show()
   # plt.show()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'app1/graphic.html', {'graphic': graphic,'message':'Rolling mean Comparision Profit and Sales'})



def records5(request):
    # print(data.head())
    #print(data.dtypes)
    data=data = pd.read_excel('app1/Sample-data sheet.xlsx')
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    print(data['Order Date'].shape)
    data.sort_values(by='Order Date')
    # print(con.sort_values(by='Order Date'))
    # print()
    data.sort_values(by='Order Date', inplace=True)
    data.set_index('Order Date', inplace=True)
    print(data.tail(40))

    sales = data[['Sales']]  ##bcz extracting sales data as dataframe
    profit = data[['Profit']]

    profit.diff().plot(figsize=(20,10), linewidth=2, fontsize=20)
    plt.xlabel('Year', fontsize=20);
    plt.show()

    #plt.show()
   # plt.show()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'app1/graphic.html', {'graphic': graphic,'message':'Diff- Mean for Profit'})



def records6(request):
    # print(data.head())
    #print(data.dtypes)
    data=data = pd.read_excel('app1/Sample-data sheet.xlsx')
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    print(data['Order Date'].shape)
    data.sort_values(by='Order Date')
    # print(con.sort_values(by='Order Date'))
    # print()
    data.sort_values(by='Order Date', inplace=True)
    data.set_index('Order Date', inplace=True)
    print(data.tail(40))

    sales = data[['Sales']]  ##bcz extracting sales data as dataframe
    profit = data[['Profit']]
    import itertools

    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
    print('Examples of parameter combinations for Seasonal ARIMA...')
    print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
    print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
    print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
    print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

    y = data['Sales'].resample('MS').mean()


    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)

                results = mod.fit()
            except:
                continue
    print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))

    mod = sm.tsa.statespace.SARIMAX(y,
                                    order=(1, 1, 1),
                                    seasonal_order=(1, 1, 0, 12),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False)
    results = mod.fit()
    print(results.summary().tables[1])

    results.plot_diagnostics(figsize=(16, 8))


    #plt.show()
   # plt.show()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'app1/graphic.html', {'graphic': graphic,'message':'Model Distributions-investigation'})







def records7(request):
    # print(data.head())
    #print(data.dtypes)
    data=data = pd.read_excel('app1/Sample-data sheet.xlsx')
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    print(data['Order Date'].shape)
    data.sort_values(by='Order Date')
    # print(con.sort_values(by='Order Date'))
    # print()
    data.sort_values(by='Order Date', inplace=True)
    data.set_index('Order Date', inplace=True)
    print(data.tail(40))

    sales = data[['Sales']]  ##bcz extracting sales data as dataframe
    profit = data[['Profit']]
    import itertools

    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
    print('Examples of parameter combinations for Seasonal ARIMA...')
    print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
    print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
    print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
    print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

    y = data['Sales'].resample('MS').mean()


    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)

                results = mod.fit()
            except:
                continue
    print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))

    mod = sm.tsa.statespace.SARIMAX(y,
                                    order=(1, 1, 1),
                                    seasonal_order=(1, 1, 0, 12),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False)
    results = mod.fit()
    print(results.summary().tables[1])

    #results.plot_diagnostics(figsize=(16, 8))
    pred_uc = results.get_forecast(steps=100)
    pred_ci = pred_uc.conf_int()
    ax = y.plot(label='observed', figsize=(14, 7))
    pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.25)
    ax.set_xlabel('Date')
    ax.set_ylabel('Furniture Sales')
    plt.legend()
    #plt.show()


    #plt.show()
   # plt.show()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'app1/graphic.html', {'graphic': graphic,'message':'Next 4 years Estimation'})
