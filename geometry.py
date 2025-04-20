# trigonometry.py
import streamlit as st
import random
import math
from sympy import symbols, sqrt, cos, sin, tan, pi
from sympy import latex
def generate_trigonometry(concept, num_problems):
    """Generate trigonometry problems."""
    problems = []
    solutions = []
    shape = st.selectbox(
        "Choose shape type:",
        ["Right Triangle", "Unit Circle", "Word Problem","Mixed"],
        key=f"{concept}_shape"
    )
    for _ in range(num_problems):
        if shape == "Right Triangle" or (shape == "Mixed" and random.choice([True, False, False])):
            problem_type = random.choice(["FindSin", "FindCos", "FindTan"])
            if problem_type == "FindSin":
                base = random.randint(5, 20)
                height = random.randint(5, 20)
                hypotenuse = math.sqrt(((base)**2)+((height)**2))
                if random.choice([True,False]):
                    oppos = base
                    adjac = height
                else:
                    oppos = height
                    adjac = base
                problems.append(f"Find the value of Sine with an adjacent side of length {adjac}, an opposite side of length {oppos}, and a hypotenuse of length {hypotenuse}.")
                solutions.append(f"Sine = {oppos/hypotenuse}")
            elif problem_type == "FindCos":
                base = random.randint(5, 20)
                height = random.randint(5, 20)
                hypotenuse = math.sqrt(((base)**2)+((height)**2))
                if random.choice([True,False]):
                    oppos = base
                    adjac = height
                else:
                    oppos = height
                    adjac = base
                problems.append(f"Find the value of Cosine with an adjacent side of length {adjac}, an opposite side of length {oppos}, and a hypotenuse of length {hypotenuse}.")
                solutions.append(f"Cosine = {adjac/hypotenuse}")
            else:  # Tangent
                base = random.randint(5, 20)
                height = random.randint(5, 20)
                hypotenuse = math.sqrt(((base)**2)+((height)**2))
                if random.choice([True,False]):
                    oppos = base
                    adjac = height
                else:
                    oppos = height
                    adjac = base
                problems.append(f"Find the value of Tangent with an adjacent side of length {adjac}, an opposite side of length {oppos}, and a hypotenuse of length {hypotenuse}.")
                solutions.append(f"Tangent = {oppos/adjac}")
        elif shape == "Unit Circle" or (shape == "Mixed" and random.choice([True, False])):
            problem_type = random.choice(["FindCos", "FindSin", "FindTan"])
            radians = [
                pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, 5*pi/6, pi,
                7*pi/6, 5*pi/4, 4*pi/3, 3*pi/2, 5*pi/3, 7*pi/4, 11*pi/6
            ]
            radian = random.choice(radians)
            # latex formatted version - display
            radian_str = latex(radian)
            # convert symbolic to float for calculation
            rad_val = float(radian.evalf())
            if problem_type == "FindCos":
                problems.append(f"Find the Cosine for the radian value {radian_str}. Round to the second decimal place.")
                solutions.append(f"Cosine = {round(math.cos(rad_val), 2)}")
            elif problem_type == "FindSin":
                problems.append(f"Find the Sine for the radian value {radian_str}. Round to the second decimal place.")
                solutions.append(f"Sine = {round(math.sin(rad_val), 2)}")
            else:  # Tangent
                problems.append(f"Find the Tangent for the radian value {radian_str}. Round to the second decimal place.")
                solutions.append(f"Tangent = {round(math.tan(rad_val), 2)}")
        elif shape == "Word Problem":
            problem_type = random.choice(["Sum and Difference Identities", "Reciprocal Identities", "Double Angle Identities","Half Angle Identities","Sum to Product Identities","Trigonometric Ratios","Periodic Identities"])
            trig1 = random.choice(["Sin","Cos","Tan"])
            trig2 = random.choice(["Sin","Cos"])
            plusorminus1 = random.choice(["+","-"])
            plusorminus2 = random.choice(["+","-"])
            if problem_type == "Sum and Difference Identities":
                problems.append(f"Find the equivalent of {trig1}(a{plusorminus1}b) according to Sum and Difference Identities")
                def get_sum_diff_identity(trig_func, operator):
                    if trig_func == "Sin":
                        return f"sin(a{operator}b) = sin(a)cos(b) {operator} cos(a)sin(b)"
                    elif trig_func == "Cos":
                        flipped = "+" if operator == "-" else "-"
                        return f"cos(a{operator}b) = cos(a)cos(b) {flipped} sin(a)sin(b)"
                    elif trig_func == "Tan":
                        flipped = "-" if operator == "+" else "+"
                        return f"tan(a{operator}b) = (tan(a) {operator} tan(b)) / (1 {flipped} tan(a)tan(b))"
                    else:
                        return "Unknown identity"
                identity = get_sum_diff_identity(trig1, plusorminus1)
                solutions.append(identity)
            elif problem_type == "Reciprocal Identities":
                problems.append(f"Find the equivalent of {trig1}(a) according to Reciprocal Identities")
                def get_reciprocal_identity(trig_func):
                    if trig_func == "Sin":
                        return "sin(a) = 1 / csc(a)"
                    elif trig_func == "Cos":
                        return "cos(a) = 1 / sec(a)"
                    elif trig_func == "Tan":
                        return "tan(a) = 1 / cot(a)"
                    else:
                        return "Unknown identity"
                identity = get_reciprocal_identity(trig1)
                solutions.append(identity)          
            elif problem_type == "Double Angle Identities":
                problems.append(f"Find the equivalent of {trig1}(2a) according to Double Angle Identities. There may be multiple correct forms.")
                def get_double_angle_identity(trig_func):
                    if trig_func == "Sin":
                        return ["sin(2a) = 2sin(a)cos(a)"]
                    elif trig_func == "Cos":
                        return [
                        "cos(2a) = cos²(a) - sin²(a)",
                        "cos(2a) = 2cos²(a) - 1",
                        "cos(2a) = 1 - 2sin²(a)"
                        ]
                    elif trig_func == "Tan":
                        return ["tan(2a) = (2tan(a)) / (1 - tan²(a))"]
                    else:
                        return ["Unknown identity"]
                identities = get_double_angle_identity(trig1)
                for identity in identities:
                    solutions.append(identity)
            elif problem_type == "Half Angle Identities":
                a = symbols("a")
                problems.append(f"Find the equivalent of {trig1}(a/2) according to Half Angle Identities")
                if trig1 == "Sin":
                    expr = sqrt((1 - cos(a)) / 2)
                elif trig1 == "Cos":
                    expr = sqrt((1 + cos(a)) / 2)
                elif trig1 == "Tan":
                    expr = sqrt((1 - cos(a)) / (1 + cos(a)))
                else:
                    expr = "Unknown identity"
                solutions.append(f"{trig1.lower()}(a/2) = ±{expr}")
            elif problem_type == "Sum to Product Identities":
                problems.append(f"Find the equivalent to {trig2}(a){plusorminus1}{trig2}(b) according to Sum to Product Identities")
                if trig2 == "Sin" and plusorminus1 == "-":
                    solutions.append(f"{trig2}(a){plusorminus1}{trig2}(b) = 2Sin((a-b)/2)*Cos((a+b)/2)")
                elif trig2 == "Sin" and plusorminus1 == "+":
                    solutions.append(f"{trig2}(a){plusorminus1}{trig2}(b) = 2Sin((a+b)/2)*Cos((a-b)/2)")
                elif trig2 == "Cos" and plusorminus1 == "-":
                    solutions.append(f"{trig2}(a){plusorminus1}{trig2}(b) = -2Sin((a+b)/2)*Sin((a-b)/2)")
                elif trig2 == "Cos" and plusorminus1 == "+":
                    solutions.append(f"{trig2}(a){plusorminus1}{trig2}(b) = 2Cos((a+b)/2)*Cos((a-b)/2)")
            elif problem_type == "Trigonometric Ratios":
                problems.append(f"What is the equivalent to {trig1} in terms of Opposite, Adjacent, and Hypotenuse?")
                if trig1 == "Sin":
                    solutions.append(f"Sin = Opposite/Hypotenuse")
                elif trig1 == "Cos":
                    solutions.append(f"Cos = Adjacent/Hypotenuse")
                elif trig1 == "Tan":
                    solutions.append(f"Tan = Opposite/Adjacent")
            else: #periodic identities
                twoOrpi = latex(random.choice([pi,2*pi]))
                problems.append(f"What is the equivalent to {trig1}(a+{twoOrpi})")
                if trig1 == "Sin":
                    solutions.append(f"Sin(a+2*pi) = Sin(a)")
                elif trig1 == "Cos":
                    solutions.append(f"Cos(a+2*pi) = Cos(a)")
                elif trig1 == "Tan":
                    solutions.append(f"Tan(a+pi) = Tan(a)")
    return problems, solutions
