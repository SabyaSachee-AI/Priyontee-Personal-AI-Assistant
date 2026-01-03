import streamlit as st
from preontee.assistant import PriyonteeAssistant
from preontee.gemini_engine import GeminiEngine
from preontee.prompt_controller import PromptController
from preontee.memory import Memory
from preontee.voice import VoiceAssistant
from preontee.pdf_exporter import PDFExporter
from config.settings import Settings

# Page setup
st.set_page_config(page_title="Priyontee!", layout="centered")
st.title("💖 Priyontee! – Your Personal AI Assistant")
st.caption("Text & Voice Enabled | Powered by Gemini API")

# Core setup
settings = Settings()
engine = GeminiEngine(settings.load_api_key())
memory = Memory()
voice = VoiceAssistant()

# Sidebar: AI role selection
role = st.sidebar.selectbox(
    "🎭 Select AI Role",
    ["General Assistant", "Coder", "Instructor", "Doctor", "Career Mentor"]
)

prompt_controller = PromptController(role)
priyontee = PriyonteeAssistant(engine, prompt_controller, memory)

# Sidebar: Clear memory
if st.sidebar.button("🗑 Clear Memory"):
    memory.clear()
    st.sidebar.success("Memory cleared")

# Sidebar: Download chat as PDF
if st.sidebar.button("📄 Download Chat as PDF"):
    pdf_exporter = PDFExporter()
    file = pdf_exporter.export(memory.get_history())
    with open(file, "rb") as f:
        st.sidebar.download_button("⬇ Download PDF", f, file_name=file)

# Display chat history
for chat in memory.get_history():
    with st.chat_message(chat["role"].lower()):
        st.write(chat["message"])

# User input
user_input = st.chat_input("Ask Priyontee...")

# Voice input
if st.button("🎤 Speak"):
    st.info("Listening...")
    voice_input = voice.listen()
    if voice_input:
        user_input = voice_input
        st.success(f"You said: {voice_input}")

# Process user input
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    response = priyontee.respond(user_input)

    with st.chat_message("assistant"):
        st.write(response)

    # Voice output
    voice.speak(response)
