from sympy import Function, Eq, Derivative, integrate, symbols, exp, sympify, simplify
from sympy.abc import x


def solve_non_homogeneous_equation(differential_part, function_part, non_homogeneous_part):
    steps = []

    y = Function('y')(x)

    P = sympify(function_part)
    g = sympify(non_homogeneous_part)
    differential_eq = Derivative(y, x) * sympify(differential_part) + P * y - g

    eq = Eq(differential_eq, 0)

    steps.append(f"Ecuación Original: {eq}")

    mu = exp(integrate(P, x))
    steps.append(f"Integrar factor (mu): {mu}")

    eq_mu = Eq(mu * differential_eq, 0)
    steps.append(f"Ecuación después de multiplicar por su factor Mu: {eq_mu}")

    lhs = Derivative(mu * y, x)
    steps.append(f"Lado izquierdo después de multiplicar por su factor integral Mu: {lhs}")

    integrated_lhs = integrate(lhs, x)
    integrated_rhs = integrate(mu * g, x)
    steps.append(f"Integral lado izquierdo: {integrated_lhs}")
    steps.append(f"Integral Lado derecho: {integrated_rhs}")

    C1 = symbols('C1')
    general_solution = Eq(integrated_lhs, integrated_rhs + C1)
    steps.append(f"Solución general: {general_solution}")

    simplified_solution = simplify(general_solution.rhs)
    steps.append(f"Solución simplificada: {simplified_solution}")

    return steps

# Example usage:
if __name__ == "__main__":
    differential_part = "1/x"
    function_part = "2"
    non_homogeneous_part = "exp(x)/x"

    steps = solve_non_homogeneous_equation(differential_part, function_part, non_homogeneous_part)
    for step in steps:
        print(step)