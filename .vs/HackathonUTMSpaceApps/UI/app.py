from shiny import App, render, ui
import pandas as pd
import plotly.express as px
import os

# Debugging: Check current working directory
print("Current working directory:", os.getcwd())

# Use absolute path to ensure the file is found
file_path = r'C:\Users\tibaa\OneDrive\Desktop\HacakthonUTMSpaceApp\HackathonUTMSpaceApps\.vs\HackathonUTMSpaceApps\data\GHG.csv'

# Check if the file exists
if os.path.exists(file_path):
    print("File exists:", file_path)
else:
    print("File does not exist:", file_path)

# Load the dataset
ghg_data = pd.read_csv(file_path)

# Create a Plotly figure using the correct column names
fig = px.line(ghg_data, 
              x="Reference Year",  # Make sure this matches your CSV column name
              y="Total Emissions (CO2e)", 
              title="Total Emissions (CO2e) from Oil and Gas Facilities Over Time")

# Define the UI
app_ui = ui.page_fluid(
    ui.h2("Tell a Climate Story"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_select("page", "Choose a page", ["Home", "Emissions Data", "Visualizations", "Stories"]),
        ),
        ui.panel_absolute(  # Use ui.panel for the main content area
            ui.output_plot("viz")
        )
    )
)

# Define server logic
def server(input, output, session):
    @output
    @render.plot  # Add this decorator to render the plot
    def viz():
        return fig

# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()
