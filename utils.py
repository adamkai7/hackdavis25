# utils.py
import streamlit as st

def create_download_buttons(all_problems, all_solutions):
    """Create download buttons for problems and solutions."""
    # Format problems for download
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
    
    # Format solutions for download
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