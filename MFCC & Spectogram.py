import os
import numpy as np
import wave
import librosa
import librosa.display
import matplotlib
matplotlib.use('Agg')  # Use 'Agg' backend for non-interactive plotting
import matplotlib.pyplot as plt

# Load data
def load_wav(file_path):
    with wave.open(file_path, 'r') as wav_file:
        n_channels, sampwidth, framerate, n_frames, comptype, compname = wav_file.getparams()
        frames = wav_file.readframes(n_frames)
        data = np.frombuffer(frames, dtype=np.int16)
    return data, framerate

# Function to create and plot spectrogram
def plot_spectrogram(data, sr, title, output_dir):
    # Normalize the data
    data = data.astype(float) / np.max(np.abs(data))
    
    # Generate spectrogram
    S = librosa.stft(data)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

    # Plot the spectrogram
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Spectrogram - {title}')
    plt.savefig(os.path.join(output_dir, f'{title}_spectrogram.png'))
    plt.close()

# Function to create and plot MFCCs
def plot_mfcc(data, sr, title, output_dir):
    # Normalize the data
    data = data.astype(float) / np.max(np.abs(data))
    
    # Generate MFCCs
    mfccs = librosa.feature.mfcc(y=data, sr=sr, n_mfcc=13)

    # Plot MFCCs
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(mfccs, sr=sr, x_axis='time')
    plt.colorbar()
    plt.title(f'MFCC - {title}')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'{title}_mfcc.png'))
    plt.close()

# Process each WAV file in the directory
def process_directory(directory, spectrogram_output_dir, mfcc_output_dir):
    if not os.path.exists(spectrogram_output_dir):
        os.makedirs(spectrogram_output_dir)
    if not os.path.exists(mfcc_output_dir):
        os.makedirs(mfcc_output_dir)
    for filename in os.listdir(directory):
        if filename.endswith('.wav'):
            file_path = os.path.join(directory, filename)
            data, sr = load_wav(file_path)
            plot_spectrogram(data, sr, filename, spectrogram_output_dir)
            plot_mfcc(data, sr, filename, mfcc_output_dir)

# Example usage
process_directory('C:\\Users\\MaxW\\Neuralink\\data\\data', 
                  'C:\\Users\\MaxW\\Neuralink\\output\\spectrograms', 
                  'C:\\Users\\MaxW\\Neuralink\\output\\mfccs')
