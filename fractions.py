import streamlit as st
import random
import math

def generate_fractions(concept, num_problems):
    """Generate fraction problems."""
    problems = []
    solutions = []
    
    operation = st.selectbox(
        "Choose operation:",
        ["Addition/Subtraction", "Multiplication/Division", "Simplification", "Mixed"],
        key=f"{concept}_operation"
    )
    
    max_denominator = st.number_input("Maximum denominator:", value=12, key=f"{concept}_max_denom")
    
    for _ in range(num_problems):
        a_num = random.randint(1, max_denominator)
        a_den = random.randint(a_num, max_denominator)
        b_num = random.randint(1, max_denominator)
        b_den = random.randint(b_num, max_denominator)
        
        # Ensure proper fractions
        if a_num > a_den:
            a_num, a_den = a_den, a_num
        if b_num > b_den:
            b_num, b_den = b_den, b_num
        
        if operation == "Addition/Subtraction" or (operation == "Mixed" and random.choice([True, False, False])):
            if random.choice([True, False]):
                problems.append(f"{a_num}/{a_den} + {b_num}/{b_den} = ?")
                # Calculate LCD
                lcm = (a_den * b_den) // math.gcd(a_den, b_den)
                result_num = (a_num * (lcm // a_den)) + (b_num * (lcm // b_den))
                result_den = lcm
                gcd = math.gcd(result_num, result_den)
                solutions.append(f"{result_num//gcd}/{result_den//gcd}")
            else:
                problems.append(f"{a_num}/{a_den} - {b_num}/{b_den} = ?")
                # Calculate LCD
                lcm = (a_den * b_den) // math.gcd(a_den, b_den)
                result_num = (a_num * (lcm // a_den)) - (b_num * (lcm // b_den))
                result_den = lcm
                if result_num == 0:
                    solutions.append("0")
                else:
                    gcd = math.gcd(abs(result_num), result_den)
                    solutions.append(f"{result_num//gcd}/{result_den//gcd}")
        
        elif operation == "Multiplication/Division" or (operation == "Mixed" and random.choice([True, False])):
            if random.choice([True, False]):
                problems.append(f"{a_num}/{a_den} × {b_num}/{b_den} = ?")
                result_num = a_num * b_num
                result_den = a_den * b_den
                gcd = math.gcd(result_num, result_den)
                solutions.append(f"{result_num//gcd}/{result_den//gcd}")
            else:
                problems.append(f"{a_num}/{a_den} ÷ {b_num}/{b_den} = ?")
                result_num = a_num * b_den
                result_den = a_den * b_num
                gcd = math.gcd(result_num, result_den)
                solutions.append(f"{result_num//gcd}/{result_den//gcd}")
        
        elif operation == "Simplification":
            # Create a fraction that can be simplified
            factor = random.randint(2, 5)
            num = random.randint(1, 10) * factor
            den = random.randint(1, 10) * factor
            problems.append(f"Simplify: {num}/{den}")
            gcd = math.gcd(num, den)
            solutions.append(f"{num//gcd}/{den//gcd}")
    
    return problems, solutions