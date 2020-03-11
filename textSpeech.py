import speech_recognition as sr

r1 = sr.Recognizer()

with sr.Microphone() as source:
    print('speack something')
    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
       print('cant regonize your voice') 
    
