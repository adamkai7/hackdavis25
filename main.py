import streamlit as st
import random
import math
from calculus import generate_calculus

st.title("Number Ninja")
st.write("Generate custom math problems based on your preferences!")

# Sidebar for concept selection
st.sidebar.header("Select Math Concepts")
selected_concepts = st.sidebar.multiselect(
    "Choose concepts you want to practice:",
    ["Calculus"],
    default=["Calculus"]
)

if not selected_concepts:
    st.info("Please select at least one math concept from the sidebar to generate problems.")
else:
    concept_generators = {"Calculus": generate_calculus}
    st.write("## Problem Settings")

    # Use session state to persist values
    if "num_problems" not in st.session_state:
        st.session_state.num_problems = 5

    st.session_state.num_problems = st.number_input(
        "Number of problems to generate per concept:",
        min_value=1, max_value=20, value=st.session_state.num_problems,
        key="num_problems_input"
    )

    # Force a re-generation if options change
    if "regen_key" not in st.session_state:
        st.session_state.regen_key = 0

    def trigger_regeneration():
        st.session_state.regen_key += 1

    all_problems = {}
    all_solutions = {}

    for concept in selected_concepts:
        st.write(f"### {concept}")

        problems, solutions = concept_generators[concept](
            concept, st.session_state.num_problems
        )

        all_problems[concept] = problems
        all_solutions[concept] = solutions

        for i, (problem, solution) in enumerate(zip(problems, solutions)):
            st.write(f"**Problem {i+1}:** {problem}")

    with st.expander("View Solutions"):
        for concept in selected_concepts:
            st.write(f"### {concept} Solutions")
            for i, solution in enumerate(all_solutions[concept]):
                st.write(f"**Problem {i+1}:** {solution}")
