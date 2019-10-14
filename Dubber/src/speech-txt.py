import speech_recognition as sr

# setting up recognizer
r = sr.Recognizer()

# # get audio from microphone
# with sr.Microphone() as source:
# 	print('Bol na do zara:')
# 	audio = r.listen(source)

with sr.AudioFile('../audio/voice.wav') as source:
	# r.adjust_for_ambient_noise(source)
	audio = r.record(source)

# recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))