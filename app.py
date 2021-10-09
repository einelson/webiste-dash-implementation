import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, suppress_callback_exceptions=True,update_title=None, title='Ethan Nelson', external_stylesheets=[dbc.themes.DARKLY, 'website.css'])
server = app.server
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True