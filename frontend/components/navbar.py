import dash_bootstrap_components as dbc
from dash import html

def Navbar(user):
    user_name = dbc.Row(
        [
            dbc.Col(
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("More pages", header=True),
                        dbc.DropdownMenuItem("Page 2", href="#"),
                        dbc.DropdownMenuItem("Page 3", href="#"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label=(f"Bem-vindo, {user}!"),
                    align_end=True
                ),
                width="auto",
            ),
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    )
        
    return dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.Button(
                            html.I(className="fas fa-bars"),
                            color="secondary",
                            id="btn_sidebar",
                        )),
                        dbc.Col(dbc.NavbarBrand("TradeLink", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="#",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                user_name,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid=True
    ),
    color="#0d6efd"
)