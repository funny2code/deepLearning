import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


app_routes = html.Div(
  children=[
   html.Div( dcc.Link( f"{page['name']} - {page['path']}", href=page["relative_path"] ) ) for page in dash.page_registry.values()
  ]
)

sidebar_devs = html.Div(
    [
        html.H5("YAW-Dashboard"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("K8s Framework", href="/k8s-framework", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar"
)

layout = html.Div(
  children=[
    sidebar_devs,
    dash.page_container,
    app_routes
    ]
)
