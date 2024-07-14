import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, 'assets/style.css']
)

app.title = 'Chenar Cafe'

app.layout = dbc.Container(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div('کافه چنار', className='card-title'),
                        html.P('جایی برای خواندن، نوشتن و نوشیدن..', className='card-description'),
                        html.Div(
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [

                                                    html.Img(
                                                        src=app.get_asset_url('icons/pin.png'),
                                                        className='loc-icon'
                                                    ),
                                                    html.Div('[ Location / آدرس ]')

                                                ],
                                                style={'text-align': 'center',
                                                       'display': 'flex',
                                                       'justify-content': 'center',
                                                       'padding': '10px 0'}
                                            ),
                                            html.Div(
                                                [

                                                    html.Img(
                                                        src=app.get_asset_url('icons/instagram.png'),
                                                        className='insta-icon'
                                                    ),
                                                    html.Div('[ Instagram / اینستاگرام ]')

                                                ],
                                                style={'text-align': 'center',
                                                       'display': 'flex',
                                                       'justify-content': 'center',
                                                       'padding': '10px 0'}
                                            ),
                                        ],
                                        className='right-section'
                                    ),
                                    html.Div(className='middle-line'),
                                    html.Div(
                                        [
                                            html.Img(
                                                src=app.get_asset_url('icons/menu.png'),
                                                className='menu-icon'
                                            ),
                                            html.Div('[ Menu / منو ]')
                                        ],
                                        className='left-section',
                                        style={'padding': '25px 0'}
                                    )
                                ],
                                className='card-enter'
                            ),
                            style={'display': 'flex',
                                   'justify-content': 'center'}
                        )
                    ],
                    className='container-card bg-yellow-box'
                )
            ],
            className='my-card'
        )
    ],
    style={'min-width': '340px!important'}
)

if __name__ == '__main__':
    app.run(host='localhost')
