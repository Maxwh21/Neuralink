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

# Function to create and plot spectrogram
def plot_spectrogram(file_path):
    data, sr = load_wav(file_path)
    # Normalize the data
    data = data.astype(float) / np.max(np.abs(data))
    
    # Generate spectrogram
    S = librosa.stft(data)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

    # Plot the spectrogram
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.show()

# Example usage
plot_spectrogram('C:\\Users\\MaxW\\Neuralink\\data\\data\\00d4f842-fc92-45f5-8cae-3effdc2245f5.wav')
