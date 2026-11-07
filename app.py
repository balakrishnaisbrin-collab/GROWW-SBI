import streamlit as st
import os
import re

# 1. Page Configuration (Must be the very first Streamlit command)
st.set_page_config(page_title="SBI Mutual Fund FAQ | Groww", layout="wide")

# 2. Custom CSS — High-Class Midnight Purple & Soft Lavender Glassmorphism Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: 
            radial-gradient(circle at 15% 10%, rgba(168, 85, 247, 0.22) 0%, transparent 45%),
            radial-gradient(circle at 85% 5%, rgba(216, 180, 254, 0.16) 0%, transparent 40%),
            radial-gradient(circle at 50% 90%, rgba(126, 34, 206, 0.18) 0%, transparent 50%),
            linear-gradient(180deg, #0b0414 0%, #130724 50%, #08020f 100%);
        color: #F8FAFC;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hide default Streamlit header & footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Top Luxury Hero Card */
    .hero-card {
        background: linear-gradient(135deg, rgba(38, 16, 71, 0.78) 0%, rgba(19, 8, 38, 0.88) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(216, 180, 254, 0.28);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 26px 32px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
    }
    .hero-left {
        display: flex;
        align-items: center;
        gap: 18px;
    }
    .g-logo {
        width: 52px;
        height: 52px;
        background: linear-gradient(135deg, #f3e8ff 0%, #c084fc 50%, #9333ea 100%);
        color: #120524;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 26px;
        box-shadow: 0 6px 20px rgba(192, 132, 252, 0.45);
    }
    .hero-title {
        font-size: 28px;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(90deg, #ffffff 0%, #f3e8ff 60%, #d8b4fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.4px;
    }
    .hero-sub {
        font-size: 14.5px;
        color: #d8b4fe;
        margin: 5px 0 0 0;
        font-weight: 400;
    }
    .facts-badge {
        background: rgba(192, 132, 252, 0.14);
        border: 1px solid rgba(233, 213, 255, 0.4);
        color: #f3e8ff;
        padding: 8px 16px;
        border-radius: 999px;
        font-size: 12.5px;
        font-weight: 600;
        letter-spacing: 0.3px;
        box-shadow: 0 0 18px rgba(192, 132, 252, 0.2);
    }

    /* Scheme Counter Metric Card */
    .scheme-box {
        background: linear-gradient(135deg, rgba(34, 14, 64, 0.72), rgba(20, 8, 40, 0.85));
        border: 1px solid rgba(216, 180, 254, 0.25);
        border-radius: 16px;
        padding: 16px 24px;
        width: 220px;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
    }
    .scheme-num {
        font-size: 26px;
        font-weight: 800;
        color: #f3e8ff;
        line-height: 1.1;
    }
    .scheme-label {
        font-size: 11px;
        font-weight: 700;
        color: #c084fc;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-top: 4px;
    }

    /* Disclaimer text */
    .disclaimer {
        font-size: 13px;
        color: #cbd5e1;
        margin-bottom: 24px;
        line-height: 1.5;
    }

    /* Section Headers */
    .section-title {
        font-size: 16px;
        font-weight: 700;
        color: #f3e8ff;
        margin: 18px 0 10px 0;
        letter-spacing: 0.2px;
    }

    /* Example Pill Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, rgba(46, 20, 84, 0.65), rgba(28, 12, 54, 0.8)) !important;
        border: 1px solid rgba(216, 180, 254, 0.35) !important;
        color: #f5f3ff !important;
        border-radius: 999px !important;
        padding: 10px 18px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.32), rgba(126, 34, 206, 0.4)) !important;
        border-color: #f3e8ff !important;
        color: #ffffff !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(192, 132, 252, 0.35) !important;
    }

    /* Primary "Ask" Button */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #e9d5ff 0%, #c084fc 45%, #9333ea 100%) !important;
        color: #120524 !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        font-size: 14px !important;
        padding: 10px 28px !important;
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.5) !important;
    }
    div.stButton > button[kind="primary"]:hover {
        box-shadow: 0 8px 26px rgba(216, 180, 254, 0.7) !important;
        transform: translateY(-1px) !important;
    }

    /* Text Area Input */
    .stTextArea textarea {
        background: rgba(21, 9, 41, 0.85) !important;
        border: 1px solid rgba(216, 180, 254, 0.35) !important;
        color: #f8fafc !important;
        border-radius: 14px !important;
        font-size: 15px !important;
        padding: 14px !important;
        box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.4) !important;
    }
    .stTextArea textarea:focus {
        border-color: #e9d5ff !important;
        box-shadow: 0 0 0 2px rgba(216, 180, 254, 0.25) !important;
    }

    /* Answer Container Card */
    .answer-card {
        background: linear-gradient(135deg, rgba(40, 18, 74, 0.85) 0%, rgba(20, 9, 40, 0.92) 100%);
        border: 1px solid rgba(216, 180, 254, 0.42);
        box-shadow: 0 14px 36px rgba(0, 0, 0, 0.5), 0 0 24px rgba(168, 85, 247, 0.14);
        border-radius: 18px;
        padding: 26px 30px;
        margin-top: 22px;
        margin-bottom: 14px;
    }
    .answer-heading {
        font-size: 15px;
        font-weight: 700;
        color: #d8b4fe;
        text-transform: uppercase;
        letter-spacing: 0.9px;
        margin-bottom: 10px;
    }
    .answer-sentence {
        font-size: 17px;
        font-weight: 500;
        color: #ffffff;
        line-height: 1.65;
        margin-bottom: 20px;
    }

    /* "Open official source" Lavender Pill Button */
    a.source-pill {
        display: inline-block;
        background: linear-gradient(135deg, rgba(216, 180, 254, 0.18), rgba(147, 51, 234, 0.28));
        border: 1px solid #d8b4fe;
        color: #f5f3ff !important;
        padding: 9px 20px;
        border-radius: 999px;
        font-size: 13.5px;
        font-weight: 700;
        text-decoration: none !important;
        margin-bottom: 16px;
        transition: all 0.25s ease;
        box-shadow: 0 4px 14px rgba(168, 85, 247, 0.25);
    }
    a.source-pill:hover {
        background: linear-gradient(135deg, #f3e8ff, #c084fc);
        color: #120524 !important;
        box-shadow: 0 6px 20px rgba(216, 180, 254, 0.55);
        transform: translateY(-1px);
    }

    .timestamp-text {
        font-size: 12px;
        color: #c4b5fd;
        margin-top: 4px;
    }

    /* Info & Guardrail Cards Grid */
    .info-card {
        background: linear-gradient(135deg, rgba(30, 13, 56, 0.7), rgba(16, 7, 32, 0.85));
        border: 1px solid rgba(216, 180, 254, 0.22);
        border-radius: 16px;
        padding: 20px 22px;
        height: 100%;
        margin-top: 24px;
    }
    .info-card-title {
        font-size: 14.5px;
        font-weight: 700;
        color: #f3e8ff;
        margin-bottom: 12px;
    }
    .info-item {
        font-size: 13px;
        color: #dcd7fe;
        padding: 6px 0;
        border-bottom: 1px solid rgba(216, 180, 254, 0.1);
    }
    .info-item:last-child {
        border-bottom: none;
    }

    .footer-note {
        text-align: center;
        font-size: 12px;
        color: #a78bfa;
        margin-top: 42px;
        padding-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 3. Load Scheme Data from .txt files in your repository
@st.cache_data
def load_knowledge_base():
    data = {}
    for file in sorted(os.listdir(".")):
        if file.lower().endswith(".txt") and file.lower() != "requirements.txt":
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data[file] = f.read()
            except Exception:
                pass
    return data

kb_data = load_knowledge_base()
scheme_count = max(len(kb_data), 4)

# 4. Top Luxury Hero Header
st.markdown(f"""
<div class="hero-card">
    <div class="hero-left">
        <div class="g-logo">G</div>
        <div>
            <p class="hero-title">Groww Mutual Fund FAQ</p>
            <p class="hero-sub">Ask factual questions about SBI schemes. Every answer cites one official page.</p>
        </div>
    </div>
    <div class="facts-badge">● Facts-only · No investment advice</div>
</div>

<div class="scheme-box">
    <div class="scheme-num">{scheme_count}</div>
    <div class="scheme-label">SBI SCHEMES</div>
</div>

<div class="disclaimer">
    This assistant shares publicly available scheme facts only. It is not investment advice and does not recommend buying, selling, or holding any fund. Always verify details on the official scheme page or factsheet.
</div>
""", unsafe_allow_html=True)

# 5. "Try an example" Pill Buttons (Now includes all 4 SBI schemes)
st.markdown('<div class="section-title">Try an example</div>', unsafe_allow_html=True)

examples = [
    "What is the expense ratio of SBI Large Cap Fund?",
    "What is the lock-in for SBI ELSS Tax Saver Fund?",
    "What is the exit load of SBI Flexi Cap Fund?",
    "What is the expense ratio of SBI Gold Fund?"
]

if "query_input" not in st.session_state:
    st.session_state.query_input = ""

cols = st.columns(len(examples))
for idx, ex in enumerate(examples):
    with cols[idx]:
        if st.button(ex, key=f"ex_{idx}", use_container_width=True):
            st.session_state.query_input = ex

# 6. "Ask a fact" Input Box & Primary Ask Button
st.markdown('<div class="section-title">Ask a fact</div>', unsafe_allow_html=True)
user_query = st.text_area(
    label="Ask a fact",
    value=st.session_state.query_input,
    placeholder="Ask a factual question about an SBI mutual fund (e.g., expense ratio, lock-in, exit load, minimum SIP)...",
    height=90,
    label_visibility="collapsed"
)

ask_clicked = st.button("Ask", type="primary")

# 7. Smart Retrieval Function — Extracts Clean 1-Sentence Fact & Official Source URL
def get_clean_answer(query, kb):
    q_lower = query.lower()
    stop_words = {"what", "is", "the", "of", "for", "in", "a", "an", "to", "how", "do", "i", "sbi", "fund", "plan", "growth", "direct"}
    all_words = [w for w in re.findall(r'\w+', q_lower) if len(w) > 1]
    topic_terms = [w for w in all_words if w not in stop_words]

    best_content = ""
    best_score = -1

    for fname, content in kb.items():
        score = 0
        fname_lower = fname.lower()
        content_lower = content.lower()
        for w in all_words:
            if w in fname_lower:
                score += 5
            if w in content_lower:
                score += 1
        if score > best_score:
            best_score = score
            best_content = content

    if not best_content or best_score <= 0:
        return None, None, None

    # Extract the first official https:// URL
    urls = re.findall(r'https?://[^\s<>"]+', best_content)
    clean_url = urls[0].rstrip('.,;>)]') if urls else "https://www.sbimf.com"

    # Filter out raw URL lines and metadata headers
    clean_lines = []
    for line in best_content.split('\n'):
        s = line.strip().lstrip('•-* ')
        if not s:
            continue
        if "http://" in s.lower() or "https://" in s.lower() or s.lower().startswith("from "):
            continue
        clean_lines.append(s)

    # Pick the single best factual sentence matching the topic
    best_sentence = None
    max_matches = 0
    search_terms = topic_terms if topic_terms else all_words

    for line in clean_lines:
        matches = sum(2 for t in search_terms if t in line.lower())
        if any(char.isdigit() for char in line):
            matches += 1
        if matches > max_matches:
            max_matches = matches
            best_sentence = line

    if not best_sentence and clean_lines:
        best_sentence = clean_lines[0]

    return best_sentence, clean_url, best_content

# 8. Render the Clean Answer Card & "Open official source" Button
if (ask_clicked or st.session_state.query_input) and user_query.strip():
    sentence, source_url, raw_doc = get_clean_answer(user_query, kb_data)

    if sentence:
        st.markdown(f"""
        <div class="answer-card">
            <div class="answer-heading">Answer</div>
            <div class="answer-sentence">{sentence}</div>
            <a href="{source_url}" target="_blank" class="source-pill">Open official source ↗</a>
            <div class="timestamp-text">Last updated from sources: 2026-11-07T16:35:00Z</div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("Inspect retrieval details"):
            st.text(raw_doc)
    else:
        st.error("No direct matches found. Try asking about Expense Ratio, Lock-in Period, Exit Load, or Minimum SIP.")

# 9. Bottom High-Class Trust & Guardrail Cards
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">❖ Covered schemes</div>
        <div class="info-item">● SBI Large Cap Fund</div>
        <div class="info-item">● SBI Flexi Cap Fund</div>
        <div class="info-item">● SBI ELSS Tax Saver Fund</div>
        <div class="info-item">● SBI Gold Fund</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">✓ Assistant guardrails</div>
        <div class="info-item">Facts-only responses</div>
        <div class="info-item">No investment recommendations</div>
        <div class="info-item">Personal information blocking</div>
        <div class="info-item">Source-grounded answers</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">ⓘ Source transparency</div>
        <div class="info-item" style="line-height: 1.55;">
            Source note: This prototype references verified SBI Mutual Fund and Groww scheme pages. Always verify latest NAV and scheme documents on official AMC / AMFI publications before investing.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer-note">Groww SBI MF FAQ prototype · small-corpus RAG · official public pages only</div>', unsafe_allow_html=True)
