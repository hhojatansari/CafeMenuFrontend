import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from server import app
import views


app.layout = dbc.Container(
    [
        dcc.Location('base-url'),
        html.Div(
            [
                html.Div(
                    [
                        html.Img(src=app.get_asset_url('header.jpg'), className='header-image'),
                        html.Div(id='main-section'),
                        html.Img(src=app.get_asset_url('footer.jpg'), className='footer-image')
                    ],
                    className='bg-yellow-box container-card',
                ),
            ],
            className='my-card'
        ),
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
