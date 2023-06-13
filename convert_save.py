import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Path to the folder containing FLAC files
folder_path = '/path/to/flac/files/'

# Create a folder to save the spectrograms
save_folder = os.path.join(folder_path, 'spct')
os.makedirs(save_folder, exist_ok=True)

# Iterate through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.flac'):
        # Load the audio file
        file_path = os.path.join(folder_path, file_name)
        audio, sr = librosa.load(file_path)

        # Compute the spectrogram
        spectrogram = librosa.stft(audio)
        spectrogram_db = librosa.amplitude_to_db(abs(spectrogram))

        # Plot the spectrogram
        plt.figure()
        librosa.display.specshow(spectrogram_db, sr=sr, x_axis='time', y_axis='log')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Spectrogram')

        # Save the spectrogram as an image
        save_path = os.path.join(save_folder, file_name.replace('.flac', '.png'))
        plt.savefig(save_path)
        plt.close()
