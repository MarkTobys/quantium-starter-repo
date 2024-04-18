import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

path = "./sorted_data.csv"


df = pd.read_csv(path)

app = Dash(__name__)

header = html.H1(
    "Pink Morsel Sales over Time",
    id="header"
)

figure = px.line(df, x="date", y="sales")

visualiser = dcc.Graph(
    id="visualization",
    figure=figure
)

# define the app layout
app.layout = html.Div(
    [
        header,
        visualiser
    ]
)


if __name__ == '__main__':
    app.run(debug=True)