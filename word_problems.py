# word_problems.py
import streamlit as st
import random

def generate_word_problems(concept, num_problems):
    """Generate word problems."""
    problems = []
    solutions = []
    
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