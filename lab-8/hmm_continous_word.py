import numpy as np
from hmmlearn import hmm
import scipy.io.wavfile as wav
import speech_recognition as sr

# create a speech recognizer object
r = sr.Recognizer()

# load the speech signal
with sr.AudioFile('lab8/speech.wav') as source:
    audio = r.record(source)

# extract the Mel-Frequency Cepstral Coefficients (MFCCs)
from python_speech_features import mfcc
signal, sample_rate = wav.read("speech.wav")
mfcc_features = mfcc(signal, sample_rate)

# define the set of words to recognize
words = ['hello', 'world', 'python']

# train an HMM model for each word
models = {}
for word in words:
    # extract the training data for this word
    word_features = [mfcc_features[i] for i in range(len(mfcc_features)) if i % len(words) == words.index(word)]
    # define the HMM model
    num_states = 5
    num_features = mfcc_features.shape[1]
    model = hmm.GaussianHMM(n_components=num_states, covariance_type="diag")
    model.fit(word_features)
    # store the model for this word in the dictionary
    models[word] = model

# perform continuous speech recognition
with sr.Microphone() as source:
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    # listen for audio and convert it to text
    while True:
        audio = r.listen(source)
        try:
            # extract the MFCC features from the audio signal
            signal = np.frombuffer(audio.frame_data, dtype=np.int16)
            mfcc_features = mfcc(signal, sample_rate)
            # recognize the word using the HMM model
            log_probabilities = []
            for word in words:
                word_model = models[word]
                log_probabilities.append(word_model.score(mfcc_features))
            recognized_word = words[np.argmax(log_probabilities)]
            print("You said: {}".format(recognized_word))
        except sr.UnknownValueError:
            print("Could not understand audio")
