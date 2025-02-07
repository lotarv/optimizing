from dash import html, dcc

layout = html.Div(children=[
    html.Div(className="inputs", children=[
        html.H3("Стартовая точка"),
        html.Div(className="input-row", children=[
            dcc.Input(id="start-x1", type="number", value='', placeholder="x1", className="input-field"),
            dcc.Input(id="start-x2", type="number", value='', placeholder="x2", className="input-field"),
        ]),
    
        html.H3("Шаг итерации"),
        html.Div(className="input-row", children=[
            dcc.Input(id="eps1-input", type="number", value='', placeholder="Шаг итерации", className="input-field"),
        ]),
    
        html.H3("Точность"),
        html.Div(className="input-row", children=[
            dcc.Input(id="eps2-input", type="number", value='', placeholder="Точность", className="input-field"),
        ]),

    html.Button("Рассчитать", id="submit-button", n_clicks=0, className="submit-button")
    ]),

    html.Div(id="output"),

    dcc.Graph(id="graph", style={"height":"500px"}),

    # Таблица с итерациями
    html.Div(id="table", style={"marginTop": "20px"}),
    

])