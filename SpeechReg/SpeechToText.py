import speech_recognition as sr
import keyboard
class SpeechToText:
    def __init__(self,lang="en-US"):
        self.mic = sr.Microphone(device_index=1)
        self.recognizer = sr.Recognizer()
        self.lang = lang
    def listener(self,time):
        while(True):
            try:
                with self.mic as source:
                    print("Listening...")
                    self.recognizer.adjust_for_ambient_noise(source)
                    audio = self.recognizer.listen(source=source,timeout=time)
                print("Stop listened")
                return str(self.recognizer.recognize_google(audio,language=self.lang))
                break
            except sr.WaitTimeoutError:
                print("TimeoutError")
                print("Press Enter to continue or \"S\" to Stop")
                while(True):
                    if keyboard.is_pressed('enter'):
                        break
            except sr.RequestError as e:
                print("Could not request results from Wit.ai service; {0}".format(e))
                print("Press Enter to continue or \"S\" to Stop")
                while (True):
                    if keyboard.is_pressed('enter'):
                        break
            except sr.UnknownValueError:
                print("Cannot understand")
                print("Press Enter to continue or \"S\" to Stop")
                while (True):
                    if keyboard.is_pressed('enter'):
                        break
