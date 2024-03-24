import sympy as sp
from sympy import Function, dsolve, Eq, Derivative, latex
from sympy.abc import x, C

# Define the function for the method of variation of parameters
def non_homogeneous_solver(p, q):
    steps = []
    y = Function('y')

    # Define the differential equation
    ode = Eq(Derivative(y(x), x) + p * y(x), q)

    # Display the differential equation
    steps.append(("Given the non-homogeneous differential equation", latex(ode)))

    # Solve the differential equation using dsolve with the correct hint
    solution = dsolve(ode, y(x), hint='nth_linear_constant_coeff_variation_of_parameters')

    # Simplify the solution
    simplified_solution = solution.simplify()

    # Display the simplified solution
    steps.append(("The simplified solution is", latex(simplified_solution)))

    return steps

# Example usage:
if __name__ == "__main__":
    p = 2 * x  # Example P(x)
    q = sp.exp(x)  # Example Q(x)
    steps = non_homogeneous_solver(p, q)
    for step in steps:
        print(step[0])
        print(step[1])