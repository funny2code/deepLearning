import dash_bootstrap_components as dbc
from dash import html


#nav_items
k8s_frameworks = dbc.NavItem(
  dbc.NavLink(
    "K8s Frameworks",
    href='/k8s-framework'
  ),
  class_name='nav_item'
)

nav_item = dbc.NavItem(dbc.NavLink("Menu", href="#"))

# Navbar 
navbar = dbc.Navbar(
  dbc.Container(
    children=[
      html.H3('YAW Dashboard'),
      dbc.NavbarToggler(id='nav-toggler'),
      dbc.Collapse(
        dbc.Nav(
          [
            k8s_frameworks
          ]
        ),
        id='nav-collapse',
        navbar=True,
        is_open=True
      )
    ],
    fluid=True)
)
