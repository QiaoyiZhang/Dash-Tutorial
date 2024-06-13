import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = pd.read_csv('Dash_tutorial/Assignment2/2011_us_ag_exports.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(id='my-title', children='this is the second exercise'),
    dcc.Dropdown(options=df.state.unique(), value=["Alabama","Arkansas"], id='state-dropdown', multi=True),
    dcc.Graph(id='graph1')
])

@callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id='state-dropdown', component_property='value')
)

def update_graph(selected_state):
    df_country = df[df.state.isin(selected_state)]
    fig = px.bar(df_country, x='state', y=['beef','pork','fruits fresh'])
    return fig

if __name__=='__main__':
    app.run(debug=True)


