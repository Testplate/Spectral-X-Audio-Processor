import os
import sys
import random
import numpy as np
from gtts import gTTS
from pydub import AudioSegment
from pydub.generators import WhiteNoise

def x_filter(samples, sr):
    stft = np.fft.rfft(samples)
    freqs = np.fft.rfftfreq(len(samples), 1/sr)
    mask = np.ones_like(stft, dtype=np.complex64)
    for i in range(len(freqs)):
        if 300 < freqs[i] < 3400:
            shift = np.sin(2 * np.pi * freqs[i] * 0.01) * 0.5
            mask[i] *= np.exp(1j * shift)
        if random.random() < 0.005:
            mask[i] = 0
    return np.fft.irfft(stft * mask).astype(np.float32)

def d_proc(audio):
    s = np.array(audio.get_array_of_samples()).astype(np.float32)
    b = 4
    st = 2 ** (16 - b)
    s = np.round(s / st) * st
    t = np.max(np.abs(s)) * 0.25
    s = np.clip(s, -t, t) * (1.0 / 0.25)
    g = []
    i = 0
    while i < len(s):
        c = random.randint(400, 1800)
        ch = s[i:i+c]
        g.extend(ch)
        if random.random() < 0.12:
            g.extend(ch)
        i += c
    s = x_filter(np.array(g), audio.frame_rate)
    return audio._spawn(s.astype(np.int16).tobytes())

def run(f_in, txt):
    tts = gTTS(text=txt, lang='en')
    tts.save("t.mp3")
    v = AudioSegment.from_file("t.mp3")
    l = AudioSegment.silent(duration=650)
    bg = WhiteNoise().to_audio_segment(duration=15200, volume=-18)
    dv = d_proc(v)
    ib = bg.overlay(dv, position=1200)
    ib = d_proc(ib)[:15200]
    m = AudioSegment.from_file(f_in)
    out = l + ib + m
    o_name = "mod_" + os.path.basename(f_in)
    out.export(o_name, format="mp3")
    if os.path.exists("t.mp3"):
        os.remove("t.mp3")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        p = input().strip().replace("'", "").replace('"', "")
    else:
        p = sys.argv[1]
    t = input()
    run(p, t)
