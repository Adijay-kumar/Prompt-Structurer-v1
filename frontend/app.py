import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Prompt Enhancer (Ollama)",
    layout="centered"
)

st.title("Prompt Enhancer")

# ---------- Input ----------
task = st.text_area(
    "Enter your prompt",
    height=180,
    placeholder="Develop a blockchain smart contract for stock trading"
)

# ---------- Action ----------
if st.button("Enhance Prompt", type="primary"):
    if not task.strip():
        st.warning("Please enter a prompt.")
    else:
        payload = {
            "task": task
        }

        with st.spinner("Enhancing prompt..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/enhance",
                    json=payload,
                    timeout=360
                )
                response.raise_for_status()
            except Exception as e:
                st.error(f"Request failed: {e}")
                st.stop()

        polished_prompt = response.json().get("polished_prompt", "")

        if not polished_prompt.strip():
            st.warning("No enhanced prompt returned.")
        else:
            st.subheader("Enhanced Prompt")
            st.markdown(polished_prompt)

