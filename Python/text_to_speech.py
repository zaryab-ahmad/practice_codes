# Import the required module for text to speech conversion
import pyttsx3

def text_to_speech(text):
    """
    This function takes a string of text and converts it into speech.
    
    :param text: The text to be converted to speech.
    :type text: str
    """
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Set properties _before_ you add things to say
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.8)  # Volume 0-1

    # Add text to speech
    engine.say(text)

    # Run the text to speech engine
    engine.runAndWait()



def text_to_speech2(text):
    """
    This function takes a string of text and converts it into speech.
    
    :param text: The text to be converted to speech.
    :type text: str
    """
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Set properties _before_ you add things to say
    engine.setProperty('rate', 140)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.6)  # Volume 0-1

    # Add text to speech
    engine.say(text)

    # Run the text to speech engine
    engine.runAndWait()


# Test the function
text_to_speech("Hello, how are you?")

text_to_speech2(" i am fine my name is zaryab what is your name ")