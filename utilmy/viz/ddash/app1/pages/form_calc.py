import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html, callback, ctx
import dash_bootstrap_components as dbc    

from dbc import Row as RR
from dbc import Col as CC
from dash import Dash, html


##########################################################################################
### Modular Dash Html Part

title   = html.H1("   AB Test Sample     ")

ctr     = dbc.Row([ dbc.Label("Baseline  CTR level :",         html_for = "ctr",            width = 3),    dbc.Col( dbc.Input(id= "ctr",           type = "number", placeholder = " CTR in %"), 
                    width       = 4)],      className   = "mb-3")
mde     = dbc.Row([ dbc.Label("Minimal Detection Effect :",    html_for = "min_effect",     width = 3),    dbc.Col( dbc.Input(id= "min_effect",    type = "number", placeholder = " MDE in %"), 
                    width       = 4)],      className   = "mb-3")
traffic = dbc.Row([ dbc.Label("Daily Traffic :",               html_for = "daily_traffic",  width = 3),    dbc.Col( dbc.Input(id= "daily_traffic", type = "number", placeholder = " 15000"), 
                    width       = 4)],      className   = "mb-3")
calc    = dbc.Row([ dbc.Label("",                              html_for = "calc",           width = 3),    dbc.Col(dbc.Button(id = "calc",         color = "primary", children  = "Calc" ), 
                    width = 4)],            className   = "mb-3")
result  = dbc.Row([ html.H5("Nsample required ( 95% Confidence, 80% Power) :", ),  html.P(id = "result"),   html.H5("Ndays required:", ),   html.P(id = "result2")])


### Constructing Layout
layout = dbc.Form([title, ctr, mde, traffic, calc, result], style={'padding'  : '20px'})


##########################################################################################
################################# Callbacks ##############################################
#### Sample BMI (Body Mass Index) calculation
@callback( Output("result",           "children"),
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
[Input("ctr", "value"), Input("min_effect", "value"),   Input("daily_traffic", "value"),  Input("calc",  "n_clicks")], prevent_initial_callback=     True)
def calc_ndays(ctr, min_effect, traffic,  _):    
    if ctx.triggered_id == 'calc':
        # Parsing from string input to float
        if (ctr is None or min_effect is None or traffic is None):  return '' 

        ctr        = float(ctr)
        min_effect = float(min_effect)
        traffic    = max(1.0, float(traffic) )

        BMI   = ctr**2 / ( min_effect) **2
        ndays = max(1, int(BMI / traffic) )
 
        res  = str(ndays)
        return res


