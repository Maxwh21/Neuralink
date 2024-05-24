import os
import cv2
import matplotlib
matplotlib.use('Agg')  # Use 'Agg' backend for non-interactive plotting
import matplotlib.pyplot as plt

# Function to load, process, and save an image
def process_and_save_image(file_path, output_dir):
    # Load the image
    image = cv2.imread(file_path)
    if image is None:
        print(f"Error loading image: {file_path}")
        return

    # Convert BGR to RGB for matplotlib display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Example processing: Here we just display the image
    # You can add more complex processing here

    # Save the processed image
    output_file_path = os.path.join(output_dir, os.path.basename(file_path))
    plt.figure(figsize=(10, 6))
    plt.imshow(image_rgb)
    plt.title(f'Spectrogram: {os.path.basename(file_path)}')
    plt.axis('off')
    plt.savefig(output_file_path, bbox_inches='tight', pad_inches=0)
    plt.close()

# Function to process each image in the directory
def process_image_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            file_path = os.path.join(input_dir, filename)
            process_and_save_image(file_path, output_dir)

# Example usage
input_directory = 'C:\\Users\\MaxW\\Neuralink\\output\\spectrograms'
output_directory = 'C:\\Users\\MaxW\\Neuralink\\output\\processed_spectrograms'
process_image_directory(input_directory, output_directory)
