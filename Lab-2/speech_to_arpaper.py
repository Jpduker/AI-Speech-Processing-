import cmudict
import speech_recognition as sr

r = sr.Recognizer()

def to_arpabet(sentence):
    arpabet = cmudict.dict()
    words = sentence.split()

    arpabet_sentence = []
    for word in words:
        if word in arpabet:
            arpabet_word = arpabet[word][0]
            arpabet_sentence.append(" ".join(arpabet_word))
        else:
            arpabet_sentence.append(word)
    return " ".join(arpabet_sentence)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) 
    print("Say Some Sentence !!")
    audio_text = r.listen(source,2,4)
    print("Done")
    Sentence = r.recognize_google(audio_text, language ='en-US')

print("Sentence: ", Sentence)
print("Arbabet Format: " , to_arpabet(Sentence))