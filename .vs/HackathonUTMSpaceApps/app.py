import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load your dataset
df = pd.read_csv('data/OilGasData.csv')

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.Div([
        # Left panel
        html.Div([
            html.H2("About", style={'margin-top': '20px'}),
            html.P("""
                The app gives a visual overview of CO2 emissions in Canada 
                and their potential impact over the years.
                Use the slider below to choose the year. The map will reflect 
                data for the selected input year.
            """),
            html.Label("Select Year"),
            dcc.Slider(
                id='year-slider',
                min=df['Year'].min(),  # Corrected 'year' to 'Year'
                max=df['Year'].max(),  # Corrected max logic
                value=df['Year'].min(),
                marks={str(year): str(year) for year in df['Year'].unique()},
                step=None
            ),
            html.H3("Dataset Information"),
            html.P("""
                For the app, we have chosen data from the ODIC-FFCO2 dataset.
            """),
            html.A("World Bank", href='https://www.worldbank.org/', target="_blank"),
            html.Br(),
            html.A("OECD", href='https://www.oecd.org/', target="_blank")
        ], style={'width': '25%', 'padding': '20px', 'float': 'left', 'backgroundColor': '#f9f9f9'}),

        # Map panel
        html.Div([
            dcc.Graph(id='emissions-map')
        ], style={'width': '70%', 'display': 'inline-block', 'padding-left': '20px'})
    ], style={'display': 'flex'}),

    # Tabs (Map, Graphs)
    html.Div([
        dcc.Tabs(id='tabs', value='map-tab', children=[
            dcc.Tab(label='Map', value='map-tab'),
            dcc.Tab(label='Graphs', value='graphs-tab'),
        ]),
        html.Div(id='tabs-content')
    ]),

    # Toggle buttons for data sources (OECD, World Bank)
    html.Div([
        html.Label("OECD"),
        dcc.Checklist(
            options=[{'label': 'OECD', 'value': 'OECD'}, {'label': 'World Bank', 'value': 'World Bank'}],
            value=['OECD'],
            inline=True
        )
    ], style={'margin': '20px'})
])

# Callback to update the map based on selected year
@app.callback(
    dash.dependencies.Output('emissions-map', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')]
)
def update_map(selected_year):
    # Filter the dataframe based on the selected year
    filtered_df = df[df['Year'] == selected_year]
    
    # Create a scatter plot on the map (update latitude and longitude column names to match your dataset)
    fig = px
