import streamlit as st
import ttg
import random

def generate_truth_table(difficulty, num_problems):
    problems = []
    solutions = []
    
    # Define available variables and operators based on difficulty
    variables = ['p', 'q']
    operators = ['and', 'or', 'not', 'xor', 'nand', 'nor']
    
    if difficulty == "medium":
        variables.append('r')
    elif difficulty == "hard":
        variables.append('r')
        variables.append('s')
    
    for _ in range(num_problems):
        if difficulty == "easy":
            # One operation between two variables
            var1 = random.choice(variables[:2])
            var2 = random.choice(variables[:2])
            op = random.choice(operators)
            
            # Ensure we don't have something like "p not p"
            if op == 'not':
                expr = f"{op} {var1}"
            else:
                expr = f"{var1} {op} {var2}"
                
        elif difficulty == "medium":
            # Three operations with possible three variables
            ops_needed = 3
            expr_parts = [random.choice(variables)]
            
            for _ in range(ops_needed):
                op = random.choice(operators)
                if op == 'not':
                    expr_parts.insert(0, op)
                else:
                    expr_parts.extend([op, random.choice(variables)])
            
            expr = ' '.join(expr_parts)
            
        else:  # hard
            # Five operations with possible four variables
            ops_needed = 5
            expr_parts = [random.choice(variables)]
            
            for _ in range(ops_needed):
                op = random.choice(operators)
                if op == 'not':
                    expr_parts.insert(0, op)
                else:
                    expr_parts.extend([op, random.choice(variables)])
            
            expr = ' '.join(expr_parts)
        
        # Generate truth table
        try:
            table = ttg.Truths(variables, [expr])
            problems.append(f"Generate truth table for: {expr}")
            solutions.append(table)
        except:
            # If the random generation creates an invalid expression, try again
            return generate_truth_table(difficulty, num_problems)
    
    return problems, solutions

def generate_truthtable(concept, num_problems):
    st.write("### Truth Table Problems")
    
    difficulty = st.radio(
        "Select difficulty level:",
        ["easy", "medium", "hard"],
        key="tt_difficulty"
    )
    
    problems, solutions = generate_truth_table(difficulty, num_problems)
    
    for i, problem in enumerate(problems):
        st.write(f"**Problem {i+1}:** {problem}")
        
        with st.expander(f"Show solution for Problem {i+1}"):
            st.write(solutions[i])
    
    return problems, solutions