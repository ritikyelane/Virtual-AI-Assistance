import speech_recognition as sr   
import pyttsx3
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # "It will take microphone input from the user and return string"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in') #english = 'en-in' hindi = 'hi'
        print(f"User Said : {query}\n") 
    except Exception as e:
        print("Say this again please....")
        return "None"
    return query
    
def game_play():

    speak("Let's play rock papaer scissor game sir.... ")
    print("Rock or paper or scissor")
    speak("The rule of the game is simple we will play 5 games....")
    speak("More points at end will win the game peacefully....Let's begain")
    i = 0
    userpoint = 0
    computerpoint = 0
    while(i<5):
       chooce = ('rock','paper','scissor')
       computer_choice = random.choice(chooce)
       user = takeCommand().lower()
       if (user == 'rock'):
        if (computer_choice == 'rock'):
            speak('rock')
            print("Both had the same choice no point to each ")
            speak("Both had the same choice no point to each ")
        elif (computer_choice == 'paper'):
            speak('paper')
            print("I won one point to me")
            speak("I won one point to me")
            computerpoint = computerpoint + 1
            print(f"Score ME :- {userpoint}  :-  JARVIS : {computerpoint}")
        elif (computer_choice == 'scissor'):
            speak('scissor')
            print("OOps...i lost one point to you")
            speak("OOps...i lost one point to you")
            userpoint = userpoint + 1
            print(f"Score ME :- {userpoint}  :  JARVIS :- {computerpoint}")
       elif (user == 'paper'):
        if (computer_choice == 'rock'):
            speak('rock')
            print("OOps...i lost one point to you")
            speak("OOps...i lost one point to you") 
            userpoint = userpoint + 1
            print(f"Score ME :- {userpoint}  :  JARVIS :- {computerpoint}")
        elif (computer_choice == 'paper'):
            speak('paper')
            print("Both had the same choice no point to each ")
            speak("Both had the same choice no point to each ")
        elif (computer_choice == 'scissor'):
            speak('scissor')
            print("I won one point to me") 
            speak("I won one point to me")
            computerpoint = computerpoint + 1
            print(f"Score ME :- {userpoint}  :  JARVIS :- {computerpoint}")
       elif (user == 'scissor'):
        if (computer_choice == 'rock'):
            speak('rock')
            print("I won one point to me")
            speak("I won one point to me")
            computerpoint = computerpoint  + 1 
            print(f"Score ME :- {userpoint}  :  JARVIS :- {computerpoint}") 
        elif (computer_choice == 'paper'):
            speak('paper') 
            print("OOps...i lost one point to you")
            speak("OOps...i lost one point to you")
            userpoint = userpoint +1
            print(f"Score ME :- {userpoint}  :  JARVIS :- {computerpoint}")
        elif (computer_choice == 'scissor'):
            speak('scissor') 
            print("Both had the same choice no point to each ") 
            speak("Both had the same choice no point to each ")
    i += 1
    print(f"The final score are : ME :- {userpoint} : JARVIS :- {computerpoint}")
    speak(f"The final score are : ME :- {userpoint} : JARVIS :- {computerpoint}")


