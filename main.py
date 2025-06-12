import streamlit as st
import numpy as np
import pickle
import pandas as pd
from feature import FeatureExtraction
import validators
import os

# Page config
st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ensure pickle directory exists
os.makedirs("pickle", exist_ok=True)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .title {
        color: #2c3e50;
        text-align: center;
    }
    .result-safe {
        color: #27ae60;
        padding: 1rem;
        border: 2px solid #27ae60;
        border-radius: 5px;
        text-align: center;
    }
    .result-unsafe {
        color: #e74c3c;
        padding: 1rem;
        border: 2px solid #e74c3c;
        border-radius: 5px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
        with open("model.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error("⚠️ Model file not found. Please ensure model.pkl exists in the pickle directory.")
        return None
    except Exception as e:
        st.error(f"⚠️ Error loading model: {str(e)}")
        return None

# Header
st.title("🔒 Phishing URL Detector")
st.markdown("""
This tool uses machine learning to detect whether a URL is legitimate or potentially phishing.
Simply enter a URL below to check its safety.
""")

# Load model
model = load_model()

if model is None:
    st.warning("System is currently unavailable. Please try again later.")
    st.stop()

# URL input
url = st.text_input("Enter URL to analyze:", placeholder="https://example.com")

if st.button("Analyze URL", type="primary"):
    if not url:
        st.warning("Please enter a URL")
    elif not url.startswith(('http://', 'https://')):
        st.warning("Please enter a valid URL starting with http:// or https://")
    else:
        try:
            with st.spinner("🔍 Analyzing URL..."):
                # Extract features
                obj = FeatureExtraction(url)
                features = np.array(obj.getFeaturesList()).reshape(1, 30)

                # Make prediction
                prediction = model.predict(features)[0]
                probability = model.predict_proba(features)[0]

                # Display result
                if prediction == 1:
                    st.markdown(f"""
                    <div class="result-safe">
                        ✅ This URL appears to be safe<br>
                        Confidence: {probability[1]*100:.2f}%
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="result-unsafe">
                        ⚠️ This URL appears to be phishing<br>
                        Confidence: {probability[0]*100:.2f}%
                    </div>
                    """, unsafe_allow_html=True)

                # Show details in expander
                with st.expander("See Technical Details"):
                    feature_names = [
                        "Using IP", "URL Length", "Shortened URL", "At Symbol", 
                        "Double Slash Redirect", "Prefix Suffix", "Sub Domains",
                        "HTTPS", "Domain Registration Length", "Favicon",
                        "Non Standard Port", "HTTPS in Domain", "Request URL",
                        "URL of Anchor", "Links in Script", "Server Form Handler",
                        "Info Email", "Abnormal URL", "Website Forwarding",
                        "Status Bar Customization", "Disabled Right Click",
                        "Popup Window", "IFrame", "Age of Domain",
                        "DNS Record", "Web Traffic", "Page Rank",
                        "Google Index", "Links Pointing", "Statistical Report"
                    ]
                    
                    df = pd.DataFrame({
                        'Feature': feature_names,
                        'Value': features[0]
                    })
                    st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Error analyzing URL: {str(e)}")
            st.info("Please check if the URL is valid and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <small>Made with ❤️ using Streamlit • 
    <a href="https://github.com/RichaKumari10/phishing-detector">GitHub</a></small>
</div>
""", unsafe_allow_html=True)