from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")

app = Dash(__name__)

my_scatter_plot = px.scatter(df, x="V", y="S")

app.layout = html.Div([
    dcc.Graph(figure=my_scatter_plot)
])

if __name__ == '__main__':
    app.run(debug=True)