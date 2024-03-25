import sympy as sp


def solve_second_order_non_homogeneous(coef_y_prime, coef_independent, coef_x_squared, coef_x, term_independent):
    steps = []
    x = sp.symbols('x')

    a = 1  # Coefficient of y''
    b = coef_y_prime
    c = coef_independent
    d = coef_x_squared
    e = coef_x
    f = term_independent

    steps.append(f"Ecuación original: y'' + {b}y' + {c}y = {d}x² + {e}x + {f}")

    characteristic_eq = a * x ** 2 + b * x + c
    roots = sp.solve(characteristic_eq, x)

    if not roots:
        steps.append("No se encontraron raíces para la solución.")
        return steps

    # Assume a particular solution of the form Yp = Ax^2 + Bx + C
    A, B, C = sp.symbols('A B C')
    Yp = A * x ** 2 + B * x + C
    Yp_prime = sp.diff(Yp, x)
    Yp_double_prime = sp.diff(Yp_prime, x)

    equation = a * Yp_double_prime + b * Yp_prime + c * Yp - (d * x ** 2 + e * x + f)

    eqs = [sp.Eq(equation.coeff(x, i), 0) for i in range(3)]
    sol = sp.solve(eqs, (A, B, C))

    if not sol:
        steps.append("No se encontraron soluciones para:  A, B, C.")
        return steps

    # Display the results
    A_value, B_value, C_value = sol[A], sol[B], sol[C]
    steps.append(f"Soluciones para A, B, C: A = {A_value}, B = {B_value}, C = {C_value}")

    # Combine the complementary and particular solutions
    complementary_solution = f"C1*exp({roots[0]}*x) + C2*exp({roots[1]}*x)"
    particular_solution = f"({A_value})*x^2 + ({B_value})*x + {C_value}"
    general_solution = f"{complementary_solution} + {particular_solution}"
    steps.append(f"Solución general: y(x) = {general_solution}")

    return steps


if __name__ == "__main__":
    coef_y_prime = 1
    coef_independent = 0
    coef_x_squared = 2
    coef_x = 7
    term_independent = 4

    detailed_steps = solve_second_order_non_homogeneous(
        coef_y_prime,
        coef_independent,
        coef_x_squared, coef_x,
        term_independent)
    for step in detailed_steps:
        print(step)
