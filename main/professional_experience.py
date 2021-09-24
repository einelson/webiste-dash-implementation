from dash import dcc, html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1('Professional Experience', className='title'),
    html.P('I love machine learning, data visualization and python. I think things that fly and robotics are amazing. I dont have any professional experience working on cars, but I love working on them!', className='paragraph'),
    html.ObjectEl(
        # To my recollection you need to put your static files in the 'assets' folder
        data=app.get_asset_url('/data/resume.pdf'),
        type="application/pdf",
        className='professional_experience_resume'
    ),
])
