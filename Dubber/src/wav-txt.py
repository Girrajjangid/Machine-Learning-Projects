import speech_recognition as sr
from pydub import AudioSegment

audio = AudioSegment.from_file('../audio/sample.wav')
audio = audio[20000:60000]
audio.export('../audio/chunk.wav', format='wav')

r = sr.Recognizer()

with sr.AudioFile('../audio/chunk.wav') as source:
	r.adjust_for_ambient_noise(source)
	audio = r.record(source)

print(r.recognize_google(audio))