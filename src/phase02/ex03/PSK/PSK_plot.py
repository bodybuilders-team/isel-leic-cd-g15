import math
import matplotlib.pyplot as plt
from PSK_Modulator import PSK_Modulator
from PSK_Demodulator import PSK_Demodulator

if __name__ == '__main__':
    input_bits = [1, 0, 1, 1, 0, 0, 0, 1]
    print("input_bits:   " + str(input_bits))

    # data to be plotted
    modulated_signal = PSK_Modulator(input_bits)

    # plotting
    plt.title("Modulated PSK signal")
    plt.plot(modulated_signal)
    plt.show()

    decoded_bits = PSK_Demodulator(modulated_signal)
    print("decoded_bits: " + str(decoded_bits))
