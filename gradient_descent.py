""" Gradient descent algorithm."""
# imports
from sympy import symbols, diff, simplify

# macros
learn_rate = 0.01

# functions
def f(x):
    """ The function to be optimized."""
    return 2 * x**3 + y**2 + 5

def get_partial_derivative(expression, variable):
    """
    Return the partial derivative of the function (expression) 
    with respect to `variable` using the power rule.
    """
    expr = simplify(expression)

    if 'x' in variable:
        x = symbols('x')
        derivative = diff(expr, x)
    elif 'y' in variable:
        y = symbols('y')
        derivative = diff(expr, y)
    elif 'z' in variable:
        z = symbols('z')
        derivative = diff(expr, z)

    simplified_derivative = simplify(derivative)
    return simplified_derivative

def gradient_descent(x, y, gradient_vector):
    """ Perform gradient descent."""
    x_new = x - (learn_rate * gradient_vector[0])
    y_new = y - (learn_rate * gradient_vector[1])
    return x_new, y_new

def get_gradient_vector(expression, variables):
    """ Get the gradient vector for a given function."""
    gradient_vector = [get_partial_derivative(expression, variable) for variable in variables]
    return gradient_vector
