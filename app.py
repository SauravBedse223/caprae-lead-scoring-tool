import streamlit as st
import pandas as pd
from utils.enrichment import enrich_data
from utils.scoring import score_leads

st.set_page_config(page_title="Lead Scoring Tool", layout="centered")

st.title("🔍 Smart Lead Scoring & Filtering Tool")

uploaded_file = st.file_uploader("Upload CSV of Company Names or Domains", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        if df.empty:
            st.error("❌ Uploaded file is empty. Please upload a valid CSV.")
        else:
            st.subheader("🔎 Input Data Preview")
            st.write(df.head())

            enriched_df = enrich_data(df)
            scored_df = score_leads(enriched_df)

            st.subheader("🏆 Scored Leads")
            st.dataframe(scored_df.sort_values("score", ascending=False))

            st.download_button(
                label="⬇️ Download Scored Leads",
                data=scored_df.to_csv(index=False).encode('utf-8'),
                file_name="scored_leads.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
else:
    st.info("👈 Please upload a CSV file to begin.")
