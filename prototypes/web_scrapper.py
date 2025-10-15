"""User interface for website crawling management."""

import streamlit as st

# --- App setup ---
st.set_page_config(page_title="Scraper Dashboard", page_icon="🕷️", layout="centered")

# --- Sidebar / Navigation ---
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Collected", "Add"])

# --- Section: Collected ---
if section == "Collected":
    st.title("🗂️ Collected Domains")
    # Mock data (replace with your DB query)
    collected_domains = ["example.com", "foodblog.net", "newsportal.org"]

    if collected_domains:
        for domain in collected_domains:
            st.markdown(f"- **{domain}**")
    else:
        st.info("No domains collected yet.")

# --- Section: Add ---
elif section == "Add":
    st.title("🌎 Add New Source")
    st.write("You can add a domain **or** a single page URL:")

    col1, col2, col3 = st.columns([1, 0.2, 1])
    with col1:
        domain = st.text_input("Domain", placeholder="e.g. example.com")
    with col2:
        st.markdown(
            "<br><h4 style='text-align:center;'>OR</h4>", unsafe_allow_html=True
        )
    with col3:
        url = st.text_input("Page URL", placeholder="e.g. https://example.com/article")

    if st.button("Add"):
        if domain or url:
            added = domain or url
            st.success(f"✅ Added: {added}")
            # TODO: insert into your database here
        else:
            st.warning("Please enter a domain or a URL.")
