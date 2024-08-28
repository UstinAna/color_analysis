Here is a `README.md` file that you can use for your project:

---

# Color Analysis Project

This project is designed to analyze the dominant colors in images using K-Means clustering. The script processes multiple images within a specified folder and generates a report detailing the dominant colors and their respective percentages.

## Features

- **Processes multiple images:** The script automatically detects and processes all `.png`, `.jpg`, and `.jpeg` files within the specified folder.
- **Color analysis using K-Means clustering:** The script identifies the dominant colors in each image and calculates their percentage presence.
- **Result visualization:** The script displays the dominant colors visually and saves the results to a text file.

## Requirements

To run this project, you'll need to install the necessary Python libraries. You can do this by running:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes the following libraries:

- `opencv-python==4.8.0.74`
- `numpy==1.24.4`
- `matplotlib==3.8.0`
- `scikit-learn==1.3.0`

## Usage

### 1. Prepare Your Images

Place your `.png`, `.jpg`, or `.jpeg` images in the `images` folder located in the same directory as the script.

### 2. Run the Script

To perform the color analysis, run the `color_analysis.py` script:

```bash
python color_analysis.py
```

### 3. Review the Results

The results of the color analysis will be saved in a `color_analysis_results.txt` file located in the same directory. Each image's dominant colors and their percentages will be listed.

### Example Output

The `color_analysis_results.txt` file will contain entries like the following:

```
Image 1 (bizcafe_sidebar_bg_color.png) - Color 1: RGB(213, 233, 238), Percentage: 100.00%
Image 2 (bizcafe_menu.png) - Color 1: RGB(254, 254, 254), Percentage: 65.63%
Image 2 (bizcafe_menu.png) - Color 2: RGB(211, 231, 236), Percentage: 30.22%
Image 2 (bizcafe_menu.png) - Color 3: RGB(57, 100, 112), Percentage: 1.74%
Image 2 (bizcafe_menu.png) - Color 4: RGB(147, 172, 179), Percentage: 2.41%
```

## License

This project is open-source and free to use.

## Contributions

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to submit a pull request or open an issue.

## Contact

If you have any questions or need further assistance, feel free to reach out.

---

This `README.md` provides a clear overview of the project, instructions for setting it up, and details on how to use it. Let me know if you need any further customization!
