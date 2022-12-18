import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

import dash_draggable


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app.layout = html.Div([
    html.H1("Dash Draggable"),
    html.B("Description:"),
    html.Ul([
        html.Li("The chart is not draggable nor resizeable (with the value 'static' set to True in 'layout')."),
        html.Li("The slider is draggable and resizeable.")
    ]),
    dash_draggable.GridLayout(
        id='draggable',
        clearSavedLayout=True,
        layout=[
            {
                "i": "spell",
                "x":0, "w":10, "y":0, "h":10
            },
        ],
        children=[
            dbc.InputGroup(
                [
                    dbc.Textarea(),
                    dbc.Textarea(),
                    dbc.Textarea(),
                    dbc.Textarea(),
                    dbc.Textarea(),
                    dbc.Textarea(),
                ],
           ),
        ]
)])



@app.callback(
    Output('graph-with-slider', 'figure'),
)
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port='5080')
