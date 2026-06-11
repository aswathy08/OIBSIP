import speech_recognition as sr
import pyttsx3
import datetime

def speak(text):
    print(f"Assistant: {text}")
    engine = pyttsx3.init('sapi5')   # fresh engine each time
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def main():
    speak("Hello Aswathi, I am ready.")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How are you?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}")
        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
