import numpy as np
import matplotlib.pyplot as plt

# Define SNR range in dB
snr_db = np.arange(-2, 18, 0.1)  # From -2 dB to 10 dB
snr_linear = 10 ** (snr_db / 10)  # Convert SNR from dB to linear

# Simplified function to estimate throughput, this is not based on actual data
# The actual performance can vary significantly based on numerous factors
throughput = 1 / (1 + np.exp(-0.3 * (snr_linear - 2)))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(snr_db[snr_db <= 4], throughput[snr_db <= 4], color='blue', linestyle='solid', label='Low SNR', linewidth=2)
plt.plot(snr_db[snr_db > 4], throughput[snr_db > 4], color='red', linestyle='dotted', label='Moderate/High SNR', linewidth=2)
plt.xticks(range(0, 18, 2), fontsize=12)
plt.yticks(fontsize=12)
plt.title(' ')

# Make x-label and y-label bold and increase their size
plt.xlabel('SNR (dB)',fontsize=17)    #fontweight='bold'
plt.ylabel('Throughput (bpcu)', fontsize=17)

plt.legend()
plt.grid(False)
plt.show()
