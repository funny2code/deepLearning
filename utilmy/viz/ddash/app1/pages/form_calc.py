import dash_bootstrap_components as dbcmin_effetctmin_effect
from dash.dependencies import Input, Output
from dash import html, callback, ctx
import dash_bootstrap_components as dbc    

from dbc import Row as RR
from dbc import Col as CC
from dash import Dash, html


##########################################################################################
### https://stackoverflow.com/questions/60299299/grid-dashboard-with-plotly-dash

layout = html.Div([
       
        html.H1("   AB Test Sample     "),
 
        dbc.Row([   html.label("   "), dbc.Input(id= "ctr",           type = "number", placeholder = "Baseline  CTR level n %",] )

        dbc.Row([   html.label("   "), dbc.Input(id= "min_effect",    type = "number", placeholder = "Minimal Detection Effect in %")  ])

        dbc.Row([   html.label("   "), dbc.Input(id= "Daily traffic", type = "number", placeholder = " 15000")   ])


        
        html.H5("   ")
        dbc.Col([ dbc.Button(id = "calc", color = "primary", children = "Calc" )], width = 4)       
        html.H5("   ")


        html.H5("Nsample required ( 95% Confidence, 80% Power) :", ),  html.P(id = "result")
        html.H5("Ndays required:", ),             html.P(id = "result2")

            ],  width           = 4,
        ),

            
        , width = 4),  


    ],    
    className       = "g-3",    style      = {"margin"     : "20px"}
)



##########################################################################################
################################# Callbacks ##############################################
#### Sample BMI (Body Mass Index) calculation
@callback( Output("result",               "children"),
[Input("ctr",   "value"),       Input("min_effect",  "value"),   Input("calc",   "n_clicks")],  prevent_initial_callback=  True)
def calculate(ctr, min_effect, _):    
    if ctx.triggered_id == 'calc':
        # Parsing from string input to float
        if (ctr is None or min_effect is None):  return '' 

        ctr        = float(ctr)
        min_effect = float(min_effect)    ###  relative minimum effect.

        variance   = ctr*(1-ctr)  ### Binonmal

        ### Per variant, need to doule for mutiple Variants
        BMI  = 16 * variance / ( min_effect **2 )
        BMI  = str(BMI)
        return BMI



@callback( Output("result2", "children"),
[Input("ctr", "value"), Input("min_effect", "value"),   Input("traffic", "value"),  Input("calc",  "n_clicks")], prevent_initial_callback=     True)
def calc_ndays(ctr, min_effect, traffic,  _):    
    if ctx.triggered_id == 'calc':
        # Parsing from string input to float
        if (ctr is None or min_effect is None):  return '' 

        ctr        = float(ctr)
        min_effect = float(min_effect)
        traffic    = max(1.0, float(traffic) )

        BMI   = ctr**2 / ( min_effect) **2
        ndays = max(1, int(BMI / traffic) )
 
        res  = str(ndays)
        return res



