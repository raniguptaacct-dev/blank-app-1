import google.generativeai as genai
import streamlit as st

st.title("✨ AI Astrologer - भविष्य जानें ✨")

# यूजर से सवाल पूछने का बॉक्स
user_query = st.text_input("अपना सवाल यहाँ लिखें:")

if st.button("भविष्य जानें ✨"):
  if user_query:
    try:
      # यहाँ अपनी Gemini API Key डालें (या Streamlit secrets का इस्तेमाल करें)
      # अपनी खुद की Gemini API Key यहाँ रख लें
      genai.configure(api_key="YOUR_GEMINI_API_KEY")

      # Gemini मॉडल सेट करें
      model = genai.GenerativeModel("gemini-1.5-flash")

      # ज्योतिष के रूप में जवाब देने के लिए प्रॉम्प्ट
      prompt = (
          f"You are an expert AI astrologer. Give a detailed, positive, and"
          f" inspiring astrological prediction for the following query: {user_query}"
      )

      with st.spinner("भविष्य की गणना की जा रही है..."):
        response = model.generate_content(prompt)
        astrology_result = response.text

      st.success("भविष्यवाणी:")
      st.write(astrology_result)

    except Exception as e:
      st.error(
          f"कुछ गड़बड़ हो गई है। कृपया API Key चेक करें या दोबारा कोशिश करें:"
          f" {e}"
      )
  else:
    st.warning("कृपया पहले अपना सवाल लिखें!")
      
