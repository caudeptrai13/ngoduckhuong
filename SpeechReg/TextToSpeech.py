from gtts import gTTS

class TextToSpeech:
    def __init__(self,lang="vi"):
        self.lang = lang
    def read(self,text: str):
        self.tts = gTTS(text,lang=self.lang)
    def save(self,file_name: str):
        return self.tts.save(file_name)

