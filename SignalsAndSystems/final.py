import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.signal import butter, lfilter, freqz

def play_audio(audio, sampling_rate, mod_vol=1):
    sd.play(audio*mod_vol, sampling_rate)
    sd.wait()

def plot_waveform(signal, sampling_rate):
    time = np.arange(0, len(signal)) / sampling_rate
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(time, signal, linewidth=1)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Magnitude (dB)')
    ax.set_title('Waveform')
    ax.set_xlim([time[0], time[-1]])
    ax.grid()
    plt.show()

def plot_magnitude_spectrum(signal, sampling_frequency, scale='dB',
    signal_type='unfiltered'):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.magnitude_spectrum(signal, 2*np.pi, scale='dB')
    ax.set_title(f'Magnitude spectrum of the {signal_type} signal')
    ax.grid()
    plt.tight_layout()
    plt.show()

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog = False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def plot_lowpass_filter(sampling_rate, sampling_frequency, cutoff, order):
    b, a = butter_lowpass(cutoff, sampling_frequency, order)
    w, h = freqz(b, a, sampling_rate)

    fig,ax = plt.subplots(figsize=(9, 5))
    ax.plot(0.5*sampling_frequency*w/np.pi, np.abs(h), 'b')
    ax.plot(cutoff, 0.5*np.sqrt(2), 'ko')
    ax.axvline(cutoff, color='k')
    ax.set_xlim(0, 0.5*sampling_frequency)
    ax.set_title("Lowpass Filter Frequency Response")
    ax.set_xlabel('Frequency [Hz]')
    ax.grid()
    plt.tight_layout()
    plt.show()

def filter_signal(signal, sampling_rate, sampling_frequency, cutoff, order):
    filtered_signal = butter_lowpass_filter(signal, cutoff, sampling_frequency,
        order)
    time = np.arange(0, len(signal)) / sampling_rate
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(time, signal, label='Unfiltered signal')
    ax.plot(time, filtered_signal, label='Filtered signal')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Magnitude (dB)')
    ax.set_title('Waveform')
    ax.set_xlim([time[0], time[-1]])
    ax.grid()
    plt.legend(loc='best')
    plt.show()
    return filtered_signal

if __name__ == '__main__':
    try:
        signal = pd.read_excel('speech2.xls', header=None, names=['magnitude'])
        signal = signal['magnitude'].values.reshape(-1)

        numbers = list(range(1, 4))
        print(f'Choose a number in {numbers}')
        number = int(input('Number: ').strip())

        while number not in numbers:
            print('-'*30)
            print(f'ERROR: Number selected not in {numbers}')
            number = int(input('Number: ').strip())

        print('-'*30)
        if number == 1:
            print('Waveform plot:')
            plot_waveform(signal, sampling_rate=8000)
            print('Magnitude spectrum plot:')
            plot_magnitude_spectrum(signal, sampling_frequency=2*np.pi,
                scale='dB', signal_type='unfiltered')
            print('Audio:')
            play_audio(signal, sampling_rate=8000, mod_vol=3)

        elif number == 2:
            print('Lowpass filter:')
            plot_lowpass_filter(sampling_rate=8000, sampling_frequency=2*np.pi,
                cutoff=2, order=5)

        elif number == 3:
            print('Waveform plot:')
            filtered_signal = filter_signal(signal, sampling_rate=8000,
                sampling_frequency=2*np.pi, cutoff=2, order=5)
            print('Magnitude spectrum plot:')
            plot_magnitude_spectrum(filtered_signal, sampling_frequency=2*np.pi,
                scale='dB', signal_type='filtered')
            print('Audio:')
            play_audio(filtered_signal, sampling_rate=8000, mod_vol=3)

    except:
        print('Could not find dataset.')
