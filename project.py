from aiBrain import ReplyBrain
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import speedtest
import smtplib 
import pywhatkit
import webbrowser as web
import pyautogui
import webbrowser as web
import keyboard
from keyboard import press_and_release
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # "It will take microphone input from the user and return string"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0)
    try:
        print("Recognizing.....")
        # english = 'en-in' hindi = 'hi'
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")
    except Exception as e:
        print("Say this again please....")
        return "None"
    return query


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning Sir")
    elif (hour >= 12 and hour <= 18):
        speak("Good Afternoon Sir")
    elif (hour >= 18 and hour <= 24):
        speak("Good Evening Sir")
    speak(" I am jarvis...")
    speak("Your personal ai assistance..")
    speak("How may i help you today..")


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "who are you" in query:
            speak("Sir I am jarvis...")
            speak("Your personal ai assistance..")
            speak("How may i help you today..")


        
        elif "how are you" in query:
            speak("I am fine sir...")

        elif "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            print(results)
            speak(results)

        elif 'google' in query:
            speak("Ok!! sir this is what i found on google")
            query = query.replace('google', '')
            query = query.replace("jarvis", "")
            query = query.replace("search","")
            pywhatkit.search(query)
            speak("Done Sir!!")
            results = wikipedia.summary(query,sentences = 1)
            speak(results)

        elif 'open youtube' in query:
            speak('Ok!! sir i am opening youtube')
            webbrowser.open('youtube.com')

        elif 'youtube' in query:
            speak("Ok Sir this is what i found for your search")
            query = query.replace("jarvis", "")
            query = query.replace("search", "")
            query = query.replace("on youtube", "")
            web = "https:///www.youtube.com//results?search_query=" + query
            # webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Ok Done sir!!")

        
        elif "time" in query:
            strTime = datetime.datetime.now().strftime('%H hour %M minute %S secound')
            print(strTime)
            speak(f"Sir,the is {strTime}")

        elif  'over and out' in query:
            speak("Good Byee Sir")
            speak("You can call me anytime sir...just wake me up")
            exit()
        
        elif 'open' in query:
            dictapp = {"commandprompt":"cmd","paint":"paint","word":"winword","excel":
            "excel","chrome":"google","vscode":"code","powerpoint":"powerpnt"}

            keys = list(dictapp.keys())
            for app in keys:
                 if app in query:
                        os.system(f"start {dictapp[app]}")
        
        
        elif "internet speed" in query:
            wifi  = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
            download_net = wifi.download()/1048576
            print("The Upload Speed is", upload_net)
            print("The download speed is ",download_net)
            speak(f"The download speed is {download_net}")
            speak(f"The Upload speed is {upload_net}")

        elif "where is" in query:
            Place = query.replace("where is","")
            Place = query.replace("jarvis","") 
            speak("Sure Sir , Extracting data from google Map")
            ReplyBrain(f"distance between wardha and {Place}")
            speak("I am displaying the best route on screen")
            web.open(f"https://www.google.com/maps/dir/Wardha,+/{Place}")
            

        elif 'open chrome' in query:
            speak('Ok!! sir i am opening chrome')
            webbrowser.open( "C:\Program Files\Google\Chrome\Application\chrome.exe")
        elif 'maximize' in query:
            press_and_release('Windows logo key + Up arrow.')

        elif 'my location' in query:
            from Feature import My_location
            My_location()


        elif 'play music' in query:
            print('Wait a while searching for most played music')
            speak('Wait a while searching for most played music')
            music_dir = 'C:\\Users\\RITIK KISHOR YELANE\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Here is your favourite music Enjoy")
            os.startfile(os.path.join(music_dir, songs[0]))


        elif "Email to harry" in query:
            try:
                speak("What do i say...")
                content = takeCommand()
                to = 'youremail@gmail.com'
                server = smtplib.SMTP('smtp.gmail.com')
                server.ehlo
                server.starttls
                server.login("Yourgamil@gmail.com", 'Your_passward_here')
                server.sendmail("Yourgamil@gmail.com", to, content)
                server.close()
                speak("Your email has been send")
            except Exception as e:
                print("Sorry unable to send email Due to some technical error")


        elif 'website' in query:
            speak("Sure sir launching....")
            query = query.replace('website', '')
            query = query.replace('jarvis', '')
            web2 = query.replace('open', '')
            web1 = "https:///www." + web2 + ".com"
            webbrowser.open(web1)
            speak("opened the result successfully")


        elif 'whatsapp' in query:
            speak("Tell me the name of the person")
            personname = takeCommand()
            if "ishaan" in personname:
                try:
                    speak("Tell me the massage...")
                    msg = int(takeCommand())
                    speak("Please tell me the time so,as i can send message accodingly")
                    speak("The hours is ")
                    hour = int(takeCommand())
                    speak("The minute is ")
                    minute = takeCommand()
                    pywhatkit.sendwhatmsg("8381047320", msg, hour, minute, 20)
                    speak("OK Sir sending the message")
                except Exception as e:
                    print("Sorry i can't send the message")
            else:
                try:
                    speak("Tell me the phone number of the person")
                    phoneno = int(takeCommand())
                    speak("Tell me the massage...")
                    msg = int(takeCommand())
                    speak("Please tell me the time so,as i can send message accodingly")
                    speak("The hours is ")
                    hour = int(takeCommand())
                    speak("The minute is ")
                    minute = takeCommand()
                    pywhatkit.sendwhatmsg(phoneno, msg, hour, minute, 20)
                    speak("OK Sir sending the message")
                except Exception as e:
                    print("Sorry i can't send the message")

        
        elif 'screenshot' in query:
            speak("ok sir ,what should i named the file")
            filename = takeCommand()
            pathname = filename + ".png"
            path = "C:\\Users\\RITIK KISHOR YELANE\\OneDrive\\Pictures\\Screenshots" + pathname
            file = pyautogui.screenshot()
            file.save(path)
            speak("screenshot is been taken and saved to your authorized location")
        
        
        
        elif 'close youtube' in query:
            speak("Ok Sir ,wait a secound")
            os.system("TASKKILL /F /im msedge.exe")
            speak("youtube has been Closde sir...")
        elif 'close music' in query:
            speak("Ok Sir ,wait a secound")
            os.system("TASKKILL /F /im Kbps.mp3")
            speak("music has been Closde sir...")
        elif 'close chrome' in query:
            speak("Ok Sir ,wait a secound")
            os.system("TASKKILL /F /im chrome.exe")
            speak("chrome has been Closde sir...")
        elif 'joke' in query:
            speak("sure sir their i go...")
            getjoke = pyjokes.get_joke()
            speak(getjoke)
        elif 'pause' in query:
            keyboard.press("k")
            speak("Paused")
        elif 'restart' in query:
            keyboard.press('0')
            speak('restared')
        elif 'forward' in query:
            keyboard.press('l')
        elif 'backward' in query:
            keyboard.press('j')
        elif 'play' in query:
            keyboard.press('k')
            speak("Played...")
        elif 'full screen' in query:
            keyboard.press("f")
        

        elif 'location' in query:
            speak("Ok!! finding your all devices currently active")
            webbrowser.open('https://www.google.com/android/find?u=0')
            speak("Thier we go...this are the current active devices linked with me")

        
        elif 'play game' in query:

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


        else:
            speak("Sure Sir....")
            print(ReplyBrain(query))
            speak(ReplyBrain(query))


