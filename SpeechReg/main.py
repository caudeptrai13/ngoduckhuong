from SpeechReg.Chatbot import Chatbot
#pip install playsound
simsimi = Chatbot(viet=False)
#Tiếng Việt bị lỗi ở encode utf-8 ở request
simsimi.ask()