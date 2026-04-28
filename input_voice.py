import speech_recognition as sr

r = sr.Recognizer()

def get_voice_input():
    try:
        with sr.Microphone() as source:
            print("Adjusting for noise... Please wait")
            r.adjust_for_ambient_noise(source, duration=2)

            r.energy_threshold = 300
            r.dynamic_energy_threshold = True
            r.pause_threshold = 1.2
            r.non_speaking_duration = 0.8

            print("Ready. Speak anything (say 'stop' to exit).")

            while True:
                try:
                    audio = r.listen(source)
                except Exception:
                    continue

                print("Processing...")

                text = None  # ✅ prevent crash

                try:
                    text = r.recognize_google(audio).lower()
                    print("Recognized:", text)

                except sr.UnknownValueError:
                    print("Didn't catch that")
                except sr.RequestError:
                    print("API error")

                return text

    except Exception as e:
        print("Error:", e)
        return None