import streamlit as st
import random
import math

st.set_page_config(page_title="Math Problem Generator", layout="wide")

st.title("Math Problem Generator")
st.write("Generate custom math problems based on your preferences")

# Sidebar for concept selection
st.sidebar.header("Select Math Concepts")
selected_concepts = st.sidebar.multiselect(
    "Choose concepts you want to practice:",
    ["Basic Arithmetic", "Fractions", "Algebra", "Geometry", "Word Problems"],
    default=["Basic Arithmetic"]
)

# Main content area
if not selected_concepts:
    st.info("Please select at least one math concept from the sidebar to generate problems.")
else:
    # Function to generate problems based on concept
    def generate_problems(concept, num_problems):
        problems = []
        solutions = []
        
        if concept == "Basic Arithmetic":
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
        
        elif concept == "Fractions":
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
        
        elif concept == "Algebra":
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
                        # This is a simplification as proper factoring would require checking if it's factorable
                        solutions.append(f"See solution (quadratic factoring)")
                    else:  # Hard
                        a = random.randint(1, 3)
                        b = random.randint(-5, 5)
                        c = random.randint(-5, 5)
                        d = random.randint(-10, 10)
                        problems.append(f"Factor: {a}x³ + {b}x² + {c}x + {d}")
                        solutions.append(f"See solution (cubic factoring)")
        
        elif concept == "Geometry":
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
        
        elif concept == "Word Problems":
            problem_type = st.selectbox(
                "Choose problem type:",
                ["Age Problems", "Motion Problems", "Mixture Problems", "Work Problems", "Mixed"],
                key=f"{concept}_type"
            )
            
            for _ in range(num_problems):
                if problem_type == "Age Problems" or (problem_type == "Mixed" and random.choice([True, False, False, False])):
                    current_age = random.randint(20, 60)
                    child_age = random.randint(5, 18)
                    years = random.randint(1, 10)
                    problems.append(f"A parent is {current_age} years old and their child is {child_age} years old. In how many years will the parent's age be {random.randint(2, 4)} times the child's age?")
                    # Solution would be calculated based on algebra: P + x = n(C + x)
                    solutions.append("See solution (requires algebra)")
                
                elif problem_type == "Motion Problems" or (problem_type == "Mixed" and random.choice([True, False, False])):
                    speed1 = random.randint(40, 80)
                    speed2 = random.randint(30, 70)
                    distance = random.randint(100, 500)
                    problems.append(f"Two cars start from the same point and travel in opposite directions. Car A travels at {speed1} mph and Car B travels at {speed2} mph. How long will it take for them to be {distance} miles apart?")
                    time = distance / (speed1 + speed2)
                    solutions.append(f"Time = {round(time, 2)} hours")
                
                elif problem_type == "Mixture Problems" or (problem_type == "Mixed" and random.choice([True, False])):
                    conc1 = random.randint(5, 40)
                    conc2 = random.randint(conc1 + 10, 80)
                    target_conc = random.randint(conc1 + 5, conc2 - 5)
                    amt2 = random.randint(10, 50)
                    problems.append(f"A solution contains {conc1}% acid. How many liters of a {conc2}% acid solution should be added to {amt2} liters of the {conc1}% solution to create a {target_conc}% acid solution?")
                    # Solution would be calculated using mixture formula
                    solutions.append("See solution (requires algebra)")
                
                elif problem_type == "Work Problems":
                    time1 = random.randint(2, 10)
                    time2 = random.randint(3, 12)
                    problems.append(f"Person A can complete a job in {time1} hours. Person B can complete the same job in {time2} hours. How long would it take if they worked together?")
                    combined_rate = 1/time1 + 1/time2
                    combined_time = 1 / combined_rate
                    solutions.append(f"Time = {round(combined_time, 2)} hours")
        
        return problems, solutions

    # Generate problems for each selected concept
    st.write("## Problem Settings")
    
    num_problems = st.number_input("Number of problems to generate per concept:", min_value=1, max_value=20, value=5)
    
    generate_button = st.button("Generate Problems")
    
    if generate_button:
        st.write("## Generated Problems")
        
        all_problems = {}
        all_solutions = {}
        
        for concept in selected_concepts:
            st.write(f"### {concept}")
            problems, solutions = generate_problems(concept, num_problems)
            all_problems[concept] = problems
            all_solutions[concept] = solutions
            
            for i, (problem, solution) in enumerate(zip(problems, solutions)):
                st.write(f"**Problem {i+1}:** {problem}")
        
        # Show solutions in a collapsible section
        with st.expander("View Solutions"):
            for concept in selected_concepts:
                st.write(f"### {concept} Solutions")
                for i, solution in enumerate(all_solutions[concept]):
                    st.write(f"**Problem {i+1}:** {solution}")
        
        # Option to download problems as text
        problem_text = ""
        for concept in all_problems:
            problem_text += f"{concept}\n"
            problem_text += "-" * len(concept) + "\n\n"
            for i, problem in enumerate(all_problems[concept]):
                problem_text += f"Problem {i+1}: {problem}\n\n"
            problem_text += "\n"
        
        st.download_button(
            label="Download Problems",
            data=problem_text,
            file_name="math_problems.txt",
            mime="text/plain"
        )
        
        # Option to download solutions as text
        solution_text = ""
        for concept in all_solutions:
            solution_text += f"{concept} Solutions\n"
            solution_text += "-" * (len(concept) + 10) + "\n\n"
            for i, solution in enumerate(all_solutions[concept]):
                solution_text += f"Problem {i+1}: {solution}\n\n"
            solution_text += "\n"
        
        st.download_button(
            label="Download Solutions",
            data=solution_text,
            file_name="math_solutions.txt",
            mime="text/plain"
        )