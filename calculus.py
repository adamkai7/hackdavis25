import google.generativeai as genai
from sympy import symbols, sin, cos, tan, log, exp, sqrt, Abs, Integral, limit, simplify, oo, pi, S, latex
import streamlit as st
import random
import re

# Configure Gemini API
genai.configure(api_key="AIzaSyCxF9mvssggNGMR_mxZS-KaYkaeKmEbYHI")

def modify_numbers_in_problem(problem_text):
    """Randomly modify numbers in the problem text to create variation"""
    numbers = re.findall(r'\d+\.?\d*', problem_text)
    for num in numbers:
        original = float(num)
        modified = original * random.uniform(0.5, 1.5)
        if abs(modified - original) < 1:
            modified = original + random.choice([-1, 1]) * random.randint(1, 3)
        if '.' in num:
            modified_str = f"{modified:.2f}".rstrip('0').rstrip('.') if '.' in f"{modified:.2f}" else f"{modified:.0f}"
        else:
            modified_str = str(int(round(modified)))
        problem_text = problem_text.replace(num, modified_str, 1)
    return problem_text

def generate_random_polynomial(degree=3, coef_range=(-5, 5)):
    x = symbols('x')
    return sum(random.randint(*coef_range) * x**i for i in range(degree + 1))

def create_integral(poly_expr, definite=False):
    x = symbols('x')
    if definite:
        a, b = sorted(random.sample(range(-10, 11), 2))
        return Integral(poly_expr, (x, a, b))
    return Integral(poly_expr, x)

def generate_easy_expression(x, approach_point):
    expression_type = random.randint(1, 5)
    if expression_type == 1:
        degree = random.randint(1, 3)
        coeffs = [random.randint(-5, 5) for _ in range(degree + 1)]
        return sum(coeff * x**i for i, coeff in enumerate(coeffs))
    elif expression_type == 2:
        num_degree = random.randint(0, 2)
        den_degree = random.randint(0, 2)
        num_coeffs = [random.randint(-5, 5) for _ in range(num_degree + 1)]
        den_coeffs = [random.randint(-5, 5) for _ in range(den_degree + 1)]
        while den_coeffs[-1] == 0:
            den_coeffs[-1] = random.randint(-5, 5)
        return sum(coeff * x**i for i, coeff in enumerate(num_coeffs)) / sum(coeff * x**i for i, coeff in enumerate(den_coeffs))
    elif expression_type == 3:
        return random.choice([sin(x), cos(x), tan(x)])
    elif expression_type == 4:
        return exp(x) if approach_point == 0 else random.choice([exp(x), log(x)])
    else:
        degree = random.randint(1, 2)
        coeffs = [random.randint(-3, 3) for _ in range(degree + 1)]
        return sum(coeff * x**i for i, coeff in enumerate(coeffs)) + random.choice([sin(x), cos(x)])

def generate_random_limit_problem(difficulty="Medium"):
    x = symbols('x')
    approach_options = {
        "Easy": [0, 1, 2, -1, -2, oo, -oo],
        "Medium": [0, 1, 2, -1, -2, oo, -oo, S.Half, -S.Half],
        "Hard": [0, 1, 2, -1, -2, oo, -oo, S.Half, -S.Half, pi]
    }
    approach_point = random.choice(approach_options[difficulty])
    
    if difficulty == "Easy":
        expr = generate_easy_expression(x, approach_point)
    elif difficulty == "Medium":
        expr = generate_easy_expression(x, approach_point)
    else:
        expr = generate_easy_expression(x, approach_point)
    
    approach_str = "∞" if approach_point == oo else "-∞" if approach_point == -oo else "π" if approach_point == pi else str(approach_point)
    
    try:
        solution = limit(expr, x, approach_point)
        solution_str = "∞" if solution == oo else "-∞" if solution == -oo else str(simplify(solution))
        latex_solution = r"\infty" if solution == oo else r"-\infty" if solution == -oo else latex(solution)
    except:
        solution_str = "Indeterminate or does not exist"
        latex_solution = r"\text{Indeterminate or does not exist}"
    
    problem_statement = f"Evaluate the limit: lim(x→{approach_str}) {expr}"
    latex_expression = f"\\lim_{{x \\to {latex(approach_point)}}} {latex(expr)}"
    return problem_statement, solution_str, latex_expression, latex_solution

def generate_calculus(concept, num_problems):
    problems = []
    solutions = []
    word_problems = []

    # Selecting problem type and difficulty level
    problem_type = st.selectbox(
        "Choose problem type:",
        ["Integrals", "Limits", "Derivatives", "Polars", "Series"],
        key=f"{concept}_problem_type"
    )

    category = st.selectbox(
        "Category Level",
        options=[
            "Application of Integrals", "Fundamental Theorem of Calculus", "Related Rates", 
            "Improper Integrals", "Area and Volume", "Particle Motion", 
            "Derivative at a Point", "Differential Equations",
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

    # First generate all mathematical problems
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
            problem, solution, latex_expr, latex_sol = generate_random_limit_problem(difficulty)
            problems.append(f"$$ {latex_expr} $$")
            solutions.append(f"$$ {latex_sol} $$")

    # Display mathematical problems (with solutions in dropdown)
    st.subheader("Mathematical Problems")
    for i, problem in enumerate(problems):
        st.markdown(f"**Problem {i+1}:**")
        st.write(problem)
        
        # Display solutions in a dropdown
        with st.expander(f"Solution {i+1}"):
            st.write(solutions[i])

    # Generate word problems based on math problems
    st.subheader("Word Problem Variations")
    for i, problem in enumerate(problems):
        prompt = f"""
        Create a real-world word problem (50-75 words) that would require solving this mathematical problem:
        {problem}
        Requirements:
        1. Keep the same problem type (e.g., integral/limit) but change all numbers
        2. Use a realistic scenario that applies this mathematics
        3. Modify any bounds/limits appropriately
        4. Make the context completely different from the original
        5. Output only the word problem text (no mathematical formula).
        """
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        word_problem = modify_numbers_in_problem(response.text)
        word_problems.append(word_problem)

    # Display word problems without any math formulas
    for i, word_problem in enumerate(word_problems):
        st.markdown(f"**Word Problem {i+1}:**")
        st.write(word_problem)

    return problems, solutions, word_problems