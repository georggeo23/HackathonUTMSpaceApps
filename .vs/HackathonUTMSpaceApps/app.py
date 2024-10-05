import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load your OilGasData.csv dataset
df = pd.read_csv('data/OilGasData.csv')

