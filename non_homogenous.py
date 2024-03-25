from sympy import Function, dsolve, Eq, Derivative, sympify, simplify
from sympy.abc import x


def non_homogeneous_solver(function_part, non_homogeneous_part):
    steps = []
    y = Function('y')(x)

    P = sympify(function_part)
    g = sympify(non_homogeneous_part)
    differential_eq = Derivative(y, x) + P * y - g

    eq = Eq(differential_eq, 0)

    steps.append(f"Original equation: {eq}")

    solution = dsolve(eq, y)
    steps.append(f"Solution: {solution}")

    simplified_solution = simplify(solution.rhs)
    steps.append(f"Simplified solution: {simplified_solution}")

    return steps


if __name__ == "__main__":
    function_part = "2/x"
    non_homogeneous_part = "exp(x)/x"

    steps = non_homogeneous_solver(function_part, non_homogeneous_part)
    for step in steps:
        print(step)
