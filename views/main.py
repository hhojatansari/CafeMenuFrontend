from server import app
from dash import html
import dash_bootstrap_components as dbc


section = [
    # html.Div('کافه چنار', className='card-title'),
    # html.P('جایی برای خواندن، نوشتن و نوشیدن..', className='card-description'),
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
                                html.A(html.Div('[ Location / آدرس ]'),
                                       href='https://maps.app.goo.gl/1vzWj91mMApPKjwp7',
                                       target="popup")

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
                                html.A(html.Div('[ Instagram / اینستاگرام ]'),
                                       href='https://www.instagram.com/cafe_chenar_lahijan/',
                                       target="popup")

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
                        html.A(html.Div('[ Menu / منو ]', style={'color': '#cbc8be !important'}),
                               href='/menu')
                    ],
                    className='left-section',
                    style={'padding': '25px 0'}
                )
            ],
            className='card-enter'
        ),
        style={'display': 'flex',
               'justify-content': 'center',
               'width': '100%'}
    )
]
