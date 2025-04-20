# calculus.py
# It's over
from sympy import symbols
from sympy import (
    symbols, sin, cos, tan, log, exp, sqrt, Abs,
    Integral, limit, simplify, oo, pi, S, latex
)
import streamlit as st
import random
from sympy import latex


def generate_calculus(concept,  num_problems):
    problems = []
    solutions = []

    problem_type = st.selectbox(
    "Choose problem type:",
    ["Integrals", "Limits", "Derivatives", "Polars", "Series"],
    key=f"{concept}_problem_type"
)

    category = st.selectbox(
        "Category Level",
        options=[
            "Application of Integrals", "Fudemental Theorem of Calculus", "Related Rates", "Improper Integrals",
            "Area and Volume", "Partical Motion", "Derivative at a Point", "Differential Equations",
            "Chain Rule", "Product Rule", "Quotient Rule", "Derivatives of Trig Functions"
        ],
        key=f"{concept}_category"
    )
   
    difficulty = st.select_slider(
        "Difficulty level:",
        options=["Easy", "Medium", "Hard"],
        value="Medium",
        key=f"{concept}_difficulty"
   )

    def generate_random_polynomial(degree=3, coef_range=(-5, 5)):
        x = symbols('x')
        
        # Generate polynomial: random coefficient for each power of x
        poly = sum(random.randint(*coef_range) * x**i for i in range(degree + 1))
        return poly

    def create_integral(poly_expr, definite=False) -> Integral:
        x = symbols('x')
        
        if definite:
            a, b = sorted(random.sample(range(-10, 11), 2))
            integral_expr = Integral(poly_expr, (x, a, b))
        else:
            integral_expr = Integral(poly_expr, x)
        
        return integral_expr

    def generate_easy_expression(x, approach_point):
        """Generate an easy limit expression."""
        # Basic expressions for easy problems
        expression_type = random.randint(1, 5)
        
        if expression_type == 1:
            # Polynomial expressions
            degree = random.randint(1, 3)
            coeffs = [random.randint(-5, 5) for _ in range(degree + 1)]
            expr = sum(coeff * x**i for i, coeff in enumerate(coeffs))
        
        elif expression_type == 2:
            # Simple rational expressions
            num_degree = random.randint(0, 2)
            den_degree = random.randint(0, 2)
            num_coeffs = [random.randint(-5, 5) for _ in range(num_degree + 1)]
            den_coeffs = [random.randint(-5, 5) for _ in range(den_degree + 1)]
            
            # Ensure denominator is not zero
            while den_coeffs[-1] == 0:
                den_coeffs[-1] = random.randint(-5, 5)
            
            numerator = sum(coeff * x**i for i, coeff in enumerate(num_coeffs))
            denominator = sum(coeff * x**i for i, coeff in enumerate(den_coeffs))
            expr = numerator / denominator
        
        elif expression_type == 3:
            # Basic trigonometric functions
            trig_funcs = [sin(x), cos(x), tan(x)]
            expr = random.choice(trig_funcs)
        
        elif expression_type == 4:
            # Simple exponential/logarithmic
            if approach_point != 0:  # Avoid log(0)
                funcs = [exp(x), log(x)]
                expr = random.choice(funcs)
            else:
                expr = exp(x)
        
        else:
            # Polynomial + trig
            degree = random.randint(1, 2)
            coeffs = [random.randint(-3, 3) for _ in range(degree + 1)]
            poly = sum(coeff * x**i for i, coeff in enumerate(coeffs))
            
            trig_funcs = [sin(x), cos(x)]
            trig = random.choice(trig_funcs)
            
            expr = poly + trig
        
        return expr

    def generate_medium_expression(x, approach_point):
        """Generate a medium difficulty limit expression."""
        expression_type = random.randint(1, 6)
        
        if expression_type == 1:
            # L'Hôpital's rule candidates (0/0 form)
            if approach_point in [0, 1, 2, -1, -2, pi]:
                # Create expression where both num and den go to 0
                num = (x - approach_point) * (random.randint(1, 3) * x + random.randint(-3, 3))
                den = (x - approach_point) * (random.randint(1, 3) * x + random.randint(-3, 3))
                expr = num / den
            else:
                # For infinity, create expression where both go to infinity
                num = x**random.randint(2, 3) + random.randint(-5, 5)
                den = x**random.randint(2, 3) + random.randint(-5, 5)
                expr = num / den
        
        elif expression_type == 2:
            # sin(x)/x and variations (famous limit)
            if approach_point == 0:
                k = random.randint(1, 3)
                expr = sin(k*x)/(k*x)
            else:
                # Create other indeterminate forms
                expr = sin(x)/x * (x/(x-approach_point))
        
        elif expression_type == 3:
            # (1 + 1/x)^x and variations (approaches e)
            if approach_point in [oo, -oo]:
                k = random.randint(1, 3)
                expr = (1 + k/x)**(x/k)
            else:
                expr = (1 + 1/(x-approach_point))**(x-approach_point)
        
        elif expression_type == 4:
            # Rational functions with potential cancelations
            num_degree = random.randint(1, 3)
            den_degree = random.randint(1, 3)
            
            # Create factors that will cancel
            factor = x - approach_point if approach_point != oo and approach_point != -oo else 1
            
            num_poly = factor
            den_poly = factor
            
            # Add additional terms
            for _ in range(num_degree):
                coeff = random.randint(-3, 3)
                if coeff != 0:
                    num_poly *= (x + coeff)
            
            for _ in range(den_degree):
                coeff = random.randint(-3, 3)
                if coeff != 0:
                    den_poly *= (x + coeff)
            
            expr = num_poly / den_poly
        
        elif expression_type == 5:
            # Composite functions
            inner = x**2 + random.randint(-3, 3)
            outer_funcs = [sin, cos, exp, sqrt]
            outer = random.choice(outer_funcs)
            expr = outer(inner)
        
        else:
            # Difference quotient (derivative definition)
            f_x = x**random.randint(2, 3) + random.randint(-3, 3)*x
            h = x - approach_point
            f_x_plus_h = (x + h)**random.randint(2, 3) + random.randint(-3, 3)*(x + h)
            expr = (f_x_plus_h - f_x) / h
        
        return expr

    def generate_hard_expression(x, approach_point):
        """Generate a hard difficulty limit expression."""
        expression_type = random.randint(1, 6)
        
        if expression_type == 1:
            # Complex indeterminate forms
            if approach_point in [0, 1, 2, -1, -2, pi]:
                # Create a complex indeterminate form
                num = sin(x - approach_point)
                den = (x - approach_point)**random.randint(1, 3)
                expr = num / den
            else:
                # For infinity
                num = x**random.randint(3, 5) * sin(1/x)
                den = x**random.randint(3, 5)
                expr = num / den
        
        elif expression_type == 2:
            # Multiple L'Hôpital applications needed
            if approach_point in [0, 1, 2, -1, -2, pi]:
                # Higher order indeterminates
                num = (x - approach_point)**random.randint(2, 4)
                den = (x - approach_point)**random.randint(2, 4) * log(1 + abs(x - approach_point))
                expr = num / den
            else:
                # For infinity
                expr = (log(x))**random.randint(2, 4) / x
        
        elif expression_type == 3:
            # Trigonometric with algebraic manipulation needed
            if approach_point == 0:
                expr = (1 - cos(x**2))/(x**4)
            else:
                expr = sin(1/x) * (x**2)
        
        elif expression_type == 4:
            # Exponential and logarithmic combinations
            if approach_point != 0:  # Avoid log(0)
                base = random.randint(2, 10)
                expr = (base**x - 1) / log(1 + x)
            else:
                expr = x * exp(1/x)
        
        elif expression_type == 5:
            # Nested functions
            inner1 = x**2 + random.randint(-3, 3)
            inner2 = sin(x) + random.randint(-3, 3)
            
            # Combine in interesting ways
            if random.choice([True, False]):
                expr = (inner1) / inner2
            else:
                expr = log(1 + abs(inner1)) / inner2
        
        else:
            # Create a function that would use the squeeze theorem
            if approach_point == 0:
                expr = x**2 * sin(1/x)
            else:
                expr = (x**2 * sin(x))/(x - approach_point)
        
        return expr
        
        
    def generate_random_limit_problem(difficulty="Medium"):
        """
        Generate a random calculus limit problem and calculate its solution.
        Returns:
            tuple: (problem_statement, solution, latex_expression, latex_solution)
        """
        x = symbols('x')
        
        approach_options = {
            "Easy": [0, 1, 2, -1, -2, oo, -oo],
            "Medium": [0, 1, 2, -1, -2, oo, -oo, S.Half, -S.Half],
            "Hard": [0, 1, 2, -1, -2, oo, -oo, S.Half, -S.Half, pi]
        }
        
        approach_point = random.choice(approach_options[difficulty])
        
        # Generate a random expression based on difficulty
        if difficulty == "Easy":
            expr = generate_easy_expression(x, approach_point)
        elif difficulty == "Medium":
            expr = generate_medium_expression(x, approach_point)
        else:  # Hard
            expr = generate_hard_expression(x, approach_point)
        
        # Format approach point for display
        if approach_point == oo:
            approach_str = "∞"
        elif approach_point == -oo:
            approach_str = "-∞"
        elif approach_point == pi:
            approach_str = "π"
        else:
            approach_str = str(approach_point)
        
        # Calculate the limit
        try:
            solution = limit(expr, x, approach_point)
            # Handle infinities in the solution
            if solution == oo:
                solution_str = "∞"
                latex_solution = r"\infty"
            elif solution == -oo:
                solution_str = "-∞"
                latex_solution = r"-\infty"
            else:
                # Try to simplify the solution
                solution = simplify(solution)
                solution_str = str(solution)
                latex_solution = latex(solution)
        except Exception as e:
            # If sympy can't compute the limit
            solution_str = "Indeterminate or does not exist"
            latex_solution = r"\text{Indeterminate or does not exist}"
        
        # Create the problem statement
        problem_statement = f"Evaluate the limit: lim(x→{approach_str}) {expr}"
        
        # Create LaTeX representation
        latex_expression = f"\\lim_{{x \\to {latex(approach_point)}}} {latex(expr)}"
        
        return problem_statement, solution_str, latex_expression, latex_solution


    for _ in range(num_problems):

        if problem_type == "Integrals":
            degree = {
                "Easy": random.randint(1, 3),
                "Medium": random.randint(2, 4),
                "Hard": random.randint(3, 5)
            }[difficulty]

            bounds_present = difficulty != "Easy"
            integral = create_integral(generate_random_polynomial(degree), bounds_present)
            answer = integral.doit()

            latex_problem = rf"$$ {latex(integral)} $$"
            latex_solution = rf"$$ {latex(answer)} $$"

            problems.append(latex_problem)
            solutions.append(latex_solution)

        elif problem_type == "Limits":
            degree = {
                "Easy": random.randint(1, 3),
                "Medium": random.randint(2, 4),
                "Hard": random.randint(3, 5)
            }[difficulty]

            problem, solution, latex_expr, latex_sol = generate_random_limit_problem(difficulty)

            problems.append(problem)
            solutions.append(solution)
            
        elif problem_type == "Derivatives":
            if difficulty == "Easy":
                pass
            elif difficulty == "Medium":
                pass
            elif difficulty == "Hard":
                pass

        elif problem_type == "Polars":
            if difficulty == "Easy":
                pass
            elif difficulty == "Medium":
                pass
            elif difficulty == "Hard":
                pass

        elif problem_type == "Series":
            if difficulty == "Easy":
                pass
            elif difficulty == "Medium":
                pass
            elif difficulty == "Hard":
                pass

        else:
            pass
        

    return problems, solutions