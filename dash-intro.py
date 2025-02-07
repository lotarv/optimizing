import dash
from dash import html, dcc
from dash.dependencies import Input, Output

#Создание приложения

# app = dash.Dash(__name__)

# #Определение макета страницы

# app.layout = html.Div(children=[
#     dcc.Input(id="input-text", type="text", value='', placeholder="Введите что-то"),
#     html.H3(id="output-text")
# ])

# @app.callback(
#     Output("output-text", "children"),
#     Input("input-text", "value")
# )

# def update_output(value):
#     return f"Вы ввели {value}"
# #Запуск сервера

# if __name__ == '__main__':
#     app.run_server(debug=True)


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    dcc.Input(id="input-text", type="text", value='', placeholder='Введите что-то'),
    html.H3(id="output-text")
])

@app.callback(
    Output("output-text", "children"),
    Input("input-text", "value")
)

def update_output(value):
    return f"Вы ввели {value}"

app.run_server(debug=True)