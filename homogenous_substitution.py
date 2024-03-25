import sympy as sp

def solve_homogenous_ode(ode_str):
    x, y, u, c = sp.symbols('x y u c')
    steps = ["**Paso 1: Transformar la diferencial**", f"Dada la diferencial: {ode_str}"]

    # Separar la ODE en LHS y RHS
    parts = ode_str.split('=')
    lhs = sp.sympify(parts[0].strip())
    rhs = sp.sympify(parts[1].strip())

    # Paso 2: Determinar la variable dependiente y hacer la sustitución
    steps.append("\n**Paso 2: Determinar la variable dependiente y sustitución**")
    substitution = {'y': u * x, 'dy/dx': u + x*sp.diff(u, x)}
    steps.append("y es la variable dependiente.")
    steps.append(f"Sustitución: y = ux, dy/dx = u + x*du/dx")

    # Paso 3: Aplicar sustitución
    steps.append("\n**Paso 3: Aplicar sustitución**")
    lhs_subst = lhs.subs(substitution)
    rhs_subst = rhs.subs(substitution)
    steps.append(f"Ecuación después de la sustitución: {lhs_subst} = {rhs_subst}")

    # Paso 4: Separar variables
    steps.append("\n**Paso 4: Separar variables**")
    sep_eq = sp.Eq(lhs_subst - rhs_subst, 0)
    sep_vars = sp.separatevars(sep_eq, symbols=(u, x), force=True)
    steps.append(f"Ecuación separada: {sep_vars}")

    # Paso 5: Integrar
    steps.append("\n**Paso 5: Integrar**")
    expression = sep_vars.lhs

    int_result = sp.integrate(expression, u)
    steps.append(f"Resultado de integración: {int_result} = C")

    # Paso 6: Deshacer la sustitución
    steps.append("\n**Paso 6: Deshacer la sustitución**")
    u_solution = sp.exp(int_result)
    y_solution = u_solution.subs(u, y/x)
    steps.append(f"Solución en términos de x y y: y = {y_solution}")

    return steps

# Ejemplo de uso
ode = "dy/dx = y/x"
solution_steps = solve_homogenous_ode(ode)
for step in solution_steps:
    print(step)