import streamlit as st
import plotly.graph_objects as go
import os
from engine import IntentInverter
from automation import MimeticController

st.set_page_config(page_title="Ghost Persona UI", page_icon="👻")

if "logs" not in st.session_state: st.session_state.logs = []
def log(msg): st.session_state.logs.append(msg)

st.title("👻 Ghost Persona: Adversarial Shield")

with st.sidebar:
    st.header("Control Panel")
    api_key = st.text_input("Gemini API Key", type="password")
    if api_key: os.environ["GEMINI_API_KEY"] = api_key
    mode = st.toggle("Active Camouflage", value=True)

real_intent = st.text_input("What are you actually searching for?", placeholder="e.g., Rolex Daytona")

if st.button("Initialize Ghost Persona") and real_intent:
    inverter = IntentInverter()
    with st.spinner("AI generating adversarial persona..."):
        ghost = inverter.generate_ghost_persona(real_intent)
    
    st.metric("Persona Generated", ghost.persona_type)
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number", value = ghost.entropy_score * 100,
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#E63946"}},
        title = {'text': "Tracker Confusion (%)"}
    ))
    st.plotly_chart(fig)

    controller = MimeticController()
    controller.interaction_loop(ghost.queries, log)

st.subheader("Live Execution Logs")
for l in reversed(st.session_state.logs): st.write(l)
