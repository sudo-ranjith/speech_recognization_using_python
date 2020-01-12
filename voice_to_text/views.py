from django.shortcuts import render, HttpResponse
import speech_recognition as sr


def home(request):
    return HttpResponse("this is home page")


def speech(request):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("you can speak...... now : ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("you said:::::::: {} ".format(text))
        except Exception as e:
            print("we got exception {}".format(e))
        finally:
            return HttpResponse("YOU SAID:     {}".format(str(text)))
