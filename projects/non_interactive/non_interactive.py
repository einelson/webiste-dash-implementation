"""
Author: Ethan Nelson
"""
from dash import  html
import dash_bootstrap_components as dbc
from app import app

'''
LAYOUT
'''
layout = html.Div([
    
    # row1
    dbc.Row(
        [
            # about
            dbc.Col(
                [
                    html.H1('Non interactive projects', className='title'),
                    html.P('All non interactive projects are linked to github, just click on the image. These projects were ones that I was not able to host on the web, or were not easy to demonstrateable on the web. I hope you enjoy these as well!', className='paragraph'),
                ],
            ),           
        ],
    ),

    # point cloud classification
    dbc.Row(
        [
            # project description
            dbc.Col(
                [
                    html.H2('Point cloud classification', className='title'),
                    html.P('The point cloud project was research into if a neural network could learn off of spatial, point cloud data. Data uesd was lidar data from warehouses and was edged towards detection of shelves, pallets, products and walls.', className='paragraph'),
                ],
            ),
            # picture link
            dbc.Col(
                [
                    html.A([html.Img(src=app.get_asset_url('/data/non_interactive/pointcloud.png'), className='image')], href='https://github.com/einelson/Point-cloud-classification-keras'),
                ],
            ),
        ],style={'margin-top': '4em'},
    ),

    # EEG eye state
    dbc.Row(
        [
            # project description
            dbc.Col(
                [
                    html.H2('EEG eye-state classification', className='title'),
                    html.P('This was probably one of my more favorite projects. I love EEG and in this project I wanted to test how well a 2D neural network could learn EEG patterns in the brain. Take a look at the research paper I wrote on this by clicking on the image to the right. ', className='paragraph'),
                ],
            ),
            # picture link
            dbc.Col(
                [
                    html.A([html.Img(src=app.get_asset_url('/data/non_interactive/eeg_eye_state_map.png'), className='image')], href='https://github.com/einelson/EEG-Eye-State-data-set/blob/master/eeg.ipynb'),
                ],
            ),
        ],style={'margin-top': '4em'},
    ),

    # RSA encryption
    dbc.Row(
        [
            # project description
            dbc.Col(
                [
                    html.H2('RSA Encryption', className='title'),
                    html.P('A simple encryption algorithm using RSA encryption', className='paragraph'),
                ],
            ),
            # picture link
            dbc.Col(
                [
                    html.A([html.Img(src=app.get_asset_url('/data/non_interactive/RSAgraph.png'), className='image')], href='https://github.com/einelson/RSA_Encryptor'),
                ],
            ),
        ],style={'margin-top': '4em'},
    ),

], className='layout')
