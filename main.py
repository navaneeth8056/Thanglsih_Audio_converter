import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from speakatoo import convert_to_audio  # Import the function from speakatoo.py

# Load the environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini's text model (free tier)
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Function to convert English to Thanglish using Gemini API
def english_to_thanglish_with_gemini(text):
    prompt = (
        "Translate the following educational English content to Tamil. "
        "However, keep key English subject words like 'Physics', 'experiments', 'natural world', etc. in English. "
        "Ensure the Tamil flow is natural and useful for blind students in audio format.\n\n"
        f"{text}\n\nThanglish Output:"
    )

    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit UI
def create_ui():
    st.set_page_config(page_title="Thanglish Converter & Audio Player", layout="wide")
    st.title("Thanglish Text-to-Speech Converter")
    
    # Sidebar for page navigation
    st.sidebar.title("Navigation")
    st.sidebar.markdown("""
    ### Convert English to Thanglish
    This tool converts English content into Thanglish for educational purposes, making it accessible for blind students.
    """)
    
    st.markdown("## Input Section")
    
    # Input field for English text
    english_input = st.text_area(
        "Enter English Text",
        "Physics is the study of nature and how things work in the natural world. It forms the foundation of all science subjects.",
        height=200
    )
    
    # Button to trigger Thanglish conversion
    if st.button("Convert to Thanglish"):
        if english_input:
            # Convert text to Thanglish
            thanglish_output = english_to_thanglish_with_gemini(english_input)
            
            # Display Thanglish output
            st.markdown("### Thanglish Output")
            st.write(thanglish_output)
            
            # Save the output as an audio file
            convert_to_audio(thanglish_output)  # Save as audio

            # Audio player to listen to the converted audio
            audio_file = open("output_audio.mp3", "rb")
            st.audio(audio_file, format="audio/mp3")
            
            # Provide the download link for the audio
            st.download_button(
                label="Download Audio",
                data=audio_file,
                file_name="output_audio.mp3",
                mime="audio/mp3"
            )
        else:
            st.warning("Please enter some text to convert!")

# Call the UI creation function
if __name__ == "__main__":
    create_ui()
