import dash
import dash_core_components as dcc
import dash_html_components as html

# Create the dash app object
APP = dash.Dash(__name__)


# Create the HTML layout
# Use html for 1:1 html tags
# Use dcc for more interactive stuff like button and sliders
APP.layout = html.Div(children=[
    html.H1(children='Hello ML6!'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    
    html.Br(),
    
    html.Img(
        src='https://ml6.eu/wp-content/themes/ml6%2830.03.2020%29/resources/assets/images/logo.svg'
    )
])

if __name__ == '__main__':
    APP.run_server(debug=True)