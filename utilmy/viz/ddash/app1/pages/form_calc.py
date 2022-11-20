import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html, callback, ctx


#from dash_bootstrap_components.dbc import Row as RR



##########################################################################################
### Modular Dash Html Part
title   = html.H1("AB Test:  N-Sample calculator     ")

ctr     = dbc.Row([ dbc.Label("Baseline  CTR level :",     width = 3),    
                    dbc.Col( dbc.Input(id= "ctr", type = "number", placeholder = "CTR in %"),            width= 4)],      className   = "mb-3")

mde     = dbc.Row([ dbc.Label("Minimal Detection Effect :", width = 3),    
                    dbc.Col( dbc.Input(id= "min_effect",    type = "number", placeholder = "MDE in %"),  width= 4)],      className   = "mb-3")

traffic = dbc.Row([ dbc.Label("Daily Traffic :",  width = 3),    
                    dbc.Col( dbc.Input(id= "daily_traffic", type = "number", placeholder = "15000"),     width= 4)],      className   = "mb-3")

nvariant= dbc.Row([ dbc.Label("N Variants :", width = 3),    
                    dbc.Col( dbc.Input(id= "n_variant", type = "number", placeholder = "2"),             width= 4)],      className   = "mb-3")


calc    = dbc.Row([ dbc.Label("",width = 3),    
                    dbc.Col(dbc.Button(id = "calc",         color = "primary", children  = "Calc" ),     width = 4)],     className   = "mb-3")

result  = dbc.Row([ html.H5("Nsample required ( 95% Confidence, 80% Power) :", ),  html.P(id = "result"),   
                    html.H5("Ndays required:", ),   html.P(id = "result2")])


### Constructing Layout
layout = dbc.Form([title, ctr, mde, traffic, nvariant, calc, result], style={'padding'  : '20px'})


##########################################################################################
################################# Callbacks ##############################################
def input_get(*s):
    ilist = []
    for si in s :
        if isinstance(si, str): 
            ilist.append(Input(si, "value"))
        elif isinstance(si, tuple):
            ilist.append(Input(si[0], si[1]))
    return ilist


@callback( Output("result",           "children"),
#[Input("ctr",   "value"),       Input("min_effect",  "value"),  Input("n_variant",   "value"),    Input("calc",   "n_clicks")],  prevent_initial_callback=  True)
input_get("ctr",  "min_effect", "n_variant",  ("calc",   "n_clicks") ),  prevent_initial_callback=  True)
def calc_nsample(ctr, min_effect, n_variant, _):    
    if ctx.triggered_id == 'calc':
        if (ctr is None or min_effect is None or n_variant is None):  return '' 

        ctr        = 0.01*float(ctr)
        min_effect = 0.01*max(0.01, float(min_effect))    ###  relative minimum effect.
        n_variant  = float(n_variant) 


        nsample = ab_get_sample(ctr, min_effect, n_variant)
        res  = str(nsample)
        return res



@callback( Output("result2", "children"),
#[Input("ctr", "value"), Input("min_effect", "value"),  Input("n_variant",   "value"),   Input("daily_traffic", "value"),  Input("calc",  "n_clicks")], prevent_initial_callback=     True)
input_get("ctr",  "min_effect", "n_variant",  ("calc",   "n_clicks") ),  prevent_initial_callback=  True)
def calc_ndays(ctr, min_effect, n_variant, traffic,  _):    
    if ctx.triggered_id == 'calc':
        if (ctr is None or min_effect is None or traffic is None or n_variant is None):  return '' 

        ctr        = 0.01*float(ctr)
        min_effect = 0.01*max(0.01, float(min_effect))  ###  relative minimum effect.
        n_variant  = float(n_variant) 
        traffic    = float(traffic)


        nsample = ab_get_sample(ctr, min_effect, n_variant)

        ndays = max(1, int(nsample / traffic) )
        res   = str(ndays)
        return res



def ab_get_sample(ctr, min_effect, n_variant):

        ### Per variant, need to doule for mutiple Variants
        variance = ctr*(1-ctr)  ### Binonmal
        nsample  = int( 16 * variance / ( min_effect **2 )   * n_variant )
        return nsample


