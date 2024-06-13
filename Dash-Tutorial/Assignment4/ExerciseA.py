import pandas as pd
from dash import Dash, html, dcc, Input, Output, callback, State
import plotly.express as px

df = pd.read_csv('C:/Users/smqazha2/Abschlussarbeit/Dash_tutorial/Assignment2/2011_us_ag_exports.csv')

app = Dash(__name__)

app.layout = html.Div([
   html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
   dcc.Dropdown(id="state-dropdown", options=df.state.unique(), value=["Alabama","Arkansas"], multi=True),
   html.Button(id="state-button", children="Submit"),
   dcc.Graph(id="graph1"),
])
@app.callback(
   Output(component_id='graph1', component_property='figure'),
   Input(component_id='state-button', component_property='n_clicks'),
   State(component_id='state-dropdown', component_property='value'),
   prevent_initial_call=True
)
def update_graph(n, states_selected):
    print(type(n))
    if n > 0:
        df_states = df[df.state.isin(states_selected)]
        fig1 = px.bar(data_frame=df_states, x='state', y=['beef','pork','fruits fresh'])
        return fig1
    else:
       return px.bar()


if __name__ == '__main__':
  app.run(debug=True)

