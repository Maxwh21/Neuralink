import numpy as np
import wave
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load data
def load_wav(file_path):
    with wave.open(file_path, 'r') as wav_file:
        n_channels, sampwidth, framerate, n_frames, comptype, compname = wav_file.getparams()
        frames = wav_file.readframes(n_frames)
        data = np.frombuffer(frames, dtype=np.int16)
    return data, framerate

# Function to create and plot MFCCs
def plot_mfcc(file_path):
    data, sr = load_wav(file_path)
    # Normalize the data
    data = data.astype(float) / np.max(np.abs(data))
    
    # Generate MFCCs
    mfccs = librosa.feature.mfcc(y=data, sr=sr, n_mfcc=13)

    # Plot MFCCs
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(mfccs, sr=sr, x_axis='time')
    plt.colorbar()
    plt.title('MFCC')
    plt.tight_layout()
    plt.show()

# Example usage
plot_mfcc('C:\\Users\\MaxW\\Neuralink\\data\\data\\00d4f842-fc92-45f5-8cae-3effdc2245f5.wav')
