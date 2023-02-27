import speech_recognition as sr
import eng_to_ipa as P

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) 
    print("Say Some Sentence !!")
    audio_text = r.listen(source,2,4)
    print("Done")
    Sentence = r.recognize_google(audio_text, language ='en-US')

print("Photetics: " + P.convert(Sentence))
print(" ")
print("Possible Transcriptions: " , P.ipa_list(Sentence))
print(" ")
print("List of Rhymes: " , P.get_rhymes(Sentence))