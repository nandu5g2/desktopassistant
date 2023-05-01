import datetime
import pyttsx3
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def out():
    speak("session terminated")


def wishme():
    hour =int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("good morning!")
       
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else :
        speak("good night")
    speak("i am jarvis ! how may help you")


    

def takecommand():
    #microphone input

    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        speak("you may speak now")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing.....")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
        speak(query)
      
    
    except Exception as e:
        print(e)
        speak("could you please say that again")
        print("say that again please....")
        return "None"
    return query

def searchcommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        speak("Say something!")
        audio = r.listen(source)

    
    try:
        text = r.recognize_google(audio)
        speak("searching for: " + text)
    # search in google
        search_url = "https://www.google.com/search?q=" + text
        webbrowser.open(search_url)
    except sr.UnknownValueError:
        speak("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def searchyoutube():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        speak("alright what to search!")
        audio = r.listen(source)
    

# Record the speech and convert to text
    
    try:
        query = r.recognize_google(audio)
        print("You said: ", query)
    
    # Search for the query on YouTube
        pywhatkit.playonyt(query)
    
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Sorry, the speech recognition service is currently unavailable. Error: ", e)

    
    
 
 


if __name__ =="__main__":

  
    wishme()
    
    
    
    while True:
         
         query = takecommand().lower()
         
         if'search youtube'in query:
             speak("opening youtube")
             searchyoutube()
             break
            
         if'google search'in query:
             searchcommand()

         if'lamda'in query:
             speak("opening youtube")
             webbrowser.open("youtube.com")
                 
        
        
         # logic for exectuing tasks
         if 'wikipedia' in query:
        
             speak("searching in wikepedia....")
             query = query.replace('wikipedia',"")
             results =wikipedia.summary(query, sentences=2)
          
             speak("according to wikipedia"+results)
         
         elif 'time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M")
             print(strTime)
             speak(strTime )

         

         

         if "date and day" in query:
             #for date
             strDate =datetime.date.today()
             speak("it's")
             speak(strDate )
             
             #for day
             strDay = strDate.strftime('%A')
             speak("today is")
             speak(strDay)
             

         elif "date" in query:
             strDate =datetime.date.today()
             
             speak("it is")
             speak(strDate)
        
         elif "day" in query:
            strDate =datetime.date.today()
            strDay = strDate.strftime('%A')
            speak("today is")
            speak(strDay)
             
             
             
             

        
             

        
             

    
            

            
       

         elif'shutdown' in query:
             speak("moving out! good bye sir")  
             out() 
             break
      
 



        
       

     
    
   
   
