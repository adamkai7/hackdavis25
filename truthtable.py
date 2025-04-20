'''
Hack Davis truth table code 
'''
import streamlit as st
import random
import ttg

# Converts expression keywords to plain English
def expression_to_english(expr: str) -> str:
    replacements = {
        "not ": "not ",
        " and ": "and",
        " or ": "or",
        "logical disjunction": "or",
        "logical conjunction": "and",
        "logical biconditional": "if and only if",
        "exclusive disjunction": "xor",
        "material implication": "if...then",
        "logical nor": "nor",
        "logical NAND": "nand",
        "negation": "not",
    }
    for key, value in replacements.items():
        expr = expr.replace(key, value)
    return expr

# App header and symbols reference
st.header("Discrete Math Questions")

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

st.subheader("Logic Symbols and Their Meanings")
for expr, (natural_name, technical_name) in symbols.items():
    st.latex(f"{expr} \\quad \\text{{= {natural_name} ({technical_name})}}")

# Generate logical expressions and their truth tables
def generate_truthtables(difficulty: str, num_problems: int):
    problems = []
    solutions = []

    logical_operators = [
        'and', 'or', 'nand', 'nor',
        'xor', 'if...then', 'if and only if'
    ]
    unary_operator = 'not'
    variables = ['p', 'q', 'r']

    op_range = {
        "Easy": (1,1),
        "Medium": (1, 2),
        "Hard": (3, 4)
    }

    min_ops, max_ops = op_range[difficulty]

    for _ in range(num_problems):
        num_ops = random.randint(min_ops, max_ops)
        used_vars = random.sample(variables, k=min(3, len(variables)))
        expr_parts = []

        for _ in range(num_ops):
            op = random.choice(logical_operators + [unary_operator])
            if op == unary_operator:
                var = random.choice(used_vars)
                expr_parts.append(f"not {var}")
            else:
                var1 = random.choice(used_vars)
                var2 = random.choice(used_vars)
                while var1 == var2:
                    var2 = random.choice(used_vars)
                expr_parts.append(f"({var1} {op} {var2})")

        final_expr = " and ".join(expr_parts)

        try:
            table = ttg.Truths(used_vars, [final_expr])
            problems.append(final_expr)
            solutions.append(table)
        except Exception:
            continue  # skip invalid expressions

    return problems, solutions

# Streamlit input controls
difficulty = st.selectbox("Choose difficulty:", ["Easy", "Medium", "Hard"])
n = st.slider("How many logic problems do you want?", 1, 10, 3)

if st.button("Generate Logic Problems"):
    problems, solutions = generate_truthtables(difficulty, n)

    st.subheader("Generated Logical Expressions")
    for i, problem in enumerate(problems):
        st.markdown(f"**Problem {i+1}:** `{problem}`")

    st.subheader("Truth Tables")
    with st.expander("Show Truth Table Solutions"):
        for i, solution in enumerate(solutions):
            st.markdown(f"**Solution to Problem {i+1}**")
            st.dataframe(solution.as_pandas())
