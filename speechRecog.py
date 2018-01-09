import pyaudio
import speech_recognition as sr
import wave
import commandParse as cp

def recAudio():
    FORMAT = pyaudio.paInt16
    CONST_CHANNELS = 2
    CONST_RATE = 44100
    CONST_CHUNK = 2048
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "file.wav"
    AUDIO_FILE = WAVE_OUTPUT_FILENAME
    r = sr.Recognizer()

    audio = pyaudio.PyAudio()

    
    stream = audio.open(format=FORMAT, channels=CONST_CHANNELS,
                    rate=CONST_RATE, input=True,
                    frames_per_buffer=CONST_CHUNK)
    print "speech recording...."
    frames_rec = []

    for i in range(0, int(CONST_RATE / CONST_CHUNK * RECORD_SECONDS)):
        data = stream.read(CONST_CHUNK)
        frames_rec.append(data)
    print "Finished Recording"

    
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CONST_CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(CONST_RATE)
    waveFile.writeframes(b''.join(frames_rec))
    waveFile.close()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        print("You said:"+ text)
    except sr.RequestError as e:
        print("Could not request result from Google Speech Recognition service; {0}".format(e))

    return text

text = recAudio()
cp.parse(text)
