from dash import Input, Output, html, dash_table
from gradient_1 import gradient_descent, generate_surface_data

def register_callbacks(app):
    @app.callback(
        [Output("output", "children"),
         Output("graph", "figure"),
         Output("table", "children")],
        [
            Input("start-x1", "value"),
            Input("start-x2", "value"),
            Input("eps1-input", "value"),
            Input("eps2-input", "value"),
            Input("submit-button", "n_clicks")
        ]
    )
    def update_output(start_x1, start_x2, eps1, eps2, n_clicks):
        figure = generate_surface_data()
        table = ""
        if n_clicks > 0:
            start = [float(start_x1), float(start_x2)]
            step = float(eps1)
            eps = float(eps2)

            #Вызываем метод градиентного спуска

            result = gradient_descent(start, step, eps)

            figure = generate_surface_data(result["history"])

            print(result["history"])

            table = dash_table.DataTable(
                columns=[
                    {"name":"Итерация", "id": "iteration"},
                    {"name":"x1", "id": "x1"},
                    {"name":"x2", "id": "x2"},
                    {"name":"Значение нормы градиента", "id":"norm"}
                ],
                data = [
                    {
                        "iteration":i,
                        "x1": round(point[0], 5),
                        "x2":round(point[1], 5),
                        "norm": round(norm, 5)
                    }
                    for i, (point, norm) in enumerate(zip(result["history"], result["norm_history"]))
                    
                ],
                style_table={"overflowX": "auto"},
                style_cell={"textAlign": "center"},
            )

            result_output = html.Div(id="result", children = [
                html.Div(className="result-item", children= [
                    html.P(f"Минимум найден в точке: ({round(result['min_point'][0], 6)}; {round(result['min_point'][1], 6)})")
                ]),
                html.Div(className="result-item", children = [
                    html.P(f"Минимальное значение функции: {round(result['min_value'], 6)}")
                ]),
                html.Div(className="result-item", children=[
                    html.P(f"Итераций: {result['iteration_count']}")
                ])      
            ])
            
            return result_output, figure, table
        return "", figure, table