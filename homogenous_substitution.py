import sympy as sp


def solve_homogenous_ode(ode_str):
    """Solves a first-order homogenous ODE using the substitution method.

    Args:
        ode_str: The ODE in string format (e.g., "y' = x/y")

    Returns:
        A list of strings explaining each step of the solution process.
    """

    x, y, u, c = sp.symbols('x y u c')

    steps = ["**Paso 1: transformar la diferencial**", f"Dada la diferencial: {ode_str}"]

    try:
        parts = ode_str.split("=")
        lhs = sp.sympify(parts[0].strip())
        rhs = sp.sympify(parts[1].strip())
        steps.append(f"Lado izquierdo (LHS): {lhs}")
        steps.append(f"Lado derecho (RHS): {rhs}")
    except:
        steps.append("Error: Formato invalido. Por favor usa el formato 'dy/dx' = <expression>'")
        return steps

    steps.append("\n**Paso 2: Determinar la variable dependiente y substitución**")
    if len(str(lhs)) < len(str(rhs)):  # Verificar que lado es mas complejo
        steps.append("'X' es la variable dependiente")
        substitution = {'x': u * y, 'dx': u * sp.diff(y) + y * sp.diff(u)}
        steps.append(f"Substitución: x = uy, dx = u*dy + y*du")
    else:
        steps.append("y Es la variable dependiente.")
        substitution = {'y': u * x, 'dy': u * sp.diff(x) + x * sp.diff(u)}
        steps.append(f"Substitución: y = ux, dy = u*dx + x*du")

    steps.append("\n**Paso 3: Aplicar substitución**")
    lhs_subst = lhs.subs(substitution)
    rhs_subst = rhs.subs(substitution)
    steps.append(f"Ecuación después de la substitución: {lhs_subst} = {rhs_subst}")

    steps.append("\n**Paso 4: Separar variables**")
    try:
        sep_eq = sp.Eq(lhs_subst, rhs_subst)
        sep_vars = sp.separatevars(sep_eq, [sp.diff(y), sp.diff(u)], dict=True)
        steps.append(f"Ecuación separada: {sep_vars}")
    except:
        steps.append("Error: No se pudieron separar las variables")
        steps.append(f"Ecuación no separada: {sp.Eq(lhs_subst, rhs_subst)}")
        return steps

    steps.append("\n**Paso 5: Integrar**")
    try:
        int_result = sp.integrate(sep_vars[sp.diff(u)], u)
        steps.append(f"Resultado de integración: {int_result} = C")
    except:
        steps.append("Error: No se pudo integrar.")
        return steps

    return steps


# Example usage
ode = "dy/dx = (2*x + 3*y)/(3*x + 2*y)"
solution_steps = solve_homogenous_ode(ode)
for step in solution_steps:
    print(step)
