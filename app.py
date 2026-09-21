import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import base64

load_dotenv()

favicon_path = "logo2.jpeg" if os.path.exists("logo2.jpeg") else ("logo2.jpg" if os.path.exists("logo2.jpg" ) else ("logo1.jpeg" if os.path.exists("logo1.jpeg") else "📊"))

st.set_page_config(
    page_title="Hasamex Enterprise Intelligence", 
    page_icon=favicon_path, 
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .block-container { 
        padding-top: 1.5rem; 
        padding-bottom: 4rem; 
        max-width: 950px; 
    }
    .stChatMessage { 
        border-radius: 12px; 
        padding: 1.2rem; 
        margin-bottom: 1.2rem; 
        border: 1px solid #E2E8F0; 
    }
    .stButton button { 
        border-radius: 20px; 
        font-weight: 500; 
        border: 1px solid #CBD5E1; 
        transition: all 0.2s ease; 
        width: 100%;
    }
    .stButton button:hover { 
        border-color: #1E3A8A; 
        color: #1E3A8A; 
        background: #EFF6FF; 
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource(show_spinner=False)
def init_llm():
    return ChatGroq(model="openai/gpt-oss-120b", temperature=0.0)

llm = init_llm()

# --- Left Sidebar: Logo 2 on top, then Developer Name ---
logo2_file = "logo2.jpeg" if os.path.exists("logo2.jpeg") else ("logo2.jpg" if os.path.exists("logo2.jpg") else None)

with st.sidebar:
    if logo2_file:
        st.image(logo2_file, width=200)
    st.markdown("<p style='font-size: 0.85rem; color: #64748B; margin-top: 1rem; margin-bottom: 0px; font-weight: 600;'>DEVELOPER</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top: 0px;'>Tanvi Prakash Patil</h3>", unsafe_allow_html=True)

# --- Main Header: Logo 1 Centered, Zoomed In ---
logo1_file = "logo1.jpeg" if os.path.exists("logo1.jpeg") else ("logo1.jpg" if os.path.exists("logo1.jpg") else None)

if logo1_file:
    with open(logo1_file, "rb") as img_file:
        encoded_logo1 = base64.b64encode(img_file.read()).decode()
    
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 0.2rem; margin-top: 0rem;">
            <img src="data:image/jpeg;base64,{encoded_logo1}" style="max-height: 180px; width: auto; object-fit: contain;" />
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align: center; font-weight: 800; font-size: 2.5rem;'>Hasamex: Expert Call Intelligence</h1>", unsafe_allow_html=True)

st.markdown("<hr style='margin-top: 0.5rem; margin-bottom: 1rem;'>", unsafe_allow_html=True)

# System prompt adhering strictly to case requirements
system_prompt = """You are a senior AI research analyst reviewing European robotic surgery expert call transcripts.
Analyze the provided transcript context thoroughly to answer the user's executive query. 
CRITICAL GUARDRAILS:
1. Always support insights with exact verbatim quotes.
2. Mandatorily cite the source and timestamp for every claim in the exact format: [Expert Name - Timestamp].
3. Explicitly surface convergence (common themes) and divergence (disagreements) across markets.
4. If the data is absent from the transcripts, explicitly state that it is unavailable. Zero hallucination tolerance.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "Here are the interview transcripts:\n\n{context}\n\nUser Question: {question}")
])
chain = prompt | llm

if "query_to_run" not in st.session_state:
    st.session_state.query_to_run = None

st.markdown("<small style='font-weight: 600;'>SUGGESTED EXECUTIVE QUERIES:</small>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Main Adoption Barriers"):
        st.session_state.query_to_run = "What are the main barriers to adoption across the markets?"
with col2:
    if st.button("Purchase Timelines"):
        st.session_state.query_to_run = "What are the exact hospital purchase decision timelines mentioned by each expert?"
with col3:
    if st.button("3-5 Year Outlook & ROI"):
        st.session_state.query_to_run = "What adoption trends and ROI expectations do experts project over the next 3-5 years?"

st.markdown("<br>", unsafe_allow_html=True)

user_input = st.chat_input("Ask a question across transcripts (e.g., 'How do France and Germany compare on procurement?')")
active_query = user_input or st.session_state.query_to_run
st.session_state.query_to_run = None

if active_query:
    user_avatar_file = "user_logo.jpeg" if os.path.exists("user_logo.jpeg") else ("user_logo.jpg" if os.path.exists("user_logo.jpg") else None)
    user_avatar = user_avatar_file if user_avatar_file else "user"

    st.chat_message("user", avatar=user_avatar).write(active_query)
    
    assistant_avatar = logo2_file if logo2_file else "assistant"
    
    with st.chat_message("assistant", avatar=assistant_avatar):
        with st.spinner("Synthesizing multi-expert insights..."):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(current_dir, "data")
            
            formatted_context = ""
            if os.path.exists(data_dir):
                for filename in os.listdir(data_dir):
                    if filename.endswith(".txt") and "Interview_Guide" not in filename:
                        with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as f:
                            formatted_context += f"\n=== Source File: {filename} ===\n" + f.read()
            
            response = chain.invoke({
                "context": formatted_context, 
                "question": active_query
            })
            
            st.markdown(response.content)