# calculus.py
# It's over
from sympy import symbols
from sympy import symbols, Eq, solve, diff, integrate, sin, cos, expand, simplify, factor, limit, oo, Matrix, Derivative, Integral
import streamlit as st
from numpy import *
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
            if difficulty == "Easy":
                pass
            elif difficulty == "Medium":
                pass
            elif difficulty == "Hard":
                pass

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