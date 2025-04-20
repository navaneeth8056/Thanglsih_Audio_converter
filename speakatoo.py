import os
import requests
import json
from dotenv import load_dotenv

# Load your Speakatoo API key from .env
load_dotenv()

# Function to convert Thanglish content to audio using the Speakatoo API
def convert_to_audio(thanglish_output):
    # Speakatoo API credentials and parameters
    username = "Navaneeth"  
    password = "Nava@8056" 
    tts_title = "Testing Nava"  
    voice_name = "Mahesh"  
    tts_engine = "neural"  
    tts_format = "mp3"  
    tts_resource_ids = "YWkg1btPM7b8bdbf0dbc4383c74a321594c6900075nHXLIKiY"  
    ssml_mode = "0"
    synthesize_type = "save" 

    # API URL
    url = "https://www.speakatoo.com/api/v1/voiceapi"

    # Prepare payload
    payload = {
        "username": username,
        "password": password,
        "tts_title": tts_title,
        "ssml_mode": ssml_mode,
        "tts_engine": tts_engine,
        "tts_format": tts_format,
        "tts_text": thanglish_output,
        "tts_resource_ids": tts_resource_ids,
        "synthesize_type": synthesize_type,
    }

    # Headers with your API Key
    headers = {
        'X-API-KEY': os.getenv("SPEAKATOO_API_KEY"),  # Ensure the API key is loaded from .env
        'Content-Type': 'application/json',
    }

    try:
        # Sending the POST request to Speakatoo API
        response = requests.post(url, headers=headers, json=payload)

        # Check if the response is successful
        if response.status_code == 200:
            # Save the audio file (e.g., as an MP3 file)
            with open("output_audio.mp3", "wb") as f:
                f.write(response.content)
            print("\nAudio conversion successful! Saved as output_audio.mp3.")
        else:
            print(f"Error: {response.status_code}, {response.text}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
