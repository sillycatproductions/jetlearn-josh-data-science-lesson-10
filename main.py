import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('WHO-COVID-19-global-data.csv')
data.columns = ('Date_reported','Country_code','Country','WHO_region','New_cases','Cumulative_cases','New_deaths','Cumulative_deaths')
data['Date_reported'] = pd.to_datetime(data['Date_reported'])

data_dates = data.groupby('Date_reported').sum()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x = data_dates.index, y = data_dates['Cumulative_cases'], fill = 'tonexty', line_color = 'blue'))
fig1.update_layout(title = 'Cumulative Cases Worldwide')
fig1.write_html('Fig1.html', auto_open = True) 

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x = data_dates.index, y = data_dates['New_cases'], fill = 'tonexty', line_color = 'red'))
fig2.update_layout(title = 'New Cases Worldwide')
fig2.write_html('Fig2.html', auto_open = True)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x = data_dates.index, y = data_dates['New_deaths'], fill = 'tonexty', line_color = 'green'))
fig3.update_layout(title = 'New Deaths Worldwide')
fig3.write_html('Fig3.html', auto_open = True)

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x = data_dates.index, y = data_dates['Cumulative_deaths'], fill = 'tonexty', line_color = 'yellow'))
fig4.update_layout(title = 'Cumulative Deaths Worldwide')
fig4.write_html('Fig4.html', auto_open = True)
