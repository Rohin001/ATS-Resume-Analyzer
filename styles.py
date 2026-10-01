import streamlit as st


def apply_styles():

    st.markdown("""
    <style>

    .stApp {
        background-color: #f5f7fa;
        color: #111827;
    }

    h1, h2, h3 {
        color: #111827 !important;
        font-weight: 700;
    }

    p, label, div, span {
        color: #1f2937 !important;
    }

    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
    }

    .stTextArea textarea {
        background-color: white !important;
        color: black !important;
    }

    /* Paste your button part here */

    .stDownloadButton button {
        background-color: #2563eb !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }

    .stDownloadButton button:hover {
        background-color: #1d4ed8 !important;
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)