EasyMed Scan
EasyMed Scan is a web application developed using Streamlit and Google's Gemini for medical and medicine image analysis.

Installation
Clone the repository:
git clone https://https://github.com/Khalil-Rehman9/EasyMed-Scan.git
cd your_repository
Install the required dependencies:


pip install -r requirements.txt
Set up the environment variables:
Create a .env file in the root directory and add your Gemini API key:


GOOGLE_API_KEY=your_google_api_key
Usage
Run the Streamlit app locally:


streamlit run app.py
Visit http://localhost:8501 in your browser to use EasyMed Scan.


Features
Upload medical or medicine images in JPG, JPEG, or PNG format.
Choose between Medical Image Analysis and Medicine Image Analysis.
Click the "Analyze" button to generate detailed analysis reports.
Download the generated report as a text file.
How it Works
Upload an image of a medical-related subject.
Select the analysis type: Medical Image Analysis or Medicine Image Analysis.
Click the "Analyze" button to process the image.
View the detailed analysis report and download it if needed.


Disclaimer
This application provides automated analysis and should not replace professional medical advice. Always consult with a doctor before making any decisions based on the generated reports.
