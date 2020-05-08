import dash
import dash_core_components as dcc
import dash_html_components as html

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
    dcc.Dropdown(
        options=[
            {'label': 'Example 1', 'value': 'ex1'},
            {'label': 'Example 2', 'value': 'ex2'},
            {'label': 'Example 3', 'value': 'ex3'}
        ],
        value='ex2'
    ),
    
    # Of course we can use Python to speed things up!
    # dcc.Dropdown(
    #     options=[
    #         {'label': colname, 'value': colname}
    #         for colname in DF.columns
    #     ],
    #     value=DF.columns[0]
    # ),
    
    # Br html tag adds a whitespace
    html.Br(),
    
    # Each tag has attributes, like an image has a src attribute
    # We will use these later in callbacks
    html.Img(
        src='https://ml6.eu/wp-content/themes/ml6%2830.03.2020%29/resources/assets/images/logo.svg'
    )
])

if __name__ == '__main__':
    APP.run_server(debug=True)