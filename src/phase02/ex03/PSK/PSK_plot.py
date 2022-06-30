import matplotlib.pyplot as plt
from PSK_Modulator import PSK_Modulator
from PSK_Demodulator import PSK_Demodulator

if __name__ == '__main__':
    input_bits = [1, 0, 1, 1, 0, 0, 0, 1]
    print("input_bits:   " + str(input_bits))

    # Data to be plotted
    modulated_signal = PSK_Modulator(input_bits)

    # Plotting
    plt.title("Modulated PSK signal")
    plt.xlabel("Sample per 10^-1 ms")
    plt.ylabel("Amplitude")
    plt.plot(modulated_signal)
    plt.show()

    decoded_bits = PSK_Demodulator(modulated_signal)
    print("decoded_bits: " + str(decoded_bits))
    import sys
    sys.exit(0)
