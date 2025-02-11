import math
import numpy as np
import plotly.graph_objects as go
#Основная функция f(x) = 2*x_1^2 + x1*x2 + x_2^2

def f(point):
    x1 = point[0]
    x2 = point[1]
    return 2 * math.pow(x1,2) + x1 * x2 + math.pow(x2,2)

#Градиент функции
def grad_f(point):
    x1 = point[0]
    x2 = point[1]
    return [4* x1 + x2, x1 + 2 * x2]

def norma(vector):
    return math.sqrt(math.pow(vector[0],2) + math.pow(vector[1],2))



def gradient_descent(start, step, eps):
    iteration_count = 0
    curr_point = start
    history = []
    norm_history = []
    while True:
        grad = grad_f(curr_point)
        history.append(curr_point.copy())
        norm_history.append(norma(grad))
        if iteration_count > 2 and abs(f(history[len(history) - 2]) - f(curr_point)) < eps:
            print(f(history[len(history) - 1]))
            print(f(curr_point))
            break
        iteration_count += 1
        curr_point[0] -= step * grad[0]
        curr_point[1] -= step * grad[1]
    return {
        "iteration_count": iteration_count,
        "min_point": curr_point,
        "min_value": f(curr_point),
        "history": history,
        "norm_history": norm_history
    }


# Генерация данных для графика
def generate_surface_data(history=None):
    # Создаем сетку значений для x1 и x2
    x1_vals = np.linspace(-3, 3, 100)
    x2_vals = np.linspace(-3, 3, 100)
    X1, X2 = np.meshgrid(x1_vals, x2_vals)

    # Вычисляем значения функции для каждой точки
    Z = 2 * X1**2 + X1 * X2 + X2**2

    # Создаем 3D-график поверхности
    fig = go.Figure(data=[go.Surface(z=Z, x=X1, y=X2)])

    # Если передана история итераций, добавляем точки на график
    if history:
        x_hist = [point[0] for point in history]
        y_hist = [point[1] for point in history]
        z_hist = [2 * x**2 + x * y + y**2 for x, y in history]  # Значения функции в точках

        fig.add_trace(go.Scatter3d(
            x=x_hist,
            y=y_hist,
            z=z_hist,
            mode="markers+lines",
            marker=dict(size=5, color="red"),
            name="Градиентный спуск"
        ))

    fig.update_layout(
        title={
        'text': " График функции f(x₁, x₂) = 2x₁² + x₁x₂ + x₂²",
        'x': 0.5,  
        'font': {'size': 18} 
    },
        scene=dict(
            xaxis_title="x1",
            yaxis_title="x2",
            zaxis_title="f(x)"
        )
    )

    return fig


