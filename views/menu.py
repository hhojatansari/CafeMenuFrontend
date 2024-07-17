import dash
from dash import html, ctx
import dash_bootstrap_components as dbc
from app import app

category = ['غذا', 'نوشیدنی']
items = ['نوشابه', 'چای', 'لیموناد', 'قرمه سبزی', 'کاسه تف']

seciton = [
              html.Img(src=app.get_asset_url('header.jpg'), className='header-image', id='heyyou'),
          ] + [
              html.Div(
                  [
                      html.Div(
                          [
                              html.Div(cat, className='text-block'),
                          ],
                          className='category-image',
                          style={'background': 'url("/assets/food.jpg")'},
                          id={"type": "pattern-category", "index": index},
                      ),
                      dbc.Collapse(
                          dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
                          id="collapse",
                          is_open=True,
                      ),
                  ],
                  style={'width': '80%'}
              )
              for index, cat in enumerate(category)
          ]


@app.callback(
    dash.Output("buttons-response", "children"),
    # dash.Input({"type": "pattern-category", "index": dash.ALL}, "n_clicks"),
    dash.Input('heyyou', 'click')
)
def display_output(cat):
    print(ctx.triggered[0])
    print(ctx.triggered[0]["value"])
    print('category:', cat)
