from dash import Dash, html, dcc, Input, Output, callback
import pandas as pd
import time

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(options=df.brand.unique(), value = 'Revlon', id='demo-dropdown'),
    dcc.Loading([html.Div(id="loading-demo")])
])

@callback(
    Output(component_id='loading-demo', component_property='children'),
    Input(component_id='demo-dropdown', component_property='value')
)
def update_loading_div(value):
    time.sleep(2)
    return f"You have selected {value}"

if __name__ == '__main__':
    app.run(debug=True)