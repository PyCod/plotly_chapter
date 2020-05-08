import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

import plotly.express as px

# Create the dash app object
APP = dash.Dash(__name__)

# Define the data we'll use
# Sorry Brecht, I'm gonna call it DF!
DF = pd.read_csv('immo.csv')


# Create the HTML layout
# Use html for 1:1 html tags
# Use dcc for more interactive stuff like button and sliders
APP.layout = html.Div(children=[
    
    html.Div([
        html.Div([
            html.Div([
               html.Img(
                    src='/assets/logo.svg',
                    width='80%',
                    style={'margin': '20px auto 20px auto'},
                    className='center'
                ), 
            ], className='row'),
            html.Br(),
            html.Div([
               dcc.Dropdown(
                    id = 'col_select',
                    options=[
                        {'label': colname, 'value': colname}
                        for colname in DF.columns
                    ],
                    value=DF.columns[1]
                ), 
            ], className='row'),
        ], className='pretty_container three columns'),
        html.Div([
            dcc.Graph(id='histogram'),
        ], className='pretty_container nine columns'),
    ], className='row'),
])

# Callbacks!
# These are the real magic of plotly dash
# Use any attribute within the layout as input
# and ouput to any other attribute based on the 
# return value of a function
@APP.callback(
    Output(component_id='histogram', component_property='figure'),
    [Input(component_id='col_select', component_property='value')]
)
def update_output_div(colname):
    fig = px.histogram(DF, x=colname)
    fig.update_layout(title=colname)
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    fig.update_traces(marker_color='#ff9900')

    return fig

if __name__ == '__main__':
    APP.run_server(debug=True)