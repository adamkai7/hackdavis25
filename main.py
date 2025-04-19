# main.py
import streamlit as st
import random
import math

# Import concept modules
from basic_arithmetic import generate_basic_arithmetic # type: ignore
from fractions2 import generate_fractions
from algebra import generate_algebra
from geometry import generate_geometry
from word_problems import generate_word_problems
from utils import create_download_buttons

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
    # Mapping between concept names and their functions
    concept_generators = {
        "Basic Arithmetic": generate_basic_arithmetic,
        "Fractions": generate_fractions,
        "Algebra": generate_algebra,
        "Geometry": generate_geometry,
        "Word Problems": generate_word_problems
    }
    
    st.write("## Problem Settings")
    num_problems = st.number_input("Number of problems to generate per concept:", 
                                   min_value=1, max_value=20, value=5)
    
    generate_button = st.button("Generate Problems")
    
    if generate_button:
        st.write("## Generated Problems")
        
        all_problems = {}
        all_solutions = {}
        
        for concept in selected_concepts:
            st.write(f"### {concept}")
            
            # Call the appropriate generator function for each concept
            problems, solutions = concept_generators[concept](concept, num_problems)
            
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
        
        # Create download buttons for problems and solutions
        create_download_buttons(all_problems, all_solutions)