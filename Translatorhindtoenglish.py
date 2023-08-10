import speech_recognition as sr 
from googletrans import Translator

def takeCommandHtoE():
    # "It will take microphone input from the user and return string"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizing.....")
        query = r.recognize_google(audio,language='hi') #english = 'en-in' hindi = 'hi'
        print(f"User Said : {query}\n") 
    except Exception as e:
        print("Say this again please....")
        return "None"
    return query


def translateHtoE(text):
    line = str(text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}") 

def MicExceution():
    data = takeCommandHtoE()
    query = translateHtoE(data)
    return query

MicExceution()

