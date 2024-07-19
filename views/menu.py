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

seciton = [
    html.Div(
        [
            html.Div(id='empty-div', style={'display': 'none'}),
            dbc.Button(
                [
                    html.Div(cat, className='text-block'),
                ],
                className='category-image',
                style={'background': 'url("/assets/food.jpg")',
                       'width': '100%',
                       'border-color': 'black'},
                id={
                    'type': 'category-pattern',
                    'index': index_list[index]
                }
            ),
            dbc.Collapse(
                dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
                id={
                    'type': 'category-pattern-output',
                    'index': index_list[index]
                },
                is_open=False,
            ),
            # html.Div([
            #              html.Div('نوشیدنی', className='sub-category')
            #          ] + [
            #              html.Div(
            #                  [
            #                      html.Div(item, style={'width': '20%', 'margin': '0 10px'}),
            #                      html.Hr(),
            #                      html.Div('65', style={'width': '20%', 'margin': '0 10px'})
            #                  ],
            #                  className='item'
            #              )
            #              for item in items[20]
            #          ])
        ],
        style={'width': '80%'}
    )
    for index, cat in enumerate(category)
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
        items_section = [html.Div('نوشیدنی', className='sub-category')]
        for item in items[category_index]:
            items_section.append(
                html.Div([
                    html.Div(
                        [
                            html.Div(item, style={'width': '20%', 'margin': '0 10px'}),
                            html.Hr(),
                            html.Div('65', style={'width': '20%', 'margin': '0 10px'})
                        ],
                        className='item'
                    )
                ])
            )
        return items_section, not is_open
    return [], is_open
