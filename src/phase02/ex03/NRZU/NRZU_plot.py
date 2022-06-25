import matplotlib.pyplot as plt
from NRZU_Coder import NRZU_Coder
from NRZU_Decoder import NRZU_Decoder

if __name__ == '__main__':
    input_bits = [1, 0, 1, 1, 0, 0, 0, 1]
    print("input_bits:   " + str(input_bits))

    # Data to be plotted
    modulated_signal = NRZU_Coder(input_bits)

    # Plotting
    plt.title("NRZU Signal")
    plt.plot(modulated_signal)
    plt.show()

    decoded_bits = NRZU_Decoder(modulated_signal)
    print("decoded_bits: " + str(decoded_bits))
    import sys
    sys.exit(0)
