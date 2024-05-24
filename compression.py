import numpy as np
import wave
import zlib
from scipy.signal import butter, lfilter

# Preprocessing: Band-pass filter
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Load data
def load_wav(file_path):
    with wave.open(file_path, 'r') as wav_file:
        n_channels, sampwidth, framerate, n_frames, comptype, compname = wav_file.getparams()
        frames = wav_file.readframes(n_frames)
        data = np.frombuffer(frames, dtype=np.int16)
    return data, framerate

# Delta encoding
def delta_encode(data):
    return np.diff(data, prepend=data[0])

# Entropy encoding using zlib
def entropy_encode(data):
    return zlib.compress(data)

# Full compression pipeline
def compress(file_path):
    data, fs = load_wav(file_path)
    filtered_data = bandpass_filter(data, 300, 3000, fs)  # Example filter range
    delta_encoded = delta_encode(filtered_data)
    compressed_data = entropy_encode(delta_encoded.tobytes())
    return compressed_data

# Example usage
compressed_data = compress('C:\\Users\\MaxW\\Neuralink\\data\\data\\00d4f842-fc92-45f5-8cae-3effdc2245f5.wav')
print(f'Compressed size: {len(compressed_data)} bytes')
