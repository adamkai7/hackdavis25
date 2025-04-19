# geometry.py
import streamlit as st
import random
import math

def generate_geometry(concept, num_problems):
    """Generate geometry problems."""
    problems = []
    solutions = []
    
    shape = st.selectbox(
        "Choose shape type:",
        ["Triangles", "Circles", "Rectangles", "Mixed"],
        key=f"{concept}_shape"
    )
    
    for _ in range(num_problems):
        if shape == "Triangles" or (shape == "Mixed" and random.choice([True, False, False])):
            problem_type = random.choice(["area", "perimeter", "pythagorean"])
            if problem_type == "area":
                base = random.randint(5, 20)
                height = random.randint(5, 20)
                problems.append(f"Find the area of a triangle with base {base} and height {height}.")
                solutions.append(f"Area = {base * height / 2}")
            elif problem_type == "perimeter":
                a = random.randint(5, 15)
                b = random.randint(5, 15)
                c = random.randint(max(a, b) - min(a, b) + 1, a + b - 1)  # Triangle inequality
                problems.append(f"Find the perimeter of a triangle with sides {a}, {b}, and {c}.")
                solutions.append(f"Perimeter = {a + b + c}")
            else:  # pythagorean
                a = random.randint(3, 12)
                b = random.randint(4, 12)
                c = round(math.sqrt(a**2 + b**2), 2)
                problems.append(f"Find the hypotenuse of a right triangle with sides {a} and {b}.")
                solutions.append(f"Hypotenuse = {c}")
        
        elif shape == "Circles" or (shape == "Mixed" and random.choice([True, False])):
            problem_type = random.choice(["area", "circumference"])
            radius = random.randint(1, 15)
            if problem_type == "area":
                problems.append(f"Find the area of a circle with radius {radius}.")
                solutions.append(f"Area = {round(math.pi * radius**2, 2)}")
            else:
                problems.append(f"Find the circumference of a circle with radius {radius}.")
                solutions.append(f"Circumference = {round(2 * math.pi * radius, 2)}")
        
        elif shape == "Rectangles":
            problem_type = random.choice(["area", "perimeter", "diagonal"])
            length = random.randint(5, 20)
            width = random.randint(3, 15)
            if problem_type == "area":
                problems.append(f"Find the area of a rectangle with length {length} and width {width}.")
                solutions.append(f"Area = {length * width}")
            elif problem_type == "perimeter":
                problems.append(f"Find the perimeter of a rectangle with length {length} and width {width}.")
                solutions.append(f"Perimeter = {2 * (length + width)}")
            else:
                problems.append(f"Find the diagonal of a rectangle with length {length} and width {width}.")
                solutions.append(f"Diagonal = {round(math.sqrt(length**2 + width**2), 2)}")
    
    return problems, solutions