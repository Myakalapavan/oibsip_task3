import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 140)

# Function to speak text aloud
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Function to capture voice commands from the user
def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Try saying things like 'what's the time' or 'search Python'.")
        return ""
    except sr.RequestError:
        speak("Sorry, speech service is currently unavailable.")
        return ""

# Main logic of the assistant
def run_assistant():
    speak("Hello! How can I help you today?")
    while True:
        command = get_command()

        if command == "":
            continue  
        if "hello" in command:
            speak("Hi there! How are you?")
        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")
        elif "date" in command or "day" in command or "today" in command:
            date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            speak(f"Today is {date}")
        elif "search" in command:
            topic = command.replace("search", "").strip()
            if topic:
                speak(f"Searching for {topic} on the web...")
                pywhatkit.search(topic)
            else:
                speak("Please say what you'd like me to search.")
        elif "stop" in command or "exit" in command or "goodbye" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm not sure how to help with that yet.")

# Run the assistant
run_assistant()
