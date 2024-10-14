import wfdb
import matplotlib.pyplot as plt
import numpy as np

# Define the path to the directory containing the data files
path = 'mit-bih-arrhythmia-database-1.0.0/'

# Load the ECG data from the .dat file using the full path (record name without file extension)
record = wfdb.rdrecord(path + '100')  # This loads 100.dat and 100.hea
print(dir(record))
# # Load the annotations from the .atr file
# annotation = wfdb.rdann(path + '100', 'atr')  # This loads the 100.atr file

# # Display the basic information about the record
# print(f"Signal length: {len(record.p_signal)} samples")
# print(f"Sampling frequency: {record.fs} Hz")

# # Display the annotations (types of beats/events and their positions)
# print(f"Annotation symbols: {annotation.symbol}")
# print(f"Annotation positions (in samples): {annotation.sample}")

# # Plot the ECG data along with annotations
# plt.figure(figsize=(10, 4))

# # Plot the first channel of the ECG signal
# plt.plot(record.p_signal[:, 0], label='ECG Channel 1')

# # Mark the annotation positions
# plt.scatter(annotation.sample, record.p_signal[annotation.sample, 0], color='red', marker='o', label='Annotations')

# plt.title('ECG Signal with Annotations')
# plt.xlabel('Sample number')
# plt.ylabel('Amplitude (mV)')
# plt.legend()
# plt.show()
