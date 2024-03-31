print("welcome to jarvis desktop assistent ")
print("this code is written by techno solutions ""if you have any orther  quwery based on code comment us on youtube or on insta")
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))


def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")

    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("Jarvis at your service , just tell me how may I help you.")
    print("Jarvis at your service , just tell me how may I help you.")


def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("C:/Users/user/Downloads/maxresdefault.jpeg")
    img.save(img_path)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

        if not query.strip():  # Check if query is empty or contains only whitespace
            return "Try Again"

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query



def open_application(application_name):
    try:
        os.startfile(application_name + ".exe")
    except Exception as e:
        speak("Sorry, I couldn't open that application.")


def math_solver():
    speak("Please tell me the math problem")
    problem = takecommand()
    try:
        result = eval(problem)
        speak(f"The result is {result}")
    except Exception as e:
        speak("Sorry, I couldn't solve that problem.")


def code_generator(topic):
    # Add code generation logic based on the specified topic
    # For demonstration purposes, we'll simply print the topic
    print(f"Generating code for {topic}")
    speak(f"Generating code for {topic}")

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "generate code on" in query:
            topic = query.split("generate code on ")[1]
            code_generator(topic)

        # Other command handlers...


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm JARVIS created by technosolution and I'm a desktop voice assistant.")
            print("I'm JARVIS created by  technosolution and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open google" in query:
            wb.open("google.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            song_dir = os.path.expanduser("~\\Music")
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0, x)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")

        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")

        elif "open web browser" in query:
            wb.open("https://www.google.com")

        elif "open" in query:
            application_name = query.split("open ")[1]
            open_application(application_name)

        elif "solve math" in query:
            math_solver()

        elif "generate code" in query:
            code_generator()

        elif "offline" in query:
            quit()
            # code author techno solutions