# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi , I am Afridi"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs
import os

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        voice_id="B6PJxMQ0Brihd46NR86u", 
        model_id="eleven_turbo_v2",
        text=input_text
    )
    elevenlabs.save(audio, output_filepath)

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing.mp3") 


# *****************************************************************************************************************************************************
                                              #  You can test this if yours doesnt work ****
# *****************************************************************************************************************************************************

# Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# from elevenlabs.client import ElevenLabs
# import os

# ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
#     # Use the correct method from the new SDK
#     audio = client.text_to_speech.convert(
#         voice_id="B6PJxMQ0Brihd46NR86u",  
#         model_id="eleven_turbo_v2",
#         text=input_text
#     )

#     with open(output_filepath, "wb") as f:
#         f.write(audio)

#     print(f"✅ ElevenLabs audio saved to: {output_filepath}")

