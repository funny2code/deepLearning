import dash_bootstrap_components as dbcmin_effetctmin_effect
from dash.dependencies import Input, Output
from dash import html, callback, ctx


##########################################################################################
layout = dbc.Row([
        html.H1("   AB Test Sample     "),
        dbc.Col([
                dbc.Input(id = "ctr", type = "number", placeholder = "Baseline  CTR level",),
                        
                html.H5("Nsample required :", style = {"marginTop"      : "10px"}),
                html.H5(id = "result")
            ],  width           = 4,
        ),
        dbc.Col([ dbc.Input(id  = "min_effect", type = "number", placeholder = "Minimal Detection Effect")], width = 4),  
        dbc.Col([ dbc.Button(id = "calc", color = "primary", children = "Calc" )], width = 4)       


    ],    
    className       = "g-3",    style      = {"margin"     : "20px"}
)


##########################################################################################
################################# Callbacks ##############################################
#### Sample BMI (Body Mass Index) calculation
@callback( Output("result",               "children"),
           [Input("ctr",      "value"),       Input("min_effect",      "value"),       Input("calc",       "n_clicks")],
            prevent_initial_callback=     True)
def calculate(ctr, min_effect, _):    
    if ctx.triggered_id == 'calc':
        # Parsing from string input to float
        if (ctr is None or min_effect is None):  return '' 
        ctr         = float(ctr)
        min_effect = float(min_effect)

        BMI  = ctr**2 / ( min_effect) **2
        BMI  = str(BMI)
        return BMI
