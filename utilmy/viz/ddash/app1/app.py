# -*- coding: utf-8 -*-
"""  Launch app
Doc::
   
   ### Dependencies
        #### Libraries:
        ``` pip install fire
            pip install dash_treeview_antd
        ```
        #### Data:
            `cd html or dash pages to specified folder`

    ### Command to run
        - Launch html viz
            `python app.py main --content_type html --dir_template assets/html --sidebar_treeview tree_view_dict`
        - Launch links viz
            `python app.py main --sidebar_treeview tree_view_dict`
        - Launch dash pages viz
            `python app.py main --content_type dash --dir_template pages/ --sidebar_treeview tree_view_dict`

"""
import dash_bootstrap_components as dbc
from dash import Dash, html
from dash_treeview_antd import TreeView
from dash.dependencies import Input, Output
from fire import Fire

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
app.title = 'Simple render html'

### Main page resource
CONTENT_DEFAULT = {
    'html': {
        'path': 'assets/html',
        'page_default': 'main.html'
        },
    'dash': {
        'path':'pages/',
        'page_default': 'main.py'
        },
    'links': {
        'path': None,
        'page_default': 'about:blank'
        }
}

dir_path     = "assets/html/"
page_default = 'assets/html/main.html'


###################################################################
######  Utils #####################################################
def sidebar_v1(tree_view="", style=""):
    """ Compose Sidebar v1 layout component.

    Returns:
        _type_: (dash.html.Div.Divz) Sidebar v1 Div Component
    """

    SIDEBAR_STYLE_DEFAULT = {
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'width': '20%',
        'padding': '20px 10px',
        'backgroundColor': '#f8f9fa',
        'verticalAlign': 'middle',
        'alignItems': 'center'
    }


    TREE_VIEW_DEFAULT = {
                        'title': 'Parent', 'key':'0',
                        'children': [{
                            'title': 'Child',   'key': '01',
                            'children': [
                                {'title': 'Subchild1', 'key': 'page1.html'},
                                {'title': 'Subchild2', 'key': 'page2.html'},
                            ],
                        },
                        {   'title': 'Child2',   'key': '02',
                            'children': [
                                {'title': 'Subchild2-1', 'key': 'page2_1.html'},
                                {'title': 'Subchild2-2', 'key': 'page2_2.html'},
                                {'title': 'Subchild2-3', 'key': 'page2_3.html'},
                            ],
                        }]
                    }

    tree_view = tree_view or TREE_VIEW_DEFAULT
    style = style or SIDEBAR_STYLE_DEFAULT

    sidebar_content = html.Div( 
                        TreeView(
                            id='input',
                            multiple=False,
                            checkable=False,
                            checked=False,
                            selected=[],
                            expanded=[],
                            data=tree_view
                        ), style=style  
                    )
    return sidebar_content


@app.callback(Output('output', 'content_placeholder'), [Input('input', 'selected')])
def render(selected):
    global page_default, dir_path
    
    def iframe_render(selected):
        """ Handle raw .html and external links using Iframe """
        ...
    
    def dash_page_render(selected):
        """ Handle dash page rendering"""
        ...
    



# def iframe_render(selected):
#     global page_default, dir_html

#     if selected == []:
#         return f'{page_default}'

#     elif selected[0].endswith('.html'):
#             page_default = selected[0]
#             return f'{dir_html}/{selected[0]}'
#     else:
#         return f'{page_default}'



###################################################################
def main_page():

    sidebar_content = sidebar_v1()

    CONTENT_STYLE = {
        'marginLeft': '20%',
        'height': '100vh'
    }
    main_content = html.Div(id="content_placeholder", style=CONTENT_STYLE)

    app.layout = html.Div([sidebar_content, main_content])



def main(content_type="links", dir_template="", dir_log="", sidebar_treeview=""):
    """ Run main app

    Args:
        content_type ({'html', 'dash', 'links'}, optional):
            The content type to be loaded. Default to 'html'.
        dir_template (str, optional): 
            _description_. Defaults to "None".

    Raises:
        ValueError
            Raised if `content_type` is not 'html', 'dash', or 'links'.

    """
    content_type = content_type.lower()
    if content_type not in CONTENT_DEFAULT.keys():
        raise ValueError('content_type must be "html", "dash", or "links"')
    
    dir_path = dir_template or CONTENT_DEFAULT[content_type]['path']


    main_page()
    app.run_server(debug=True)



if __name__ == '__main__':
     Fire()


