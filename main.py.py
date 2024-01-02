import streamlit as st
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

# Configure GenerativeAI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

# Streamlit UI
st.title("Medical Image Analysis App")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Ask user to select analysis type
analysis_type = st.radio("Select analysis type:", ["Medical Image Analysis", "Medicine Image Analysis"], index=0)

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    # Generate response when the user clicks the "Analyze" button
    if st.button("Analyze"):
        # Read the image from the uploaded file
        img = Image.open(uploaded_file)

        # Sample prompts for analysis
        if analysis_type == "Medical Image Analysis":
            sample_prompt = """
            You are a medical practitioner and an expert in analyzing medical-related images working for a very reputed hospital. 
            You will be provided with images and you need to identify the anomalies, any disease or health issues. 
            You need to generate the result in a detailed manner. Write all the findings, next steps, recommendations, etc. 
            You only need to respond if the image is related to a human body and health issues. 
            You must have to answer but also write a disclaimer saying that "Consult with a Doctor before making any decisions."

            Remember, if certain aspects are not clear from the image, it's okay to state 'Unable to determine based on the provided image.'

            Now analyze the image and answer the above questions in the same structured manner defined above
            """
        elif analysis_type == "Medicine Image Analysis":
            sample_prompt = """
            You are a medical practitioner and an expert in analyzing Medicine images working for a very reputed hospital. 
            You will be provided with images and you need to identify the Medicine type, its formula, its side effects, and its use cases. 
            You need to generate the result in a detailed manner. Write all the findings, next steps, use cases, and Side effects etc. 
            You only need to respond if the image is related to a Medicine. 
            You must have to answer but also write a disclaimer saying that "Consult with a Doctor before making any decisions."

            Remember, if certain aspects are not clear from the image, it's okay to state 'Unable to determine based on the provided image.'

            Now analyze the image and answer the above questions in the same structured manner defined above
            """

        # Add a loading spinner
        with st.spinner("Analyzing..."):
            # Generate response using GenerativeAI model
            response = model.generate_content([sample_prompt, img])

        # Display the generated response
        st.text(response.text)

        # Download report button
        download_button = st.download_button(
            label="Download Report",
            data=BytesIO(response.text.encode('utf-8')),
            file_name="medical_analysis_report.txt",
            key="download_button"
        )
