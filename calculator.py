import streamlit as st

# Page Configuration
st.set_page_config(page_title="Calculator",layout="centered")

# 1. Memory Initialization
if "math_equation" not in st.session_state:
    st.session_state.math_equation = ""

# 2. Simple Functions (Handle Button Click Events)
def add_to_calc(value):
    st.session_state.math_equation += str(value)

def calculate_result():
    try:
        # Use Python's eval to calculate string expression
        # Replace display symbols (if any) with math symbols
        expr = st.session_state.math_equation.replace('÷', '/').replace('×', '*')
        if expr.strip() == "":
            return
        result = eval(expr)
        # Format: Remove .0 for integers
        st.session_state.math_equation = str(int(result) if result == int(result) else round(result, 4))
    except:
        st.session_state.math_equation = "Error"

def clear_calc():
    st.session_state.math_equation = ""

def del_last():
    st.session_state.math_equation = st.session_state.math_equation[:-1]


# 3. UI Design (Modern & Responsive)
st.title("Calculator")

# Display (Keyboard and Button Synchronized)
st.text_input(
    label="Calculator Display",
    label_visibility="collapsed",
    key="math_equation",
    on_change=calculate_result,
    placeholder="0"
)

st.write("---")

# 4. Buttons Grid (Refined 4-column layout)
# Row 1
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("AC", on_click=clear_calc, use_container_width=True)
with c2: st.button("Del", on_click=del_last, use_container_width=True)
with c3: st.button("%", on_click=add_to_calc, args=("/100",), use_container_width=True)
with c4: st.button("➗", on_click=add_to_calc, args=("÷",), use_container_width=True)

# Row 2
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("7", on_click=add_to_calc, args=("7",), use_container_width=True)
with c2: st.button("8", on_click=add_to_calc, args=("8",), use_container_width=True)
with c3: st.button("9", on_click=add_to_calc, args=("9",), use_container_width=True)
with c4: st.button("✖", on_click=add_to_calc, args=("×",), use_container_width=True)

# Row 3
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("4", on_click=add_to_calc, args=("4",), use_container_width=True)
with c2: st.button("5", on_click=add_to_calc, args=("5",), use_container_width=True)
with c3: st.button("6", on_click=add_to_calc, args=("6",), use_container_width=True)
with c4: st.button("--", on_click=add_to_calc, args=("-",), use_container_width=True)

# Row 4
c1, c2, c3, c4 = st.columns(4)
with c1: st.button("1", on_click=add_to_calc, args=("1",), use_container_width=True)
with c2: st.button("2", on_click=add_to_calc, args=("2",), use_container_width=True)
with c3: st.button("3", on_click=add_to_calc, args=("3",), use_container_width=True)
with c4: st.button("➕", on_click=add_to_calc, args=("+",), use_container_width=True)

# Row 5
c1, c2, c3 = st.columns([1, 1, 2])
with c1: st.button("0", on_click=add_to_calc, args=("0",), use_container_width=True)
with c2: st.button(".", on_click=add_to_calc, args=(".",), use_container_width=True)
with c3: st.button("=", on_click=calculate_result, use_container_width=True, type="primary")
