# Language Learning Assitant

This is a python application which will help in learning languages by allowing you speak to ChatGPT in the language of your choice.
There are many great sites out there for learning Vocabulary, but when it comes to actually speaking the language, the tools available are not the best as the conversations are easy to repeat and memorise. This means that when it comes to being in an actual conversation, it's hard to respond when someone isn't exactly like the conversation you've memorised. 

This app aims to break this flow, by providing a dynamic, unique conversation with ChatGPT in a certain language. By providing conversation topics and a difficulty scale, users are able to tailor these conversations to talk about anything they want to talk about, at any level of complexity.

Here's an example flow:

I'm learning Spanish, and I want to become familiar with conversations regarding my friends, so that I can tell people about them

1. A message is generated, which tells ChatGPT that I want to have a conversation, in Spanish, about friends, that's at a 'very easy', or 'beginner' level. 
2. The response that comes back is fed into a 'Text to Speech' library, which converts it into an mp3, and is then played. For instance, the response could be 'Hi, my name is John. Tell me about your friends, what do you like to do together?
3. Once this file is finished playing, my audio is recorded as I reply in Spanish. For instance, 'Hi John! My friends and I love to go to the cinema in our spare time. Wnat do you like to do with your friends?
4. This audio is then fed into a 'Speech to Text' API, and then sent back to ChatGPT, where it will respond to the question that  I've asked and ask another one to me.

The beauty about using AI here is that there is no limit to the conversations that can be had. With existing language learning methods, we're relying on either words or phrases that have been defined by someone else. Eventually, we're going to run out of new, unique things, which again means we'll start to memorise a response to a prompt or question, rather than actually answering it. 

With this approach, answering fresh and unique questions forces us to use our knowledge of the language to put a response together, rather then just responding to the prompt. 
 
## Prerequisites
1. You must have an OpenAI key, which has got existing tokens on it. 
2. You must also have ffmpeg installed, which can be found here: https://ffmpeg.org/
3. You must have a version of python 3.12, which can be found here: https://www.python.org/downloads/

## Installation Instructions
1. Install the required python libraries using 'pip install -r requirements.txt'
2. Set your OpenAI Key as an environment variable. For git bash, this could be done using command 'export OPENAI_API_KEY=<KEY>
3. Run the main file using 'python main.py', and the conversation should commence. 


# Future Work
This is very much a proof of concept, which I want to share now so people can consume the idea, and offer suggestions on how to improve it. 

Future work that I plan to add will be: 
- A UI to make it more accessible
- A cleaner installation procedure
- Further customisation of the prompts
- Stability Testing, as I have found that the prompts can sometimes generate an entire conversation rather then just the response that I want
