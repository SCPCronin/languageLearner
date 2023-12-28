from OpenAIImplementation import OpenAIImplementation
from AudioImplementation import AudioImplementation

if __name__ == "__main__":
    openai_instance = OpenAIImplementation()  # Create an instance of OpenAIImplementation
    audio_instance = AudioImplementation()

    i = 0
    while (i < 10):
        openai_instance.setPrompts(["Philosophy"])  # Set prompts if needed
        chatGPTResponse = openai_instance.sendRequest()  # Call sendRequest with the instance
        audio_instance.text_to_speech(chatGPTResponse)
        myResponse = audio_instance.record_and_save_mp3("recorded_audio.mp3")
        myResponseAsText = audio_instance.speech_to_text()
        openai_instance.updateUserResponse(myResponseAsText)
        i = i + 1
