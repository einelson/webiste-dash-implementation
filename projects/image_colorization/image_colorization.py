"""
Author: Ethan Nelson
File: collage_generator.py
Description: 
    Using OpenCV to constuct a collage.
    Border color, rotation and placement are randomly generated

"""
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from app import app

import numpy as np
from cv2 import cv2
import base64
import os
import datetime
from itertools import chain
import plotly.express as px

# global
images = []
image_names = []

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
                    html.H1('Image colorization', className='title'),
                    html.P('Under construction', className='paragraph'),

                ],
            ),
            # picture
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('/data/image_colorization/image_colorization.png'), className='image'),
                ],
            ),            
        ],
    ),
    # row2
    dbc.Row(
        [
            # tools
            dbc.Col(
                [
                    dbc.Card(
                        [   
                            # header
                            dbc.CardHeader('Upload Image'),
                            # settings
                            dbc.CardBody(
                                [
                                    # # upload images
                                    # html.P('Upload images', className='input_line'),
                                    # html.Div(className='images_list'),
                                    # html.Div(id='output-image-upload'),
                                    # dcc.Upload(
                                    #     id='upload-image',
                                    #     children=html.Div([
                                    #         'Drag and Drop or ',
                                    #         html.A('Select Files')
                                    #     ]),
                                    #     style={
                                    #         'width': '100%',
                                    #         'height': '60px',
                                    #         'lineHeight': '60px',
                                    #         'borderWidth': '1px',
                                    #         'borderStyle': 'dashed',
                                    #         'borderRadius': '5px',
                                    #         'textAlign': 'center',
                                    #         'margin': '10px'
                                    #     },
                                        # Allow multiple files to be uploaded
                                        # multiple=True
                                    # ),

                                    # clear uploaded
                                    # dbc.Button('Clear', color='secondary', id='b_clear_uploaded'),
                                ],
                            ),

                            # execute
                            dbc.CardFooter(
                                [
                                    # dbc.Button('Create', color='success', id='b_create_collage'),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            # picture output
            dbc.Col(
                [
                    # dcc.Graph(id='out_image_collage', className='image_gen'),
                ],
            ),
        ],style={'margin-top': '4em'},
    ),
], className='layout')
