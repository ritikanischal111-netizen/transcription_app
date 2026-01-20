import streamlit as st
import whisper
import tempfile
import os

# ------------------ Page Config ------------------
st.set_page_config(page_title="Japanese Transcription Tool")
st.title("🎧 Japanese Audio / Video Transcriber")

# ------------------ Pricing Section ------------------
st.markdown("## 💰 Pricing Plans")

st.markdown("""
### 🟢 Basic – ₹500
Up to **10 MB** audio / video  
👉 [Pay Now](https://rzp.io/rzp/mLuqttlf)

### 🔵 Standard – ₹1000
**10–50 MB** audio / video  
👉 [Pay Now](https://rzp.io/rzp/3V33GQ1)

### 🔴 Pro – ₹2000
**Above 50 MB** audio / video  
👉 [Pay Now](https://rzp.io/rzp/CkQNcOrg)

🕒 **Validity:** 1 Month  
⚠ Please complete payment before uploading files.
""")

st.divider()

# ------------------ Load Whisper Model ------------------
@st.cache_resource
def load_model():
    return whisper.load_model("small")

model = load_model()

# ------------------ Upload Section ------------------
uploaded_file = st.file_uploader(
    "Upload Audio or Video",
    type=["mp3", "wav", "m4a", "mp4"]
)

# ------------------ Transcription Logic ------------------
if uploaded_file:
    if st.button("Transcribe"):
        with st.spinner("Please wait, transcribing..."):
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(uploaded_file.read())
                temp_path = tmp.name

            result = model.transcribe(temp_path, language="ja")
            os.remove(temp_path)

        st.success("✅ Transcription completed!")
        st.text_area("Transcription Output", result["text"], height=300)
