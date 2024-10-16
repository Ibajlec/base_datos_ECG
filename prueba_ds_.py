import wfdb
import matplotlib.pyplot as plt
import numpy as np
import os

# Define the path to the directory containing the data files
path = 'mit-bih-arrhythmia-database-1.0.0/'
record_name = '100'
ruta = os.path.join(path, record_name)
# Load the ECG data from the .dat file using the full path (record name without file extension)
record = wfdb.rdrecord(ruta)  # This loads 100.dat and 100.hea
print(dir(record))
# # Load the annotations from the .atr file
annotation = wfdb.rdann(ruta, 'atr')  # This loads the 100.atr file

#print(f'los comments son {record.comments}')

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
