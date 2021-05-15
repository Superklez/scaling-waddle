import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
from scipy.signal import argrelextrema
from numpy import ndarray

def main(num:int=1):
    def sine_wave(A:float, f:float, t:ndarray):
        return np.sin(2*np.pi*f*t)

    def power_spectrum(Yw:ndarray):
        return 4.7179*np.log10(np.abs(Yw/85.278)**2)

    N = 200
    fs = 200
    df = fs/N
    trange = np.arange(N+1)/fs
    frange = np.arange(-N/2, N/2+1)*df

    wave1 = sine_wave(0.001, 70, trange)
    wave2 = sine_wave(1, 60, trange)
    wave = wave1 + wave2

    if num == 1:
        Yw = fft(wave, N+1)
        Yw = fftshift(Yw)[(N+1)//2:]
        Pw = power_spectrum(Yw)

        ind_freqs = argrelextrema(Pw, np.greater, order=4)
        print('Frequency of the peaks in the Power spectrum:')
        for freq in frange[(N+1)//2:][ind_freqs]:
            print(f'{freq:4.1f} Hz')

        fig, ax = plt.subplots(2, 1, figsize=(12, 8), dpi=200)
        for i, pair in enumerate(zip([wave, Pw],
            ['Sum of Two Sine Waves', 'Corresponding Power Spectrum'])):
            x, title = pair
            if i == 0:
                ax[i].plot(trange, x, zorder=2)
                ax[i].set_xlabel('Time (s)')
                ax[i].set_ylabel('Amplitude')
                ax[i].set_xlim([trange[0], trange[-1]])
            else:
                ax[i].plot(frange[(N+1)//2:], x, zorder=2)
                ax[i].scatter(frange[(N+1)//2:][ind_freqs], Pw[ind_freqs], c='r', zorder=3)
                ax[i].set_xlabel('Frequency (Hz)')
                ax[i].set_ylabel('Power (dB)')
                ax[i].set_xlim([frange[(N+1)//2:][0], frange[(N+1)//2:][-1]])
                ax[i].set_ylim([-140, 20])
            ax[i].set_title(title)
            ax[i].grid(zorder=1)
        plt.tight_layout()
        plt.show()

    elif num == 2:
        letters = ['a', 'b', 'c', 'd']
        print(f'Choose a letter in {letters}')
        letter = input('Letter: ').strip()
        while letter not in letters:
            print('-'*30)
            print(f'ERROR: Letter selected not in {letters}')
            letter = input('Letter: ').strip()

        if letter == 'a':
            window = np.bartlett(len(wave))
            window_function = 'Bartlett Window'
        elif letter == 'b':
            window = np.kaiser(len(wave), 6)
            window_function = 'Kaiser Window'
        elif letter == 'c':
            window = np.hamming(len(wave))
            window_function = 'Hamming Window'
        elif letter == 'd':
            window = np.hanning(len(wave))
            window_function = 'Hanning Window'

        print('-'*30)
        print(f'Window function: {window_function}')

        X = wave * window
        power = power_spectrum(X[1:-1])

        fig, ax = plt.subplots(4, 1, figsize=(12, 17))

        for i, pair in enumerate(zip(
            [wave, window, X, power],
            ['Input Signal', 'Window Function', 'Windowed Signal',
             'Corresponding Power Spectrum of the Windowed Signal'])):
            x, title = pair
            if i == 3:
                ax[i].plot(trange[1:-1], x, zorder=2)
                ax[i].set_ylabel('Power (dB)')
            else:
                ax[i].plot(trange, x, zorder=2)
                ax[i].set_ylabel('Amplitude')
            if i == 1:
                ax[i].set_title(f'{title} ({window_function})')
            else:
                ax[i].set_title(title)
            ax[i].set_xlabel('Time (s)')
            ax[i].set_xlim([trange[0], trange[-1]])
            ax[i].grid(zorder=1)

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    numbers = list(range(1, 3))
    print(f'Choose a number in {numbers}')
    number = int(input('Number: ').strip())

    while number not in numbers:
        print('-'*30)
        print(f'ERROR: Number selected not in {numbers}')
        number = int(input('Number: ').strip())

    print('-'*30)
    main(number)
