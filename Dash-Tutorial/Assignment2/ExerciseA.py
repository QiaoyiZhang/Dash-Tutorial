import pandas as pd
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv('Dash_tutorial/Assignment2/2011_us_ag_exports.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(id='my-title', children='this is the second exercise'),
    dcc.Dropdown(options=df.state.unique(), value='Alabama', id='state-dropdown'),
    dcc.Graph(id='graph1',figure={})

])

if __name__=='__main__':
    app.run(debug=True)
