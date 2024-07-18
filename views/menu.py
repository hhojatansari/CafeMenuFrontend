import dash
from dash import MATCH, ALL

from dash import html, ctx
import dash_bootstrap_components as dbc
from server import app

category = ['غذا', 'نوشیدنی']
index_list = [10, 20]
items = ['نوشابه', 'چای', 'لیموناد', 'قرمه سبزی', 'کاسه تف']

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
            html.Div(
                id={
                    'type': 'category-pattern-output',
                    'index': index_list[index]
                }
            )
        ],
        style={'width': '80%'}
    )
    for index, cat in enumerate(category)
]


@app.callback(
    dash.Output({'type': 'category-pattern-output', 'index': MATCH}, "children"),
    dash.Input({'type': 'category-pattern', 'index': MATCH}, 'n_clicks'),
    prevent_initial_call=True
)
def display_output(cat):
    print(ctx.triggered)
    print('category:', cat)
    return 'چه خبر پسر جون'
