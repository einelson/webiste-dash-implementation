from datetime import time
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from app import app

from projects.fault_detection.visualizations import Visuals

graphs = Visuals(df=('.' + app.get_asset_url('data/fault_detection/fault_detection.csv')), num_clusters=8)

time_series = graphs.time_series()
time_series.update_layout(paper_bgcolor = 'rgb(34, 34, 34)', font = {'color': "white", 'family': "Arial"})

heat_map = graphs.heat_map()
heat_map.update_layout(paper_bgcolor = 'rgb(34, 34, 34)', font = {'color': "white", 'family': "Arial"})

cluster = graphs.get_cluster_viz()
cluster.update_layout(paper_bgcolor = 'rgb(34, 34, 34)', font = {'color': "white", 'family': "Arial"})

'''
LAYOUT
'''
layout = html.Div([
    
    # about
    dbc.Row(
        [
            # about
            dbc.Col(
                [
                    html.H1('Fault Detection', className='title'),
                    html.P('Fault Detection was designed to detect and predict costly faults in oil and gas pipelines. The goal was to use clustering and PCA to create groupings for sensors and use that as a basis detectign faults.', className='paragraph'),
                    html.Label(['This was based on a paper by and sponsored by Avery Smith at ', html.A('Snow Data Science.', href='https://www.snowdatascience.org/')], className='paragraph'),
                    html.P('I immensly enjoyed this project and loved working on the machine learning, dimensionality reduction and data visualization aspects of it!', className='paragraph'),
                ],
            ),
            # picture
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('/data/fault_detection/FD3000.png'), className='image'),
                ],
            ),            
        ],
    ),
    # time series
    dbc.Row(
        [
            # time series
            dbc.Col(
                [
                    dcc.Graph(figure=time_series, className='image'),
                ],
            ),
            # description
            dbc.Col(
                [
                    html.H3('Sensor Visualization', className='title'),
                    html.P('Dash was used to render graph visualizations to show the time-series data from eash sensor.', className='paragraph'),
                    html.P('Shown here is all of the 250+ sensors graphed together. The data here is graphed in time series, so it shows sensor data and how it changes over time. To isolate on sensor double click on its name in the legend.', className='paragraph'),
                ],
            ),
        ],style={'margin-top': '4em'},
    ),
    # heatmap
    dbc.Row(
        [
            # heatmap
            dbc.Col(
                [
                    html.H3('Heatmap', className='title'),
                    html.P('When sensors were clustered together we generated a heatmap to visualize the groupings. Since this is a correlation heatmap the values are based on how the sensor values correlate one with another. The lighter values correlate positivley with one another and the darker values correlate oppositley with one another.', className='paragraph'),
                ],
            ),
            # graph
            dbc.Col(
                [
                    dcc.Graph(figure=heat_map, className='image'),
                ],
            ),
        ],style={'margin-top': '4em'},
    ),
    # cluster
    dbc.Row(
        [
            # 3d
            dbc.Col(
                [
                    dcc.Graph(figure=cluster, className='image'),
                ],
            ),
            # description
            dbc.Col(
                [
                    html.H3('PCA Clustering', className='title'),
                    html.P('There were over 250 sensors used in ths scenerio and when clustering there were over 250 dimensions used. PCA was used to reduce the dimensionality down from 250D down to the human redable dimensions of 3D', className='paragraph'),
                ],
            ),
        ],style={'margin-top': '4em'},
    ),
], className='layout')

