from shiny import App, render, ui
import pandas as pd
import plotly.express as px

# Load your dataset with the correct path
emissions_data = pd.read_csv('HackathonUTMSpaceApps\data\OilGasData.csv')

# Create a plotly figure using the correct column names
fig = px.line(emissions_data, 
              x="Reference Year",  # Ensure this matches your CSV column name
              y="Total Emissions (CO2e)", 
              title="Total Emissions (CO2e) from Oil and Gas Facilities Over Time")

# Define UI
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
    
    def viz():
        return fig

# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()
