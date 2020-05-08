import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

# Create the dash app object
APP = dash.Dash(__name__)

# Define the data we'll use
# Sorry Brecht, I'm gonna call it DF!
DF = pd.read_csv('immo.csv')


# Create the HTML layout
# Use html for 1:1 html tags
# Use dcc for more interactive stuff like button and sliders
APP.layout = html.Div(children=[
    html.H1(children='Hello ML6!'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    
    # Dcc elements are usually interactive (Javascripty) elements    
    # Of course we can use Python to speed things up!
    dcc.Dropdown(
        id = 'col_select',
        options=[
            {'label': colname, 'value': colname}
            for colname in DF.columns
        ],
        value=DF.columns[0]
    ),
    
    # Create a div just to output something with the callback
    html.Div(id='out_div'),
    
    html.Br(),
    
    html.Img(
        src='https://ml6.eu/wp-content/themes/ml6%2830.03.2020%29/resources/assets/images/logo.svg'
    )
])

# Callbacks!
# These are the real magic of plotly dash
# Use any attribute within the layout as input
# and ouput to any other attribute based on the 
# return value of a function
@APP.callback(
    Output(component_id='out_div', component_property='children'),
    [Input(component_id='col_select', component_property='value')]
)
def update_output_div(colname):
    return 'You\'ve selected "{}"'.format(colname)

if __name__ == '__main__':
    APP.run_server(debug=True)