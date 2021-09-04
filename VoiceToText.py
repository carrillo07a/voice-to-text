import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()


# Audio output
def SpeekText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while (1):
    try:
        # Activate microphone
        with sr.Microphone() as source:
            # Get the audio
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)

            # Convert audio to text
            recognize_google_text = recognizer.recognize_google(audio, language="es-ES")
            google_text = recognize_google_text.lower()
            print("Google Text: " + google_text.lower())

            # Convert Text to Audio
            SpeekText(google_text)
    except sr.RequestError as e:
        print("No Result; {0}".format(e))

    except sr.UnknownValueError as e:
        print("Error" + str(e))
