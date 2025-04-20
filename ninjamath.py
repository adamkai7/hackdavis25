from sympy import symbols
from sympy import symbols, Eq, solve, diff, integrate, sin, cos, expand, simplify, factor, limit, oo, Matrix, Derivative, Integral
import streamlit as st
from numpy import *
import random

num_prpblems = st.slider("Number of problems to generate per concept:", 0, 20)