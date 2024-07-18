import dash
import dash_bootstrap_components as dbc


app = dash.Dash(
    'CafeMenu',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.title = 'Chenar Cafe'
