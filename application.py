from dash.resources import Scripts
from app import app
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from main import home, professional_experience, not_found
from projects.non_interactive import non_interactive
from projects.image_collage import image_collage
from projects.image_colorization import image_colorization
from projects.fault_detection import fault_detection


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className='top_row_nav'),
    
    # add in links here
    dbc.Nav(
        [
            # main pages
            dbc.NavLink("Home", active=True, href="/main/home"),
            dbc.NavLink("Professional Experience", active=True, href="/main/professional_experience"),

            # project base
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem(dbc.NavLink("Non Interactive", active=True, href="/projects/non_interactive")),
                    dbc.DropdownMenuItem(dbc.NavLink("Collage Generator", active=True, href="/projects/image_colage")),
                    dbc.DropdownMenuItem(dbc.NavLink("Image Colorization", active=True, href="/projects/image_colorization")),
                    dbc.DropdownMenuItem(dbc.NavLink("Fault Detection", active=True, href="/projects/fault_detection")),
                ],
                label="Projects",
                nav=True,
            ),
        ],
        className='new-navbar'
    ),

    # new page loaded here
    html.Div(id='page-content'),

    # footer
    html.Div(
        [
            html.P('Check me out on social media and take a look at my projects', className='paragraph', style={'text-align': 'center'}),
            html.Div(
                [
                    html.A([html.Img(src=app.get_asset_url('/footer_icons/linkedin.png'), className='footer_image')], href='https://www.linkedin.com/in/ethan-nelson/'),
                    html.A([html.Img(src=app.get_asset_url('/footer_icons/github.png'), className='footer_image')], href='https://github.com/einelson'),
                    html.A([html.Img(src=app.get_asset_url('/footer_icons/instructables.png'), className='footer_image')], href='https://www.instructables.com/member/enelson8/'),
                ],
                className='footer_items',
            ),
            html.P('einelson8i@gmail.com', className='paragraph', style={'text-align': 'center'}),
            html.P('© 2022 by Ethan Nelson', className='paragraph', style={'text-align': 'center'}),
        ],
        className='footer_new',
    ),

], className='body')


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    # main
    if pathname == '/main/home' or pathname == '/':
        return home.layout
    elif pathname == '/main/professional_experience':
        return professional_experience.layout
    # projects
    elif pathname == '/projects/non_interactive':
        return non_interactive.layout
    elif pathname == '/projects/image_colage':
        return image_collage.layout
    elif pathname == '/projects/image_colorization':
        return image_colorization.layout
    elif pathname == '/projects/fault_detection':
        return fault_detection.layout
    # 404
    else:
        return not_found.layout

if __name__ == '__main__':
    application = app.server
    application.run(debug=True)