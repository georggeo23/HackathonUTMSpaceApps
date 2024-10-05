from shiny import App, render, ui
import pandas as pd

# Load your datasets
ghg_data = pd.read_csv('data/GHG.csv')
oil_gas_data = pd.read_csv('data/OilGasData.csv')

# Check the datasets (optional)
print(ghg_data.head())
print(oil_gas_data.head())

# Define UI
app_ui = ui.page_fluid(
    ui.h2("Tell a Climate Story"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select("page", "Choose a page", ["Home", "Emissions Data", "Visualizations", "Stories"]),
        ),
        ui.panel_absolute(
            ui.output_text("content")  # This will show content based on page selection
        )
    )
)

# Define server logic
def server(input, output, session):
    @output
    @render.text  # Render the text based on the selected page
    def content():
        if input.page == "Home":
            return "Welcome to the Climate Story App!"
        elif input.page == "Emissions Data":
            return "Here you can explore emissions data."
        elif input.page == "Visualizations":
            return "This page will have visualizations."
        elif input.page == "Stories":
            return "Read stories about climate impact."

# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()

