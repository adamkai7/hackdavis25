# algebra.py
import streamlit as st
import random

def generate_algebra(concept, num_problems):
    """Generate algebra problems."""
    problems = []
    solutions = []
    
    problem_type = st.selectbox(
        "Choose problem type:",
        ["Solve for x (Linear)", "Evaluate Expression", "Factoring", "Systems of Equations"],
        key=f"{concept}_type"
    )
    
    difficulty = st.select_slider(
        "Difficulty level:",
        options=["Easy", "Medium", "Hard"],
        value="Medium",
        key=f"{concept}_difficulty"
    )
    
    for _ in range(num_problems):
        if problem_type == "Solve for x (Linear)":
            if difficulty == "Easy":
                a = random.randint(1, 10)
                b = random.randint(1, 20)
                answer = b / a
                problems.append(f"{a}x = {b}")
                solutions.append(f"x = {answer}")
            elif difficulty == "Medium":
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 20)
                answer = (c - b) / a
                problems.append(f"{a}x + {b} = {c}")
                solutions.append(f"x = {answer}")
            else:  # Hard
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                d = random.randint(1, 20)
                answer = (d - b) / (a - c) if a != c else "No solution"
                problems.append(f"{a}x + {b} = {c}x + {d}")
                solutions.append(f"x = {answer}")
        
        elif problem_type == "Evaluate Expression":
            x = random.randint(-10, 10)
            if difficulty == "Easy":
                a = random.randint(1, 5)
                b = random.randint(1, 10)
                expr = f"{a}x + {b}"
                result = a * x + b
            elif difficulty == "Medium":
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                c = random.randint(1, 10)
                expr = f"{a}x² + {b}x + {c}"
                result = a * (x ** 2) + b * x + c
            else:  # Hard
                a = random.randint(1, 3)
                b = random.randint(1, 5)
                c = random.randint(1, 5)
                d = random.randint(1, 10)
                expr = f"{a}x³ + {b}x² + {c}x + {d}"
                result = a * (x ** 3) + b * (x ** 2) + c * x + d
            
            problems.append(f"Evaluate {expr} when x = {x}")
            solutions.append(result)
        
        elif problem_type == "Factoring":
            if difficulty == "Easy":
                a = random.randint(1, 5)
                b = random.randint(1, 10)
                problems.append(f"Factor: {a}x + {b}")
                solutions.append(f"{a}x + {b} (already in factored form)")
            elif difficulty == "Medium":
                a = random.randint(1, 5)
                b = random.randint(-10, 10)
                c = random.randint(-10, 10)
                problems.append(f"Factor: {a}x² + {b}x + {c}")
                solutions.append(f"See solution (quadratic factoring)")
            else:  # Hard
                a = random.randint(1, 3)
                b = random.randint(-5, 5)
                c = random.randint(-5, 5)
                d = random.randint(-10, 10)
                problems.append(f"Factor: {a}x³ + {b}x² + {c}x + {d}")
                solutions.append(f"See solution (cubic factoring)")
                
        elif problem_type == "Systems of Equations":
            if difficulty == "Easy":
                a1 = random.randint(1, 5)
                b1 = random.randint(1, 10)
                a2 = random.randint(1, 5)
                b2 = random.randint(1, 10)
                x = random.randint(-5, 5)
                y = random.randint(-5, 5)
                c1 = a1*x + b1*y
                c2 = a2*x + b2*y
                problems.append(f"Solve the system:\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}")
                solutions.append(f"x = {x}, y = {y}")
            else:
                # More complex systems for medium/hard
                a1 = random.randint(1, 5)
                b1 = random.randint(1, 5)
                c1 = random.randint(1, 10)
                a2 = random.randint(1, 5)
                b2 = random.randint(1, 5)
                c2 = random.randint(1, 10)
                problems.append(f"Solve the system:\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}")
                # Calculate solution using Cramer's rule
                det = a1*b2 - a2*b1
                if det == 0:
                    solutions.append("No unique solution")
                else:
                    x = (c1*b2 - c2*b1)/det
                    y = (a1*c2 - a2*c1)/det
                    solutions.append(f"x = {round(x, 2)}, y = {round(y, 2)}")
    
    return problems, solutions