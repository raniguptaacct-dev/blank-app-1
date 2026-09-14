import streamlit as st
import requests

st.set_page_config(page_title="AI Astrologer", page_icon="✨", layout="centered")

st.title("✨ आपका अपना AI ज्योतिषी (AI Astrologer)")
st.write("अपने जीवन, करियर या भविष्य से जुड़ा कोई भी सवाल नीचे पूछें।")

# आपका n8n Production Webhook URL
N8N_WEBHOOK_URL = "https://rani-gupta.app.n8n.cloud/webhook/5c17d3b2-0142-4389-af48-18f13e346c7f"

user_question = st.text_input("अपना सवाल यहाँ लिखें:", placeholder="जैसे: मेरी नौकरी में तरक्की कब होगी?")

if st.button("भविष्य जानें ✨"):
    if not user_question.strip():
        st.warning("कृपया पहले अपना सवाल लिखें!")
    else:
        with st.spinner("ज्योतिषी जी गणना कर रहे हैं, कृपया प्रतीक्षा करें..."):
            try:
                # n8n वेबहुक पर डेटा भेजना
                response = requests.post(
                    N8N_WEBHOOK_URL,
                    json={"question": user_question}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    # n8n से आने वाला उत्तर दिखाना
                    answer = data.get("output") or data.get("response") or data.get("message") or str(data)
                    st.success("✨ **भविष्यवाणी:**")
                    st.write(answer)
                else:
                    st.error("उत्तर प्राप्त करने में समस्या आई। कृपया n8n वर्कफ़्लो और कनेक्शन जांचें।")
            except Exception as e:
                st.error(f"कनेक्शन एरर: {e}")
              
