import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

import views

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.title = 'Chenar Cafe'

app.layout = dbc.Container(
    [
        dcc.Location('base-url'),
        html.Div(
            [
                html.Div(
                    className='container-card bg-yellow-box',
                    id='main-section'
                )
            ],
            className='my-card'
        )
    ],
    style={'min-width': '340px!important'}
)


@app.callback(
    dash.Output('main-section', 'children'),
    dash.Input('base-url', 'pathname')
)
def router(pathname):
    print('pathname', pathname)
    if pathname.lower() == '/':
        return views.main.section
    elif pathname.lower() == '/menu':
        return views.menu.seciton
    else:
        return dash.no_update


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)