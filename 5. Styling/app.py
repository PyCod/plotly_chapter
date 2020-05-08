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


# Use lots of divs! Most of the time you'll alternate between
# using rows and columns
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

# You can change the plot background color to transparent so it just folows
# the main page style
# Use update_traces for custom marker colors, individual colors possible too
# If using non plotly express you can give it along with your traces like so:
# fig.add_trace(go.Bar(
#     x=months,
#     y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
#     name='Primary Product',
#     marker_color='indianred'
# ))
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