#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess

SetLogLevel(0)

sample_rate=16000
model = Model("model")
rec = KaldiRecognizer(model, sample_rate)

process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                            'clnsp1007.wav',
                            '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                            stdout=subprocess.PIPE)

file=open("speech_text.txt", "w+")


while True:
    data = process.stdout.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        pass
        print(rec.Result())
        # file.write(rec.Result() + " ")
    # else:
        # print(rec.PartialResult())
        # file.write(rec.PartialResult()+" ")

# print(rec.FinalResult())
file.write(rec.FinalResult() + " ")
