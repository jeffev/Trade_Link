import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State
from pages.home import Home
from pages.trades import Trades
from pages.desempenho import Desempenho
from components.navbar import Navbar
from components.sidebar import Sidebar, SIDEBAR_STYLE, CONTENT_STYLE1, SIDEBAR_HIDEN, CONTENT_STYLE

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

content = html.Div(
    id="page-content",
    style=CONTENT_STYLE
)

app.layout = dbc.Container([
    dcc.Store(id='side_click'),
    dcc.Location(id='url', refresh=False),
    Navbar(user="Nome do Usuário"),  # Substitua pelo nome real do usuário
    Sidebar(),
    content,
], fluid=True)

# Callback to toggle the sidebar
@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

# Callback para atualizar o conteúdo da página com base na URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return Home()
    elif pathname == '/trades':
        return Trades()
    elif pathname == '/desempenho':
        return Desempenho()
    else:
        return '404 Página não encontrada'

if __name__ == "__main__":
    app.run_server(debug=True)
