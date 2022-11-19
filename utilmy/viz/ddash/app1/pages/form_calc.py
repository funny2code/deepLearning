import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html, callback


##########################################################################################
layout = dbc.Row([
        html.H1("     Simple BMI Calculator     "),
        dbc.Col([
                dbc.Input(id= "height-variable", type = "number", placeholder = "Enter Height (cm)",),
                        
                html.H5("Result :", style   = {"marginTop"      : "10px"}),
                html.H5(id      = "result")
            ],  width           = 4,
        ),
        dbc.Col([ dbc.Input(id= "weight-variable", type = "number", placeholder = "Enter Weight (kg)",
                )], width = 4,
        ),        
],    
    className       = "g-3", style      = {"margin"     : "20px"}
)


##########################################################################################
################################# Callbacks ##############################################
#### Sample BMI (Body Mass Index) calculation
@callback( Output("result",               "children"),
           [Input("height-variable",      "value"),       Input("weight-variable",      "value")],
         prevent_initial_callback= True)
def calculate(height, weight):
    if height != None and weight != None:
        # Parsing from string input to float
        height      = float(height)
        weight      = float(weight)

        BMI         = weight / (height/100) **2
        BMI = str(BMI)
        return BMI
