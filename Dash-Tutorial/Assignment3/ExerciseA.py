from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

df = pd.read_csv('C:/Users/smqazha2/Abschlussarbeit/Dash_tutorial/Assignment2/2011_us_ag_exports.csv')

app = Dash(__name__)

app.layout = html.Div([
   html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
   dcc.Dropdown(id="state-dropdown", options=df.state.unique(), value=["Alabama","Arkansas"], multi=True),
   dcc.Graph(id="graph1"),
   dag.AgGrid(
      id='tabular-table',
      rowData=df.to_dict('records'),
      columnDefs = [{"field": i} for i in df.columns]
    )
])

@app.callback(
   Output(component_id='graph1', component_property='figure'),
   Input(component_id='state-dropdown', component_property='value')
)
def update_graph(states_selected):
   df_country = df[df.state.isin(states_selected)]
   fig1 = px.bar(data_frame=df_country, x='state', y=['beef','pork','fruits fresh'])
   return fig1

@app.callback(
    Output(component_id='tabular-table', component_property='rowData'),

    Input(component_id='graph1', component_property='hoverData'),
    prevent_initial_call=True
)
def update_table(data_hovered):
    print(data_hovered)
    country_hovered = data_hovered['points'][0]['label']
    dff = df[df.state == country_hovered]
    return dff.to_dict('records')

if __name__ == '__main__':
  app.run(debug=True)

