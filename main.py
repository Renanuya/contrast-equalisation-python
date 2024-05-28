import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('data/example_data.xlsx', header=None)
data_values = data.values

hist, bins = np.histogram(data_values.flatten(), bins=256, range=[0,256])
cdf = hist.cumsum()  # Cumulative distribution function (CDF)

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

equalized_data = cdf[data_values]

# Create tables of pixel value and frequency
unique, counts = np.unique(data_values, return_counts=True)
freq_table = pd.DataFrame({'Value': unique, 'Count': counts})

cdf_table = pd.DataFrame({
    'Pixel Intensity': np.arange(256),
    'CDF': cdf,
    'Equalized Value': cdf
})

# Visualization
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Original Image
axs[0, 0].imshow(data_values, cmap='gray', vmin=0, vmax=255)
axs[0, 0].set_title('Original Data')
axs[0, 0].axis('off')

# Original Image Matrix
axs[0, 1].axis('off')
table_0 = axs[0, 1].table(cellText=data_values, loc='center', cellLoc='center', fontsize=10)
axs[0, 1].set_title('Original Data As Matrix', pad=75)

# Pixel Value and Frequency Table
axs[1, 0].bar(freq_table['Value'], freq_table['Count'])
axs[1, 0].set_title('Original Pixel Values and Frequencies')
axs[1, 0].set_xlabel('Pixel Value')
axs[1, 0].set_ylabel('Frequency')

# CDF and Equalized Value Table
axs[1, 1].hist(equalized_data.flatten(), bins=256, alpha=0.5, color='blue', label='Equalized Data')
axs[1, 1].set_title('Equalized Pixel Values and Frequencies')
axs[1, 1].set_xlabel('Pixel Value')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].legend()

# Equalized Image
axs[2, 0].imshow(equalized_data, cmap='gray', vmin=0, vmax=255)
axs[2, 0].set_title('Equalized Data')
axs[2, 0].axis('off')

# Equalized Image Matrix
axs[2, 1].axis('off')
table_1 = axs[2, 1].table(cellText=equalized_data, loc='center', cellLoc='center', fontsize=10)
axs[2, 1].set_title('Equalized Data Matrix', pad=75)

plt.tight_layout()
plt.show()
