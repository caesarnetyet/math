import sympy as sp
from sympy import latex, Eq, simplify, expand, solve, dsolve
from sympy.abc import y, x, C


def separable_variables_solver(ode):
    steps = []
    lhs_str, rhs_str = ode.split("=")
    dy_dy = simplify(lhs_str)
    expression = simplify(rhs_str)
    steps.append("Dada la ecuación diferencial" + latex(Eq(dy_dy, expression)))

    y_terms = get_related_terms(expression, y, invert=True)
    lhs = simplify(1)
    for term in y_terms:
        lhs = lhs * term
    lhs_integrated = sp.integrate(lhs, y)

    rhs = simplify(1)
    x_terms = get_related_terms(expression, x)
    for term in x_terms:
        rhs = rhs * term
    rhs_integrated = sp.integrate(rhs, x) + C
    steps.append(f"Integrar ambos lados: ∫{lhs}dy = ∫{rhs}dx")

    general = Eq(lhs_integrated, rhs_integrated)
    steps.append("Integrado" + latex(general))

    solution = solve(general, y)

    steps.append("La solución es" + latex(solution))

    return steps


def get_related_terms(expression, variable, invert=False):
    terms = []
    print(f"Expression: {expression}")

    # Use args to break the expression into terms
    for term in expression.as_ordered_factors():
        if variable in term.free_symbols:
            print(term)
            if invert:
                term = term**-1
            terms.append(term)

    return terms


if __name__ == "__main__":
    # Example usage:
    solution = separable_variables_solver("dy/dx = (2*x**2)/y")
    for step in solution:
        print(step)