import streamlit as st
from model import predict_emotion

st.title("Facial Emotion Detection App")
st.write("Upload a face image to detect the emotion.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.write("Processing...")

    try:
        prediction = predict_emotion(uploaded_file)
        st.success(f"Predicted Emotion: {prediction}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
