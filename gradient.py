import dash
from dash import dcc, html, Input, Output, State, dash_table
import plotly.graph_objs as go
import numpy as np
import math

# Функция f(x1, x2)
def f(x1, x2):
    return 2 * x1**2 + x1 * x2 + x2**2

# Градиент функции
def grad_f(point):
    x1, x2 = point
    return [4 * x1 + x2, x1 + 2 * x2]

# Норма вектора
def norma(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)

# Градиентный спуск
def gradient_descent(start, step, eps):
    iteration_count = 0
    curr_point = list(start)
    trajectory = [curr_point.copy()]
    history = []
    while True:
        grad = grad_f(curr_point)
        norm = norma(grad)
        history.append({"Iteration": iteration_count, "x1": curr_point[0], "x2": curr_point[1], "f(x1, x2)": f(curr_point[0], curr_point[1]), "Norm": norm})
        if norm < eps:
            break
        iteration_count += 1
        curr_point[0] -= step * grad[0]
        curr_point[1] -= step * grad[1]
        trajectory.append(curr_point.copy())
    return curr_point, trajectory, history

# Генерация 3D графика
def create_surface():
    x = np.linspace(-2, 2, 50)
    y = np.linspace(-2, 2, 50)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    return go.Surface(x=X, y=Y, z=Z, colorscale='viridis', opacity=0.8)

# Инициализация Dash
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Метод градиентного спуска"),
    html.Label("Начальная точка x1:"),
    dcc.Input(id="x1", type="number", value=0.5, step=0.1),
    html.Label("Начальная точка x2:"),
    dcc.Input(id="x2", type="number", value=1.0, step=0.1),
    html.Label("Шаг обучения (alpha):"),
    dcc.Input(id="alpha", type="number", value=0.1, step=0.01),
    html.Label("Точность (epsilon):"),
    dcc.Input(id="epsilon", type="number", value=0.15, step=0.01),
    html.Button("Найти минимум", id="run", n_clicks=0),
    dcc.Graph(id="graph"),
    dash_table.DataTable(id="table", columns=[
        {"name": "Iteration", "id": "Iteration"},
        {"name": "x1", "id": "x1"},
        {"name": "x2", "id": "x2"},
        {"name": "f(x1, x2)", "id": "f(x1, x2)"},
        {"name": "Norm", "id": "Norm"}
    ])
])

@app.callback(
    [Output("graph", "figure"), Output("table", "data")],
    [Input("run", "n_clicks")],
    [State("x1", "value"), State("x2", "value"), State("alpha", "value"), State("epsilon", "value")]
)
def update_graph(n_clicks, x1, x2, alpha, epsilon):
    if n_clicks == 0:
        return go.Figure(data=[create_surface()]), []
    minimum, trajectory, history = gradient_descent([x1, x2], alpha, epsilon)
    
    traj_x = [p[0] for p in trajectory]
    traj_y = [p[1] for p in trajectory]
    traj_z = [f(p[0], p[1]) for p in trajectory]
    
    fig = go.Figure(data=[create_surface()])
    fig.add_trace(go.Scatter3d(x=traj_x, y=traj_y, z=traj_z, mode='lines+markers',
                                marker=dict(size=5, color='red'),
                                line=dict(color='red', width=3),
                                name="Путь к минимуму"))
    fig.update_layout(title="Градиентный спуск", scene=dict(zaxis_title="f(x1, x2)"))
    return fig, history

if __name__ == "__main__":
    app.run_server(debug=True)
