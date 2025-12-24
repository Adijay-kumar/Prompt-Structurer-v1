import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Prompt Enhancer", layout="centered")
st.title("Prompt Enhancer")

# ---- Load roles ----
try:
    roles_resp = requests.get(f"{BASE_URL}/roles")
    roles_resp.raise_for_status()
    roles = roles_resp.json()["roles"]
except Exception as e:
    st.error("Backend not running or /roles failed")
    st.stop()

# ---- UI ----
selected_role = st.selectbox("Select Role", roles)

task = st.text_area(
    "Enter your task / raw prompt",
    height=150,
    placeholder="Build a blockchain contract that stores messages"
)

instruction_keys = st.multiselect(
    "Instruction Tags",
    ["professional", "concise", "step_by_step"]
)

output_keys = st.multiselect(
    "Output Format Tags",
    ["code_first", "explanation", "numbered_steps"]
)

# ---- Submit ----
if st.button("Enhance Prompt"):
    if not task.strip():
        st.warning("Please enter a task")
    else:
        payload = {
            "task": task,
            "instruction_keys": instruction_keys,
            "output_keys": output_keys
        }

        with st.spinner("Enhancing prompt..."):
            resp = requests.post(f"{BASE_URL}/enhance", json=payload)

        if resp.status_code == 200:
            polished = resp.json()["polished_prompt"]
            st.subheader("Polished Prompt")
            st.markdown(polished)
        else:
            st.error(f"Error {resp.status_code}: {resp.text}")
