import math
import matplotlib.pyplot as plt


def PSK_Modulator(bits, tb=0.001, amplitude=2, frequency=2000, num_samples_per_bit=10):
    """
    Modulate the bits into a PSK (Phase-Shift Keying) signal.

    :param bits: the bits to be modulated.
    :param tb: bit period.
    :param amplitude: the amplitude of the modulated signal.
    :param frequency: the frequency of the modulated signal.
    :param num_samples_per_bit: the number of samples per bit.

    :return: the PSK signal
    """

    signal = []

    for bit in bits:
        signal.extend(PSK_Bit_Modulator(bit, tb, amplitude, frequency, num_samples_per_bit))

    return signal


def PSK_Bit_Modulator(bit, tb, amplitude, frequency, num_samples_per_bit):
    """
    Modulate a bit into a PSK (Phase-Shift Keying) signal.

    :param bit: the bit to be modulated.
    :param tb: the bit period.
    :param amplitude: the amplitude of the modulated signal.
    :param frequency: the frequency of the modulated signal.
    :param num_samples_per_bit: the number of samples per bit.

    :return: the PSK signal
    """

    samples = []

    for sample_i in range(num_samples_per_bit):
        x = (tb / num_samples_per_bit) * sample_i
        val = amplitude * math.cos(2 * math.pi * frequency * x)
        if bit == 1:
            val = -val

        samples.append(val)

    return samples


# Test the modulator
if __name__ == '__main__':
    # Data to be plotted
    y = PSK_Modulator([1, 0, 1, 1, 0, 0, 0, 1])

    # Plotting
    plt.plot(y)
    plt.show()
