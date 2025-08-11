import streamlit as st
from rag import process_urls, generate_answer

# --- Page Config ---
st.set_page_config(
    page_title="Financial Market Research Tool",
    page_icon="📊",
    layout="wide"
)

# --- Title ---
st.title("📊 Financial Market Research Tool")
st.markdown("Summarize financial news & get AI-powered answers from provided URLs.")

# --- Sidebar ---
st.sidebar.header("🔗 Enter URLs to Analyze")
urls = [
    url.strip()
    for url in [
        st.sidebar.text_input(f"URL {i+1}", placeholder="https://example.com")
        for i in range(3)
    ]
    if url.strip()
]

# --- Placeholder for status updates ---
status_box = st.empty()

# --- Process URLs ---
if st.sidebar.button("🚀 Process URLs"):
    if not urls:
        status_box.warning("⚠️ Please enter at least one valid URL.")
    else:
        status_box.info("Starting URL processing...")
        for status in process_urls(urls):  # This preserves the yield updates
            status_box.info(status)
        status_box.success("✅ All URLs processed!")

# --- Query Section ---
st.subheader("💬 Ask a Question")
query = st.text_input("Type your question about the processed data...")

if st.button("🔍 Get Answer"):
    if not query.strip():
        st.warning("⚠️ Please enter a question.")
    else:
        try:
            with st.spinner("Generating answer..."):
                answer, sources = generate_answer(query)

            st.markdown("### 📝 Answer")
            st.write(answer)

            if sources:
                st.markdown("### 📚 Sources")
                for source in sources:
                    st.markdown(f"- [{source}]({source})")

        except RuntimeError:
            st.error("❌ Please process URLs first.")
