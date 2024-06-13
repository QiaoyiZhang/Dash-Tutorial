import pandas as pd
from dash import Dash, dcc, html
import dash_ag_grid as dag

app = Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")

app.layout = html.Div([
    dag.AgGrid(
        id = 'table',
        rowData = df.to_dict("records"),
        columnDefs = [{"field": i} for i in df.columns])
]) 

if __name__ == '__main__':
    app.run(debug=True)