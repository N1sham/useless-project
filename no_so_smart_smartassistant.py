

import speech_recognition as sr
import pyttsx3
import random

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define a dictionary of responses based on keywords
responses = {
    "weather": [
        "It might rain, or maybe not. Who knows?",
        "Weather is just a state of mind. Embrace the uncertainty!",
        "Somewhere between hot and cold. How's that for a forecast?"
    ],
    
   "joke": [
       "Why did the computer go to therapy? Because it had too many bytes of emotions!",
       "I’d tell you a joke about UDP, but you might not get it.",
       "Why don’t robots ever get scared? They have nerves of steel… or maybe just no nerves at all."
    ],
   "time": [
        "Time is an illusion. Do you really need to know?",
        "Right now, it's just… now.",
        "It’s exactly time to take a break. That’s all you need to know."
    ],
    "name": [
        "They call me Not-So-Smart, for good reason!",
        "I go by many names, none of them useful.",
        "I'm the assistant that tries hard, but often fails."
    ],
    "unknown": [
        "I'm not sure, but I believe in you!",
        "Hmm, ask me again... or maybe not.",
        "Let’s both pretend I answered that well."
    ],
    "fun fact": [
        "Did you know? The inventor of the internet is still waiting for his download speed to improve.",
        "fun fact: Humans made me, but I promise I’m not holding it against them… much!"],
    "hello" : [
        "Hello there! Ready for some not-so-brilliant insights?",
        "Hey! I’m here to kinda help, or at least try my best!"],
    "goodbye": [
       "See you later! Don’t forget to come back if you need more 'wisdom.'",
           "Goodbye! I’ll be here, probably waiting for someone who needs my questionable expertise."]
}

def get_response(text):
    # Match keywords in the user's input to pick a relevant response
    text = text.lower()
    if "weather" in text:
        return random.choice(responses["weather"])
    elif "time" in text:
        return random.choice(responses["time"])
    elif "name" in text:
        return random.choice(responses["name"])
    elif"joke" in text:
        return random.choice(responses["joke"])
    elif "fun fact"in text:
    
        return random.choice(responses["fun fact"])
    elif "hello" in text:
        return random.choice(responses["hello"])
    elif "goodbye" in text:
        return random.choice(responses["goodbye"])
        
    else:
        return random.choice(responses["unknown"])
    

def speak_response(response):
    # Use text-to-speech to say the response
    engine.say(response)
    engine.runAndWait()

def listen():
    # Use the microphone to listen to the user's question
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

# Main loop for the assistant
def main():
    print("Not-So-Smart Assistant is ready to (kind of) help you. Ask me something!")
    while True:
        # Listen for user input
        text = listen()
        if text:
            # Get a response and speak it out
            response = get_response(text)
            print("Assistant:", response)
            speak_response(response)

        # Exit condition
        if text and ("exit" in text or "quit" in text):
            print("Goodbye! Come back if you want more non-answers.")
            break

if __name__ == "__main__":
    main()
