from dash import dcc, html
import dash_bootstrap_components as dbc

from app import app


layout = html.Div([
    # spacing
    html.Div(className='top_row'),

    # about me
    dbc.Row(
        [
            # about
            dbc.Col(
                [
                    html.H1('About me', className='title'),
                    html.P('Hey guys! I am currently a software engineer over in Virginia. I enjoy working on machine learning problems and data visualization.', className='paragraph'),
                    html.P('I really just enjoy working on any problems. I would like to think I am a good problem solver, and not just with software. I think that everything we know and have learned can pool over into other areas of our life.', className='paragraph'),
                    html.P('I hope that whatever I do is something that can benefit and help people. There is so much good that can be shared with others.', className='paragraph'),
                    html.P('Keep reading and get to know more about me! and if you want help on any projects dont hesitate to reach out to me!', className='paragraph'),
                ],
            ),
            # picture
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('/data/bridge.jpg'), className='image')
                ],
            ),            
        ],
    ),

    # education
    html.Div(className='top_row'), 
    dbc.Row(
        [
            # picture
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('/data/panama.jpg'), className='image')
                ],
            ),
            # about
            dbc.Col(
                [
                    html.H1('Education', className='title'),
                    html.P('I went to school at Brigham Young University Idaho (2018-2021) and graduated with a degree in computer science.', className='paragraph'),
                    html.P('My favorite classes were the machine learning and senior project classes.', className='paragraph'),
                    html.P('While I do not currently do machine learning or data visualization for work I continue to work on it in my free time.', className='paragraph'),
                    html.P('Continuing education is important to me. I am currently studying to take the GRE so I can persue a masters or PhD in data/machine learning.', className='paragraph'),
                ],
            ),
        ],
    ),

    # what I enjoy
    html.Div(className='top_row'),
    dbc.Row(
        [
            # about
            dbc.Col(
                [
                    html.H1('Off-Topic', className='title'),
                    html.P('We are all humans and dont enjoy working 24/7. I enjoy many things not related to my field of work', className='paragraph'),
                    html.P('I love to work on and fix cars. At the age of 22 I restored and sold my dream car- a 66 mustang.', className='paragraph'),
                    html.P('While in college I worked as a carpenter and started to make and sell custom furniture on the side. Making furniture in a 1 car garage is not easy!', className='paragraph'),
                    html.P('I love the outdoors. I love camping, hiking and being in the mountains. When camping we would tie our hammocks between a tree and the bumper of my jeep.', className='paragraph'),
                    html.P('I love to weld. I learned as a senior in high school and while in college I was contracted to help weld shark tanks for an aquarium.', className='paragraph'),
                ],
            ),
            # picture
            dbc.Col(
                [
                    html.Img(src=app.get_asset_url('/data/bridge.jpg'), className='image')
                ],
            ),            
        ],
    ),



], className='layout')