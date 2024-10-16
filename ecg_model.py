import wfdb
import numpy as np
import matplotlib.pyplot as plt
import os
# Función para asignar un color específico a cada tipo de anotación
def get_annotation_colors(symbols):
    colors = []
    for symbol in symbols:
        if symbol == 'N':  # Latido normal
            colors.append('orange')
        elif symbol == 'V':  # Latido ventricular prematuro
            colors.append('red')
        elif symbol == 'L':  # Latido de escape ventricular
            colors.append('blue')
        else:  # Otros tipos de anotaciones
            colors.append('green')
    return colors

# Función para plotear el ECG con las anotaciones coloreadas
def plot_ecg_with_annotations(record_path, start_time, duration):
    # Cargar el archivo ECG
    record = wfdb.rdrecord(record_path)
    annotation = wfdb.rdann(record_path, 'atr')
    
    fs = record.fs  # Frecuencia de muestreo
    start_sample = int(start_time * fs)  # Convertir tiempo de inicio a muestras
    end_sample = int((start_time + duration) * fs)  # Convertir duración a muestras

    # Asegurarse de que los límites estén dentro de la señal
    if end_sample > record.sig_len:
        end_sample = record.sig_len
    
    # Obtener la porción de la señal y las anotaciones en el rango solicitado
    ecg_signal = record.p_signal[start_sample:end_sample, 0]
    relevant_annotations = (annotation.sample >= start_sample) & (annotation.sample < end_sample)
    
    annotation_samples = annotation.sample[relevant_annotations] - start_sample
    annotation_symbols = annotation.symbol[relevant_annotations]
    
    # Asignar colores a las anotaciones
    annotation_colors = get_annotation_colors(annotation_symbols)

    # Plotear la señal ECG
    plt.figure(figsize=(15, 6))
    plt.plot(ecg_signal, label='ECG', color='black')

    # Graficar las anotaciones
    plt.scatter(annotation_samples, ecg_signal[annotation_samples], color=annotation_colors, label='Annotations', zorder=5)
    
    # Mostrar etiquetas para cada tipo de anotación
    unique_symbols = np.unique(annotation_symbols)
    for symbol in unique_symbols:
        indices = np.where(annotation_symbols == symbol)[0]
        plt.scatter(annotation_samples[indices], ecg_signal[annotation_samples[indices]], label=f'Annotation {symbol}', color=get_annotation_colors([symbol])[0], zorder=5)
    
    plt.title(f'ECG Signal from {start_time} to {start_time + duration} seconds')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude (mV)')
    plt.legend()
    plt.grid()
    plt.show()

# Definir la ruta del archivo sin extensión
path = 'mit-bih-arrhythmia-database-1.0.0/'
record_name = '100'
path_with_no_extension = path+record_name
record_path = wfdb.rdrecord(path_with_no_extension)


# Llamar a la función para plotear con un rango de tiempo
start_time = 0  # Tiempo de inicio en segundos
duration = 100  # Duración en segundos
plot_ecg_with_annotations(record_path, start_time, duration)
