import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(

)

app.title = 'Cafe Menu'

app.layout = dbc.Container(
    [
        html.Div(
            html.Div([
                html.Div('به کافه ... خوش آمدید',
                className='card-title')
            ],
            className='container-card bg-yellow-box'),
            className='card'
        )
    ]
)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
