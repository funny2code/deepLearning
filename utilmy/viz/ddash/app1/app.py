# -*- coding: utf-8 -*-
"""  Launch app
Doc::
   
   ### Dependencies
        #### Libraries:
        ``` pip install fire
            pip install dash_bootstrap_components
            pip install dash_treeview_antd
            pip install orjson
        ```
        #### Data:
            - For Html
                `copy .html files to assets/html/`
            - For Dash Pages
                `copy pages.py files to pages/ folder`

        #### Layout Json:
            Base Format:
                ```
                {
                    "main_content" : {
                        <MAIN_CONTENT_STYLE>
                    },
                    "sidebar_content":{
                        "version": <SIDEBAR_VERSION>,
                        "data": {
                            "title": "Home", "key":"<LINKS or HTML FILENAME or DASH FILENAME>",
                            "children": [{
                                "title": "Child",   "key": "<NUMBER>",
                                "children": [...]

                            }]
                        },
                        "style": {
                            <SIDEBAR_STYLE>
                        }
                    }
                }
                ```
            
            Save .json to assets folder


    ### Command to run
        - Launch html viz
            `python app.py main --content_type html --content_layout assets/content_layout.json --homepage main.html`
        - Launch links viz
            `python app.py main --content_layout links_example.json
        - Launch dash pages viz
            `python app.py main` // under development

"""
import dash_bootstrap_components as dbc
import orjson
from dash import Dash, html
from dash.dcc import Store
from dash.dependencies import ClientsideFunction, Input, Output
from dash_treeview_antd import TreeView
from fire import Fire

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Simple render html'

### Main page resource

###################################################################
######  Utils #####################################################
def sidebar_v1(sidebar):
    """ Compose Sidebar v1 layout component.
    Args:
        _type_: (dict) Sidebar data and style

    Returns:
        _type_: (dash.html.Div.Div) Sidebar v1 Div Component

    Raises:
        ValueError
            Raised if `data` or `style` is not exist in `sidebar_content` json.
    """
    if 'data' not in sidebar.keys():
        raise ValueError('data key not found in json file')
    
    if 'style' not in sidebar.keys():
        raise ValueError('style key not found in json file')

    sidebar_content = html.Div( 
                        TreeView(
                            id='input',
                            multiple=False,
                            checkable=False,
                            checked=False,
                            selected=[],
                            expanded=[],
                            data=sidebar['data']
                        ), style=sidebar['style']
                    )
    return sidebar_content

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='render'
    ),
    Output('output', 'src'),
    [Input('content-type', 'data'),
    Input('input', 'selected'),
    Input('homepage', 'data')]
)
        

###################################################################
def render_page(content_type, content_layout, homepage):
    """
    Main Render Page

    Raises:
        ValueError
            - Raised if `sidebar_content` is not found in layout json.
            - Raised if `version` is not found in `sidebar_content` section.  
    
    """
    SIDEBAR_VER = {1: sidebar_v1} # Scalable sidebar

    if 'sidebar_content' not in content_layout.keys():
        raise ValueError('sidebar_content key not found in layout json')
    
    if 'version' not in content_layout['sidebar_content'].keys():
        raise ValueError('version key not found in sidebar_content section')
        
    version = content_layout['sidebar_content']['version'] 

    sidebar_content = SIDEBAR_VER[version](content_layout['sidebar_content'])
    main_content = html.Div(html.Iframe(id="output", height='100%', width='100%'), style=content_layout['main_content'])

    app.layout = html.Div([
                            sidebar_content, 
                            main_content,
                            Store(id='content-type', storage_type='session', data=content_type),
                            Store(id='homepage', storage_type='session', data=homepage)
                        ])


def main(content_type="links", content_layout="assets/content_layout.json", homepage="", debug=True, dir_log=""):
    """ Run main app

    Args:
        content_type ({'html', 'dash', 'links'}, optional):
            The content type to be loaded. Default to 'html'.
        content_layout (dict, optional):
            The content layout in JSON format. Default to 'assets/content_layout.json'.
        homepage (str, optional): 
            Set Homepage Location. Defaults to "None".
        debug (boolean, optional):
            Set dash debug options. Default to 'True'

    Raises:
        ValueError
            Raised if `content_type` is not 'html', 'dash', or 'links'.

    """

    content_type = content_type.lower()
    if content_type not in ['links', 'html', 'dash']:
        raise ValueError('content_type must be "links", "html", or "dash"')
    
    with open(fr"{content_layout}", "rb") as f:
        content_layout = orjson.loads(f.read())

    homepage = homepage or content_layout['sidebar_content']['data']['key']
   
    render_page(content_type, content_layout, homepage)

    app.run_server(debug=debug)


if __name__ == '__main__':
     Fire()