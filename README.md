# 📊 Contrast Equalisation Script

This repository contains a Python script for performing contrast equalisation on image data stored in an Excel file.

## 📋 Table of Contents
- [📖 Description](#-description)
- [✨ Features](#-features)
- [🛠️ Requirements](#-requirements)
- [💾 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📝 Example](#-example)
- [🙏 Acknowledgements](#-acknowledgements)

## 📖 Description

The script reads image data from an Excel file, performs contrast equalisation to enhance the image, and prints the processed image data in a tabular format using the `rich` library. Contrast equalisation is a technique that improves the contrast of an image by adjusting the pixel intensity values based on their cumulative distribution function (CDF).

## ✨ Features

- Reads image data from an Excel file.
- Calculates histogram and CDF of the pixel values.
- Performs contrast equalisation on the pixel values.
- Displays the histogram, CDF, and equalised pixel values using the `rich` library.

## 🛠️ Requirements

- Python 3.x
- pandas
- rich

## 💾 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Renanuya/contrast-equalisation-python.git
   cd contrast-equalisation-script
   ```

2. Install the required Python packages:
   ```sh
   pip install pandas rich
   ```

## 🚀 Usage

1. Place your input Excel file (`example_data.xlsx`) in the `data` directory.

2. Run the script:
   ```sh
   python main.py
   ```

3. The script will process the data and display the histogram, CDF, and equalised pixel values in a tabular format in the console.

## 📝 Example

When the script is executed, the following tables will be generated:
- **Value & Count Table**: Displays the original pixel values and their counts.
- **Pixel Intensity, CDF(v), Equalized v Table**: Displays the pixel intensity, CDF values, and the equalised pixel values.

## 🙏 Acknowledgements

- [pandas](https://pandas.pydata.org/)
- [rich](https://rich.readthedocs.io/)

Feel free to reach out if you have any questions or need further assistance!
