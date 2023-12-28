import requests
from Difficulty import Difficulty
from Languages import Languages

class OpenAIImplementation:

    # Variables inputted by the user

    def  __init__(self):
        self.prompts = []
        self.difficulty = Difficulty.VERY_HARD
        self.language = Languages.ENGLISH
        self.userResponse = ""

    # Setters
    def setPrompts(self, inputtedPrompts):
        self.prompts = inputtedPrompts

    def setDifficulty(self, inputtedDifficulty):
        self.difficulty = inputtedDifficulty

    def setLangauge(self, inputtedLanguage):
        self.language = inputtedLanguage

    def updateUserResponse(self, newMessage):
        self.userResponse = newMessage

    # Getters
    def getPrompts(self):
        return self.prompts
    
    def getDifficulty(self):
        return self.difficulty

    def format_list(self, items):
        if len(items) == 0:
            return "Nothing yet"
        elif len(items) == 1:
            return items[0]
        else:
            # Join all items except the last one with commas, then add the last item with "and"
            return ", ".join(items[:-1]) + " and " + items[-1]

    # Handle the actual request being sent to the ChatGPT API
    def sendRequest(self):

        # Specify Headers, including Authorization Header and Content Type
        headers = {
            'Authorization': 'Bearer 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',
            'Content-Type': 'application/json'
        }

        # Specify the Body of the request
        message = f'I am a student learning to speak {self.language.value}. You are John, a student. I want you to ask me a question in {self.language.value}. On a scale of 1 to 5, where 1 is a complete beginner and 5 is fluent, the conversation level should be {self.difficulty.value}.' \
                f'Our conversation will involve prompts like: {self.format_list(self.prompts)}. I will answer your questions and ask new ones. You can provide opinions or ask questions as well.' \
                f'My response to you is: {self.userResponse}. If you think, that at the end of my response I am asking you a question, I want you to answer it as John, then ask me another question'

# The rest of your code...

        print(message)

        body = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": message}],
            "temperature": 0.7
        }

        # Make the POST Request and return the message if it exists
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=body)
        try:
            result = response.json()['choices'][0]['message']['content']
            print(result)
            return result
        except (KeyError, IndexError, ValueError):
            # Handle the case where the expected structure is not found in the response
            return "Error: Unexpected response format"