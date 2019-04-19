from main import Pandorabots
import json
#import speech_recognition as sr

host = 'api.pandorabots.com'
botname = 'rosie'
app_id = 'un4b6a331d'
user_key = 'c86126da2147a35be8cef821924c0c67'
test_filename = 'test.aiml'
botkey = 'JiikqcKNx6CqAJoZWN4PZM-KsaZJqV4kwQYLn35G-KGANbTINfoEhYx1ki5SbvulXzkiNY0_l4o~'

message_dict = {}

#r = sr.Recognizer()

main = Pandorabots(user_key, app_id, host, botname)

print(main.compile_bot().text)

print("########### WELCOME TO MY CHATBOT #############")
print("########### ROSIE WELCOMES YOU ##############\n\n")
print("Enjoy the conversation.")

while True:
    """with sr.Microphone() as source:
        print("You : ")
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        continue
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        continue"""
    print("You : ",end="")
    message = input() #r.recognize_google(audio)
    if message=='zero':
        break
    message_dict['message'] = message
    response_str = main.talk(message_dict).text
    reply = json.loads(response_str)['responses'][0]
    print("Rosie : ",reply)
        
"""while True:
    with sr.Microphone() as source:
        print("You : ",end="")
        audio = r.listen(source)
    print("Message read")
    if audio==None:
        continue
    message = r.recognize_google(audio)
    if(message=='zero'):
        break
    message_dict['message'] = message
    response_str = main.talk(message_dict).text
    reply = json.loads(response_str)['responses'][0]
    print("Rosie : ",reply)"""

