import requests
from SpeechReg.SpeechToText import SpeechToText
from SpeechReg.TextToSpeech import TextToSpeech
from playsound import playsound
class Chatbot:
    def __init__(self,viet : bool):
        self.lang = "vi" if viet else "en"
        self.stt = SpeechToText("vi-VN" if viet else "en-US")
        self.tts = TextToSpeech(self.lang)
        self.headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'x-api-key': r"0pG.bT9NE-I6HUhQOD7VvgbLJOkZPe22LSPeyWab"
        }
    def makeRequest(self,text:str):
        data = '{\n            "utext": \"' + text + '\", \n            "lang": \"'+ self.lang +'\"\n     }'
        response = requests.post('https://wsapi.simsimi.com/190410/talk', headers=self.headers, data=data.encode('utf-8'))
        answer = response.json()['atext']
        self.tts.read(answer)
        self.tts.save('answer.mp3')
        return answer
    def ask(self):
        audio = self.stt.listener(time=3)
        print("You said : ", audio)
        answer = self.makeRequest(text=audio)
        print("Simsimi said : ", answer)
        playsound('answer.mp3')

