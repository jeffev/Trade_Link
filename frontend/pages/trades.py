from dash import html

def Trades():
    return html.Div([
        html.H1("Lista de Trades"),
        html.P("Aqui você verá a lista de trades cadastrados."),
    ])
