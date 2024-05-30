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
- **Value & Count Table**:
```
┏━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Value        ┃ Count ┃
┡━━━━━━━━━━━━━━╇━━━━━━━┩
│ 112          │ 1     │
│ 113          │ 4     │
│ 114          │ 4     │
│ 115          │ 6     │
│ 116          │ 11    │
│ 117          │ 13    │
│ 118          │ 6     │
│ 119          │ 34    │
│ 120          │ 15    │
│ 121          │ 31    │
│ 122          │ 26    │
│ 123          │ 34    │
│ 124          │ 20    │
│ 125          │ 19    │
│ 126          │ 26    │
│ 127          │ 10    │
│ 128          │ 23    │
│ 129          │ 19    │
│ 130          │ 12    │
│ 131          │ 1     │
│ 132          │ 10    │
│ 133          │ 2     │
│ 134          │ 1     │
│ 135          │ 3     │
│ 136          │ 14    │
│ 137          │ 20    │
│ 138          │ 9     │
│ 139          │ 1     │
│ 140          │ 3     │
│ 141          │ 12    │
│ 142          │ 2     │
│ 143          │ 19    │
│ 144          │ 3     │
│ 145          │ 8     │
│ 146          │ 10    │
│ 147          │ 12    │
│ 148          │ 4     │
│ 149          │ 23    │
│ 150          │ 14    │
│ 151          │ 5     │
│ 152          │ 36    │
│ 153          │ 38    │
│ 154          │ 45    │
│ 155          │ 48    │
│ 156          │ 64    │
│ 157          │ 89    │
│ 158          │ 88    │
│ 159          │ 60    │
│ 160          │ 36    │
│ 161          │ 15    │
│ 162          │ 7     │
│ 163          │ 6     │
│ 164          │ 2     │
└──────────────┴───────┘
```
- **Pixel Intensity, CDF(v), Equalized v Table**:
```
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Pixel Intensity  ┃ CDF(v) ┃ Equalized v ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━┩
│ 112              │ 1      │ 0           │
│ 113              │ 5      │ 1           │
│ 114              │ 9      │ 2           │
│ 115              │ 15     │ 3           │
│ 116              │ 26     │ 6           │
│ 117              │ 39     │ 9           │
│ 118              │ 45     │ 11          │
│ 119              │ 79     │ 19          │
│ 120              │ 94     │ 23          │
│ 121              │ 125    │ 31          │
│ 122              │ 151    │ 37          │
│ 123              │ 185    │ 46          │
│ 124              │ 205    │ 51          │
│ 125              │ 224    │ 56          │
│ 126              │ 250    │ 62          │
│ 127              │ 260    │ 65          │
│ 128              │ 283    │ 70          │
│ 129              │ 302    │ 75          │
│ 130              │ 314    │ 78          │
│ 131              │ 315    │ 78          │
│ 132              │ 325    │ 81          │
│ 133              │ 327    │ 81          │
│ 134              │ 328    │ 82          │
│ 135              │ 331    │ 82          │
│ 136              │ 345    │ 86          │
│ 137              │ 365    │ 91          │
│ 138              │ 374    │ 93          │
│ 139              │ 375    │ 93          │
│ 140              │ 378    │ 94          │
│ 141              │ 390    │ 97          │
│ 142              │ 392    │ 97          │
│ 143              │ 411    │ 102         │
│ 144              │ 414    │ 103         │
│ 145              │ 422    │ 105         │
│ 146              │ 432    │ 107         │
│ 147              │ 444    │ 110         │
│ 148              │ 448    │ 111         │
│ 149              │ 471    │ 117         │
│ 150              │ 485    │ 121         │
│ 151              │ 490    │ 122         │
│ 152              │ 526    │ 131         │
│ 153              │ 564    │ 140         │
│ 154              │ 609    │ 152         │
│ 155              │ 657    │ 164         │
│ 156              │ 721    │ 179         │
│ 157              │ 810    │ 202         │
│ 158              │ 898    │ 224         │
│ 159              │ 958    │ 239         │
│ 160              │ 994    │ 248         │
│ 161              │ 1009   │ 251         │
│ 162              │ 1016   │ 253         │
│ 163              │ 1022   │ 255         │
│ 164              │ 1024   │ 255         │
└──────────────────┴────────┴─────────────┘
```
## 🙏 Acknowledgements

- [pandas](https://pandas.pydata.org/)
- [rich](https://rich.readthedocs.io/)

Feel free to reach out if you have any questions or need further assistance!
