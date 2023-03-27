import numpy as np
from hmmlearn import hmm
import scipy.io.wavfile as wav

# load the speech signal
sample_rate, signal = wav.read('speech.wav')

# extract the Mel-Frequency Cepstral Coefficients (MFCCs)
from python_speech_features import mfcc
mfcc_features = mfcc(signal, sample_rate)

# define the HMM model
num_states = 5
num_features = mfcc_features.shape[1]
model = hmm.GaussianHMM(n_components=num_states, covariance_type="diag")

# train the HMM model
model.fit(mfcc_features)

# define the set of words to recognize
words = ['hello', 'world', 'python']

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
            signal = audio.get_array_of_samples()
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