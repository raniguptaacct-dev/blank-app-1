import streamlit as st
import requests

st.set_page_config(page_title="AI Astrologer", page_icon="✨", layout="centered")

st.title("✨ आपका अपना AI ज्योतिषी (AI Astrologer)")
st.write("अपने जीवन, करियर या भविष्य से जुड़ा कोई भी सवाल नीचे पूछें।")

# उपयोगकर्ता से सवाल पूछने के लिए इनपुट बॉक्स
user_query = st.text_input("अपना सवाल यहाँ लिखें:", placeholder="जैसे: मेरी नौकरी में तरक्की कब होगी?")

if st.button("भविष्य जानें ✨"):
    if user_query:
        with st.spinner("ग्रहों की चाल का अध्ययन किया जा रहा है..."):
            try:
                # n8n वेबहुक का लिंक (बैकएंड)
                webhook_url = "YOUR_N8N_WEBHOOK_URL_HERE"
                
                response = requests.post(webhook_url, json={"question": user_query})
                
                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("output", "ज्योतिषी से उत्तर प्राप्त हुआ।")
                    st.success("🔮 भविष्यवाणी:")
                    st.write(answer)
                else:
                    st.error("सर्वर से जुड़ने में समस्या आ रही है। कृपया थोड़ी देर बाद कोशिश करें।")
            except Exception as e:
                st.error(f"त्रुटि (Error): {e}")
    else:
            st.warning("कृपया पहले अपना सवाल दर्ज करें!")
        
