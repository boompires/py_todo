import streamlit as st
import funcs

# To run app use: streamlit run web.py

todos = funcs.get_todos()

st.title("My Todo App")
# st.subheader("This is my todo app!")
st.write("Select a todo when completed to remove it from the list.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...")
