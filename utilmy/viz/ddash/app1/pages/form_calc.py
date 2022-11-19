import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html, callback

##########################################################################################

layout = dbc.Row([
        html.H1("     Simple BMI Calculator     "),
        dbc.Col([
                dbc.Input(
                    type        = "number",
                    id          = "height-variable",
                    placeholder = "Enter Height (cm)",
                ),
                        
                html.H5("Result :", style   = {"marginTop"      : "10px"}),
                html.H5(id      = "result")
            ],  width           = 4,
        ),
        dbc.Col([
                dbc.Input(
                    type        = "number",
                    id          = "weight-variable",
                    placeholder = "Enter Weight (kg)",
                )], width       = 4,
        ),
        
        ],
    
    className       = "g-3", style      = {"margin"     : "20px"}
)

##########################################################################################
################################# Callbacks ##############################################
#### Sample BMI (Body Mass Index) calculation
@callback(
    Output("result",               "children"),
    [Input("height-variable",      "value"),       Input("weight-variable",      "value")],
    prevent_initial_callback=       True
)
def calculate(height, weight):
    if height != None and weight != None:
        # Parsing from string input to float
        height      = float(height)
        weight      = float(weight)

        BMI         = weight / (height/100) **2

        if   BMI    <= 18.4:
            return("You are underweight.")
        elif BMI    <= 24.9:
            return("You are healthy.")
        elif BMI    <= 29.9:
            return("You are over weight.")
        elif BMI    <= 34.9:
            return("You are severely over weight.")
        elif BMI    <= 39.9:
            return("You are obese.")
        
        return(f"You are severely obese.")
