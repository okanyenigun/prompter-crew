import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import streamlit as st
from src.prompter.main import run


def main():
    st.title("Prompt Engineer")

    user_input = st.text_input("Enter the initial promt:")

    if st.button("Run"):
        st.empty()
        with st.spinner("Agents are running..."):
            results = run({"prompt": user_input})
            results = results.to_dict()["prompts"]
        
        for result in results:
            st.subheader(result["framework"])
            st.write(result["prompt"])

if __name__ == "__main__":
    main()