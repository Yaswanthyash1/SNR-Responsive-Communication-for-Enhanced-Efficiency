import numpy as np
import matplotlib.pyplot as plt

# Extending SNR range from -5 to 50 dB
snr_db_extended = np.linspace(-5, 50, 200)
snr_lin_extended = 10 ** (snr_db_extended / 10)

# Simplified throughput model for extended SNR
# Without soft combining
throughput_no_combining_extended = 1 - np.exp(-snr_lin_extended / 10)

# With IR and soft combining, assume a better performance especially at higher SNR
throughput_with_combining_extended = 1 - np.exp(-snr_lin_extended / 3)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(snr_db_extended, throughput_no_combining_extended, label='Without Soft Combining', color='red')
plt.plot(snr_db_extended, throughput_with_combining_extended, label='With Soft Combining', color='blue', linestyle='dashdot')
plt.xlabel('SNR (dB)',  fontsize=17)
plt.ylabel('Throughput', fontsize=17)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12 ) #fontweight='bold'
plt.title('')
plt.legend()
plt.grid(False)
plt.show()
