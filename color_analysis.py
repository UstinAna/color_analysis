import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# Get the base path of the script
base_path = os.path.dirname(os.path.abspath(__file__))

# Define the folder path where images are stored
folder_path = os.path.join(base_path, 'images')  # Ensure 'image' folder exists in the same directory

# Initialize an empty list to store image file names
image_files = []

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file ends with .png or .jpg (case insensitive)
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_files.append(file_name)

# Check if any image files were found
if not image_files:
    raise ValueError("No image files found in the specified folder.")

# Loop through each image file for color analysis
for i, image_file in enumerate(image_files):
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error loading image: {image_file}")
        continue  # Skip to the next image if there's an error

    # Convert image from BGR to RGB format
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)

    # Number of dominant colors to find
    n_colors = 4

    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(pixels)

    # Extract the dominant colors
    dominant_colors = np.array(kmeans.cluster_centers_, dtype='uint8')
    
    # Calculate the percentage of each color
    percentages = np.unique(kmeans.labels_, return_counts=True)[1] / len(kmeans.labels_)

    # Prepare results for saving
    results = []
    for j, (color, percent) in enumerate(zip(dominant_colors, percentages)):
        result_line = f"Image {i + 1} ({image_file}) - Color {j + 1}: RGB{tuple(color)}, Percentage: {percent:.2%}"
        print(result_line)
        results.append(result_line)

    # Save the results to a text file
    result_path = os.path.join(base_path, 'color_analysis_results.txt')
    with open(result_path, 'a') as file:  # Use 'a' mode to append results for each image
        file.write("\n".join(results) + "\n")

print("Results saved to 'color_analysis_results.txt'")
