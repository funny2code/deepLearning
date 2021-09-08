

test\vizhtml.py
-------------------------functions----------------------
log(*s)
test_getdata(verbose = True)
test1()
test2()
test3(verbose = True)
test_scatter_and_histogram_matplot()
test_pd_plot_network()
test_cssname(verbose = True, css_name = "A4_size")
help()
mlpd3_add_tooltip(fig, points, labels)
pd_plot_scatter_get_data(df0:pd.DataFrame, colx: str = None, coly: str = None, collabel: str = None, colclass1: str = None, colclass2: str = None, nmax: int = 20000)
pd_plot_scatter_matplot(df:pd.DataFrame, colx: str = None, coly: str = None, collabel: str = None, colclass1: str = None, colclass2: str = None, cfg: dict  =  {}, mode = 'd3', save_path: str = '', **kw)
pd_plot_histogram_matplot(df:pd.DataFrame, col: str = '', title: str = '', nbin = 20.0, q5 = 0.005, q95 = 0.995, nsample = -1, save_img: str = "")
pd_plot_tseries_matplot(df:pd.DataFrame, plot_type: str = None, cols_axe1: list  =  [], cols_axe2: list  =  [], 8, 4), spacing = 0.1, **kw))
mpld3_server_start()
pd_plot_tseries_highcharts(df, coldate:str = None, date_format:str = '%m/%d/%Y', cols_axe1:list  = [], cols_axe2:list  = [], figsize:tuple  =   None, title:str = None, x_label:str = None, axe1_label:str = None, axe2_label:str = None, cfg:dict = {}, mode = 'd3', save_img = "")
pd_plot_histogram_highcharts(df:pd.DataFrame, colname:str = None, binsNumber = None, binWidth = None, title:str = "", xaxis_label:str =  "x-axis", yaxis_label:str = "y-axis", cfg:dict = {}, mode = 'd3', save_img = "", show = False)
html_show_chart_highchart(html_code, verbose = True)
html_show(html_code, verbose = True)
images_to_html(dir_input = "*.png", title = "", verbose = False)
pd_plot_network(df:pd.DataFrame, cola: str = 'col_node1', colb: str = 'col_node2', coledge: str = 'col_edge', colweight: str = "weight", html_code:bool  =  True)
help_get_codesource(func)
zz_css_get_template(css_name:str =  "A4_size")
zz_test_get_random_data(n = 100)
zz_pd_plot_histogram_highcharts_old(df, col, figsize = None, title = None, cfg:dict = {}, mode = 'd3', save_img = '')

-------------------------methods----------------------
htmlDoc.__init__(self, dir_out = "", mode = "", title: str = "", format: str  =  None, cfg: dict  = None, css_name:str = "a4_size")
htmlDoc.tag(self, x)
htmlDoc.h1(self, x, css: str = '')
htmlDoc.h2(self, x, css: str = '')
htmlDoc.h3(self, x, css: str = '')
htmlDoc.h4(self, x, cs: str = '')
htmlDoc.p(self, x, css: str = '')
htmlDoc.div(self, x, css: str = '')
htmlDoc.hr(self, css: str = '')
htmlDoc.sep(self, css: str = '')
htmlDoc.br(self, css: str = '')
htmlDoc.get_html(self)
htmlDoc.print(self)
htmlDoc.save(self, dir_out = None)
htmlDoc.open_browser(self)
htmlDoc.add_css(self, css)
htmlDoc.add_js(self, js)
htmlDoc.hidden(self, x, css: str = '')
htmlDoc.table(self, df:pd.DataFrame, format: str = 'blue_light', custom_css_class = None, use_datatable = False, table_id = None, **kw)
htmlDoc.plot_histogram(self, df:pd.DataFrame, col, 14, 7), nsample = 10000, nbin = 10, q5 = 0.005, q95 = 0.95, cfg: dict  =  {}, mode: str = 'matplot', save_img = "", **kw)
htmlDoc.plot_scatter(self, df:pd.DataFrame, colx, coly, 14, 7), nsample: int = 10000, collabel = None, colclass1 = None, colclass2 = None, colclass3 = None, cfg: dict  =  {}, mode: str = 'matplot', save_img = '', **kw)
htmlDoc.images_dir(self, dir_input = "*.png", title: str = "", verbose:bool  = False)
htmlDoc.pd_plot_network(self, df:pd.DataFrame, cola: str = 'col_node1', colb: str = 'col_node2', coledge: str = 'col_edge')
mpld3_TopToolbar.__init__(self)
