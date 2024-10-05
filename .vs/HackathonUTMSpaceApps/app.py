from shiny import App, render, ui
import pandas as pd

# Load your datasets
ghg_data = pd.read_csv('data/GHG.csv')
oil_gas_data = pd.read_csv('data/OilGasData.csv')

# Define UI
app_ui = ui.page_fluid(
    ui.h2("Tell a Climate Story"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            # Adding "About" and slider similar to the example UI
            ui.h3("About"),
            ui.p("The app gives a visual overview of Greenhouse Gas Emissions in Canada over the years "
                 "and their potential impact on climate change."),
            ui.p("Please use the slider below to choose the year. The map will reflect data for the selected input year."),
            
            # Adding a year slider
            ui.input_slider("year_slider", "Select Year", 
                            min=ghg_data['Year'].min(), 
                            max=ghg_data['Year'].max(), 
                            value=ghg_data['Year'].min()),
            
            # Adding Dataset Information section
            ui.h3("Dataset Information"),
            ui.p("For the app, we have chosen data from the World Bank, OECD, and other trusted sources."),
            ui.a("World Bank", href="https://www.worldbank.org/", target="_blank"),
            ui.br(),
            ui.a("OECD", href="https://www.oecd.org/", target="_blank"),
        ),
        ui.panel_main(
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
