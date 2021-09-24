from dash import dcc, html
import dash_bootstrap_components as dbc

from app import app


layout = html.Div([
    
    # row1
    dbc.Row(
        [
            # about
            dbc.Col(
                [
                    html.H1('Ethan Nelson', className='title'),
                    html.P('Hey! You found my homepage!', className='paragraph')
                ],
            ),
            # picture
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('/images/bridge.jpg'), className='image')
                ],
            ),            
        ],
    ),
    # row2
    dbc.Row(
        [
            # about
            dbc.Col(
                [
                    
                ],
            ),
            # picture
            dbc.Col(
                [
                  
                ],
            ),
        ],
    ),
], className='layout')