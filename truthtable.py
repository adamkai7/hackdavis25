import streamlit as st
from streamlit import dataframe
import random
import ttg

# Supported logical operators
logical_operators = [
    'and', 'or', 'nand', 'nor',
    'xor', 'if...then', 'if and only if'
]
unary_operator = 'not'
variables = ['p', 'q', 'r']

# Converts user-friendly expression to ttg-compatible logic
def make_expression(op: str, var1: str, var2: str) -> str:
    if op == 'and':
        return f"({var1} and {var2})"
    elif op == 'or':
        return f"({var1} or {var2})"
    elif op == 'xor':
        return f"({var1} != {var2})"
    elif op == 'nand':
        return f"not ({var1} and {var2})"
    elif op == 'nor':
        return f"not ({var1} or {var2})"
    elif op == 'if...then':
        return f"(not {var1} or {var2})"
    elif op == 'if and only if':
        return f"({var1} == {var2})"
    else:
        return f"({var1} {op} {var2})"  # fallback

# App Header
st.header("🔢 HackDavis Logic Problem Generator")

# Symbol reference
symbols = {
    '¬p': ('not', 'negation'),
    'p ∨ q': ('or', 'logical disjunction'),
    'p ↓ q': ('nor', 'logical nor'),
    'p ⊕ q': ('xor', 'exclusive disjunction'),
    'p ∧ q': ('and', 'logical conjunction'),
    'p | q': ('nand', 'logical NAND'),
    'p → q': ('if...then', 'material implication'),
    'p ↔ q': ('if and only if', 'logical biconditional')
}

st.subheader("🧠 Logic Symbols and Their Meanings")
for expr, (natural_name, technical_name) in symbols.items():
    st.latex(f"{expr} \\quad \\text{{= {natural_name} ({technical_name})}}")

# Problem generation function
def generate_truthtables(difficulty: str, num_problems: int):
    problems = []         # Friendly display
    logic_expressions = []  # ttg-compatible expressions
    solutions = []

    op_range = {
        "Easy": (1, 1),
        "Medium": (1, 2),
        "Hard": (3, 4)
    }

    min_ops, max_ops = op_range[difficulty]

    for _ in range(num_problems):
        num_ops = random.randint(min_ops, max_ops)
        used_vars = random.sample(variables, k=min(3, len(variables)))
        expr_display_parts = []
        expr_logic_parts = []

        for _ in range(num_ops):
            op = random.choice(logical_operators + [unary_operator])
            if op == unary_operator:
                var = random.choice(used_vars)
                expr_display_parts.append(f"not {var}")
                expr_logic_parts.append(f"(not {var})")
            else:
                var1 = random.choice(used_vars)
                var2 = random.choice(used_vars)
                while var1 == var2:
                    var2 = random.choice(used_vars)

                expr_display_parts.append(f"({var1} {op} {var2})")
                expr_logic_parts.append(make_expression(op, var1, var2))

        final_display_expr = " and ".join(expr_display_parts)
        final_logic_expr = " and ".join(expr_logic_parts)

        try:
            table = ttg.Truths(used_vars, [final_logic_expr])
            problems.append(final_display_expr)
            logic_expressions.append(final_logic_expr)
            solutions.append(table)
        except Exception as e:
            print("Skipping invalid expression:", final_logic_expr, "Error:", e)
            continue

    return problems, solutions

# Streamlit UI
difficulty = st.selectbox("Choose difficulty:", ["Easy", "Medium", "Hard"])
n = st.slider("How many logic problems do you want?", 1, 10, 3)

if st.button("Generate Logic Problems"):
    problems, solutions = generate_truthtables(difficulty, n)

    st.subheader("🧩 Generated Logical Expressions")
    for i, problem in enumerate(problems):
        st.markdown(f"**Problem {i+1}:** `{problem}`")

    st.subheader("📊 Truth Table Solutions")
    with st.expander("Show Truth Table Solutions"):
        for i, (problem, solution) in enumerate(zip(problems, solutions)):
            st.markdown(f"**Solution to Problem {i+1}:** `{problem}`")
            st.dataframe(solution.as_pandas)

