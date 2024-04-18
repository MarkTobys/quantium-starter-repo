import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

path = "./sorted_data.csv"


df = pd.read_csv(path)

app = Dash(__name__)

regions = ['north', 'east', 'south', 'west']

header = html.H1(
    "Pink Morsel Sales over Time",
    id="header",
    style={'textAlign': 'center', 'color': '#EEACEE', 'marginBottom': '20px'}
)

figure = px.line(df, x="date", y="sales")

visualiser = dcc.Graph(
    id="visualization",
    figure=figure
)

region_radio = dcc.RadioItems(
    id='region-radio',
    options=[{'label': region, 'value': region} for region in regions],
    value='north',
    labelStyle={'display': 'inline-block'}
)

# Define callback to update the graph based on selected region
@app.callback(
    Output('visualization', 'figure'),
    [Input('region-radio', 'value')]
)
def update_figure(selected_region):
    filtered_df = df[df['region'] == selected_region]
    fig = px.line(filtered_df, x="date", y="sales")
    return fig

app.layout = html.Div(
    [
        header,
        region_radio,
        visualiser
    ],
    style={'maxWidth': '800px', 'margin': 'auto', 'padding': '20px', 'backgroundColor': '#3E3E3E'}
)


if __name__ == '__main__':
    app.run(debug=True)