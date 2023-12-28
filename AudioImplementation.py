import sounddevice as sd 
import numpy as np
from pydub import AudioSegment
from openai import OpenAI
from gtts import gTTS
import os
import pygame

class AudioImplementation():
    def record_and_save_mp3(self, output_file, duration=10, sample_rate=44100):
        print("Recording audio...")

        # Record audio
        audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=2, dtype=np.int16)
        sd.wait()

        # Convert audio data to AudioSegment
        audio_segment = AudioSegment(
            audio_data.tobytes(),
            frame_rate=sample_rate,
            sample_width=audio_data.dtype.itemsize,
            channels=2
        )

        # Save as MP3 file
        audio_segment.export(output_file, format="mp3")

        print(f"Audio recorded and saved to {output_file}")
        print(self.speech_to_text())

    def speech_to_text(self):
        client = OpenAI()

        audio_file_path = "C:/Projects/languageLearner/recorded_audio.mp3"
        with open(audio_file_path, 'rb') as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format='text'
            )

        return transcript
    
    def text_to_speech(self, text, language='en', output_file='mostrecentresponse.mp3'):
        try:
            # Create a gTTS object
            tts = gTTS(text=text, lang=language, slow=False)
            
            # Save the speech as an audio file
            tts.save(output_file)
            
            print(f"Text-to-speech conversion completed. Output saved to '{output_file}'")
            
            pygame.mixer.init()
            sound = pygame.mixer.Sound(output_file)
            sound.play()
            pygame.time.wait(int(sound.get_length() * 1000))
            print("Sound Completed!")

        except Exception as e:
            print(f"Error: {e}")