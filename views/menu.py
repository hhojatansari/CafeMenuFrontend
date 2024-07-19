import ast

import dash
from dash import MATCH

from dash import html, ctx
import dash_bootstrap_components as dbc
from server import app

category = ['غذا', 'نوشیدنی']
index_list = [10, 20]
items = {
    10: ['املت', 'پاستا'],
    20: ['لیموناد', 'چای', 'اسپرسو']
}

menu_dict = {
    'نوشیدنی': {
        'index': 0,
        'img': '/assets/drink.jpg',
        'sub': {
            'نوشیدنی گرم': {'چای سیاه': 70, 'چای ماسالا': 100},
            'نوشیدنی خنک': {'موهیتو': 120, 'لیموناد': 120},
            'نوشیدنی کافئین‌دار': {'اسپرسو': 50, 'آفوگاتو': 70},
        }
    },
    'کیک و شیرینی': {
        'index': 1,
        'img': '/assets/cake.jpg',
        'sub': {
            'کیک': {'کیک شکلاتی': 70, 'چیزکیک': 100},
            'شیرینی': {'شیرینی کوکی': 20, 'شیرینی زبان': 15},
        }
    }
}

seciton = [
    html.Div(
        [
            html.Div(id='empty-div', style={'display': 'none'}),
            dbc.Button(
                [
                    html.Div(cat, className='text-block'),
                ],
                className='category-image',
                style={'background': 'url("{}") no-repeat'.format(menu_dict[cat]['img']),
                       'background-size': '100% auto',
                       'width': '100%',
                       'border-color': 'black'},
                id={
                    'type': 'category-pattern',
                    'index': menu_dict[cat]['index']
                }
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
                id={
                    'type': 'category-pattern-output',
                    'index': menu_dict[cat]['index']
                },
                is_open=False,
            )
        ],
        style={'width': '80%'}
    )
    for cat in menu_dict
]


@app.callback(
    [dash.Output({'type': 'category-pattern-output', 'index': MATCH}, "children"),
     dash.Output({'type': 'category-pattern-output', 'index': MATCH}, "is_open")],
    [dash.Input({'type': 'category-pattern', 'index': MATCH}, 'n_clicks')],
    [dash.State({'type': 'category-pattern-output', 'index': MATCH}, "is_open")],
    prevent_initial_call=True
)
def display_output(btn, is_open):
    category_index = ast.literal_eval(ctx.triggered[0]['prop_id'].split('.')[0])['index']
    if btn:
        items_section = []
        for cat in menu_dict:
            if menu_dict[cat]['index'] != category_index:
                continue
            sub_cat = []
            for sub in menu_dict[cat]['sub']:
                sub_cat.append(html.Div(sub, className='sub-category'))
                sub_items = []
                for item in menu_dict[cat]['sub'][sub]:
                    sub_items.append(
                        html.Div(
                            [
                                html.Div(item, style={'width': '20%', 'margin': '0 10px'}),
                                html.Hr(),
                                html.Div(menu_dict[cat]['sub'][sub][item], style={'width': '20%', 'margin': '0 10px'})
                            ],
                            className='item'
                        )
                    )
                sub_cat.append(html.Div(sub_items))
            items_section.append(html.Div(sub_cat))
        return items_section, not is_open
    return [], is_open
