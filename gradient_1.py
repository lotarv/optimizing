import math
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



#Стартовая точка
start = [0.5,1]

def gradient_descent(start, step, eps):
    iteration_count = 0
    curr_point = start
    while True:
        grad = grad_f(curr_point)
        if norma(grad) < eps:
            break
        iteration_count += 1
        curr_point[0] -= step * grad[0]
        curr_point[1] -= step * grad[1]
    print(f"итераций: {iteration_count}")
    print(f"Минимум найден в точке: {curr_point}")
    print(f"Значение функции в минимуме: {f(curr_point)}")


gradient_descent(start, 0.1,0.15)


