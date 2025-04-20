# basic_arithmetic.py
import streamlit as st
import random

def generate_basic_arithmetic(concept, num_problems):
    """Generate basic arithmetic problems."""
    problems = []
    solutions = []
    
    operation = st.selectbox(
        "Choose operation:",
        ["Addition", "Subtraction", "Multiplication", "Division", "Mixed"],
        key=f"{concept}_operation"
    )
    
    min_val = st.number_input("Minimum value:", value=1, key=f"{concept}_min")
    max_val = st.number_input("Maximum value:", value=100, key=f"{concept}_max")
    
    for _ in range(num_problems):
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        
        if operation == "Addition" or (operation == "Mixed" and random.choice([True, False, False, False])):
            problems.append(f"{a} + {b} = ?")
            solutions.append(a + b)
        elif operation == "Subtraction" or (operation == "Mixed" and random.choice([True, False, False])):
            # Ensure a >= b for easier subtraction
            if a < b:
                a, b = b, a
            problems.append(f"{a} - {b} = ?")
            solutions.append(a - b)
        elif operation == "Multiplication" or (operation == "Mixed" and random.choice([True, False])):
            problems.append(f"{a} × {b} = ?")
            solutions.append(a * b)
        elif operation == "Division":
            # Create division problems with whole number answers
            product = a * b
            problems.append(f"{product} ÷ {b} = ?")
            solutions.append(a)
    
    return problems, solutions