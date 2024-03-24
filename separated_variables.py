import sympy as sp
from sympy import latex, Eq, simplify, expand, solve
from sympy.abc import y, x, C


def separable_variables_solver(ode):
    steps = []
    # Parse the input ODE
    lhs_str, rhs_str = ode.split("=")
    dy_dy = simplify(lhs_str)
    expression = simplify(rhs_str)

    steps.append(("Dada la ecuación diferencial", latex(Eq(dy_dy, expression))))

    # Move variables from x to dx and y to dy
    y_terms = get_related_terms(expression, y, invert=True)
    lhs = simplify(1)
    for term in y_terms:
        lhs = lhs * term
    print(f"lhs: {lhs}")
    lhs_integrated = sp.integrate(lhs, y)

    rhs = simplify(1)
    x_terms = get_related_terms(expression, x)
    for term in x_terms:
        rhs = rhs * term
    print(f"rhs: {rhs}")
    rhs_integrated = sp.integrate(rhs, x) + C

    general = Eq(lhs_integrated, rhs_integrated)
    print(latex(general))
    solution = solve(general, y)
    print(latex(solution))

    return steps


def get_related_terms(expression, variable, invert=False):
    terms = []
    print(f"Expression: {expression}")
    # Expand the expression to ensure it's in a form that can be iterated over
    expanded_expr = expand(expression)
    for term in expanded_expr.as_ordered_factors():
        if term.has(variable):
            if invert:
                term = term**-1
            terms.append(term)
    return terms


if __name__ == "__main__":
    # Example usage:
    solution = separable_variables_solver("dy/dx = x/y")
    print(f"Solution for dy/dx = y/x: {sp.latex(solution)}")
    solution = separable_variables_solver("dy/dx = x**2")
    print(f"Solution for dy/dx = 2*x**2: {sp.latex(solution)}")
