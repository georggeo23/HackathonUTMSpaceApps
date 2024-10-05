from shiny import App, render, ui
import pandas as pd
import plotly.express as px
import os

# Debugging: Check current working directory
print("Current working directory:", os.getcwd())

# Use absolute paths for both datasets
ghg_file_path = r'C:\Users\tibaa\OneDrive\Desktop\HacakthonUTMSpaceApp\HackathonUTMSpaceApps\.vs\HackathonUTMSpaceApps\data\GHG.csv'
oilgas_file_path = r'C:\Users\tibaa\OneDrive\Desktop\HacakthonUTMSpaceApp\HackathonUTMSpaceApps\.vs\HackathonUTMSpaceApps\data\OilGasData.csv'

# Check if the files exist
if os.path.exists(ghg_file_path):
    print("File exists:", ghg_file_path)
else:
    print("File does not exist:", ghg_file_path)

if os.path.exists(oilgas_file_path):
    print("File exists:", oilgas_file_path)
else:
    print("File does not exist:", oilgas_file_path)

# Load the datasets
ghg_data = pd.read_csv(ghg_file_path)
oilgas_data = pd.read_csv(oilgas_file_path)

# Create Plotly figure for GHG data
ghg_fig = px.line(ghg_data, 
              x="Year",  # Corrected to match your dataset
              y="Total Greenhouse Gas Emissions (Mt CO2e)", 
              title="Total Greenhouse Gas Emissions (Mt CO2e) Over Time")

# Create Plotly figure for OilGasData
oilgas_fig = px.scatter(oilgas_data, 
                        x="Reference Year",  # Ensure this matches your CSV column name
                        y="Total Emissions (CO2e)", 
                        hover_name="Facility Name",  # Include facility name for hover
                        color="Province",  # Different colors for provinces
                        title="Oil and Gas Facilities Emissions (CO2e) by Year")

# Define the UI with tabs to switch between datasets
app_ui = ui.page_fluid(
    ui.h2("Tell a Climate Story"),
    ui.page_sidebar(  # Corrected from panel_sidebar to page_sidebar
        ui.input_select("page", "Choose a page", ["Home", "Emissions Data", "Visualizations", "Stories"]),
        ui.input_radio_buttons("data_selector", "Choose Dataset", choices=["GHG Emissions", "Oil and Gas Data"])
    ),
    ui.panel_main(
        ui.output_plot("viz")  # This will display the chosen plot
    )
)

# Define server logic to switch between the GHG and OilGas plots based on user selection
def server(input, output, session):
    @output
    @render.plot  # Add this decorator to render the plot
    def viz():
        if input.data_selector == "GHG Emissions":
            return ghg_fig  # Show GHG emissions plot
        elif input.data_selector == "Oil and Gas Data":
            return oilgas_fig  # Show Oil and Gas emissions plot

# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()
