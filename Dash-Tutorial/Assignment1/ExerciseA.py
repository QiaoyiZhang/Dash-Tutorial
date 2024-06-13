import pandas as pd
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv")

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(options=df.brand.unique(), value = 'Revlon', id='demo-dropdown'),

    dcc.RadioItems(options=[{"label": "Fenty Beauty's PRO FILT'R Foundation Only", "value": 0},
                           {"label": "Make Up For Ever's Ultra HD Foundation Only", "value": 1},
                           {"label": "US Best Sellers", "value": 2},
                           {"label": "BIPOC-recommended Brands with BIPOC Founders", "value": 3},
                           {"label": "BIPOC-recommended Brands with White Founders", "value": 4},
                           {"label": "Nigerian Best Sellers", "value": 5},
                           {"label": "Japanese Best Sellers", "value": 6},
                           {"label": "Indian Best Sellers", "value": 7}])
])

if __name__ == '__main__':
    app.run(debug=True)