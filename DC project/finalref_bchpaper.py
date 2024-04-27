import numpy as np
import matplotlib.pyplot as plt
import math

def average_percentage_increase(throughput1, throughput2, SNR_values, start_SNR, end_SNR):
    # Find start and end indices in the SNR_values array
    start_index = np.searchsorted(SNR_values, start_SNR)
    end_index = np.searchsorted(SNR_values, end_SNR)
    
    # Ensure that the end index is within the array bounds
    end_index = min(end_index, len(SNR_values) - 1)
    
    # Extract the relevant ranges of throughput values
    throughput1_range = throughput1[start_index:end_index ]
    throughput2_range = throughput2[start_index:end_index ]
    
    # Calculate the percentage increase at every step
    percentage_increases = ((np.array(throughput2_range) - np.array(throughput1_range)) / np.array(throughput1_range)) * 100
    
    # Calculate the average of the percentages
    average_increase = np.mean(percentage_increases)
    
    print(f"Average percentage increase from throughput1 to throughput2 from SNR {start_SNR} dB to {end_SNR} dB is {average_increase:.2f}%")

# Example usage
# average_percentage_increase(throughput_GBN_values, throughput_HARQ1_values, SNR_dB, 5, 15)



# Parameters
N = 511  # Length of RS code word
K_GBN = 383  # Count of information symbols for HARQ scheme 1
K_HARQ1 = 383  # Count of information symbols for HARQ scheme 1
K_HARQ2 = 255  # Count of information symbols for HARQ scheme 2
t_HARQ1 = 64   # Count of repairable symbols for HARQ scheme 1
t_HARQ2 = 128  # Count of repairable symbols for HARQ scheme 2
S = 5         # Delay
b = 9         # Number of bits per symbol
CRC = 32      # Length of CRC code



def calculate_pb(snr):
    pb = 0.5 * math.erfc(math.sqrt(snr/ 2))
    return pb
# Function to calculate block error probability
def block_error_probability(Pb, n):
    return 1 - (1 - Pb) ** n



# Function to calculate throughput for GBN mode
def throughput_GBN(Pb, N, S, b, CRC):
    Pe = block_error_probability(Pb,N )
    return (1 - Pe) / (1 + S * Pe) * (N * b - CRC) / (N * b)

# Function to calculate throughput for HARQ mode
def throughput_HARQ(K, N, t, S, Pb):
    Pe = block_error_probability(Pb, N)
    sum_term = np.sum([np.math.comb(N, i) * (Pb ** i) * ((1 - Pb) ** (N - i)) for i in range(t + 1, N )])
    return (K / N) * (1 - sum_term) / (1 + S * sum_term)

# Generate range of SNR values
SNR_dB = np.arange(0, 19, 0.1)
# for e in SNR_dB:
#     print(e)
  
SNR = 10 ** ((SNR_dB-1.5) / 10)

# Calculate throughput for GBN mode
throughput_GBN_values = [throughput_GBN(calculate_pb(SNR_val), N, S, b, CRC) for SNR_val in SNR]

# Calculate throughput for HARQ modes
throughput_HARQ1_values = [throughput_HARQ(K_HARQ1, N, t_HARQ1, S, 1/(10 ** ((SNR_val+3)/ 10))) for SNR_val in SNR_dB]
# for e in throughput_HARQ1_values:
#     print(e)
throughput_HARQ2_values = [throughput_HARQ(K_HARQ2, N, t_HARQ2, S, 1/(10 ** ((SNR_val+2)/ 10))) for SNR_val in SNR_dB]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(SNR_dB, throughput_GBN_values, linestyle='dashdot', label='Pure GBN', color='black')
plt.plot(SNR_dB, throughput_HARQ1_values, linestyle='dotted', label='HARQ (4599,3477)', color='black')
plt.plot(SNR_dB, throughput_HARQ2_values, linestyle='dashed', label='HARQ (4599,2295)', color='black')
max_throughput_values = [max(x) for x in zip(throughput_GBN_values, throughput_HARQ1_values, throughput_HARQ2_values)]
plt.plot(SNR_dB, max_throughput_values, linestyle='solid', label='ideal throughput', color='black')

#plt.plot(SNR_dB, max(throughput_GBN_values,throughput_HARQ1_values,throughput_HARQ2_values), linestyle='solid', label='ideal throughput', color='black')

plt.title('SNR Throughput Curves')
plt.xlabel('SNR (dB)')
plt.ylabel('Throughput')
plt.grid(False)
plt.legend()
plt.show()