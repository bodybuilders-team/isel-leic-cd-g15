import math
import matplotlib.pyplot as plt


def psk(bit, tb, amplitude, frequency, num_samples_per_bit):
    samples = []

    for sample_i in range(num_samples_per_bit):
        x = (tb / num_samples_per_bit) * sample_i
        val = amplitude * math.cos(2 * math.pi * frequency * x)
        if bit == 1:
            val = -val

        samples.append(val)

    return samples


def PSK_Modulator(bits, tb=0.001, amplitude=2, frequency=2000, num_samples_per_bit=10):
    """
    Modulate the bits into a PSK (Phase-Shift Keying) signal.

    :param bits: the bits to be modulated.«

    :return: the PSK signal
    """

    signal = []

    for bit in bits:
        signal.extend(psk(bit, tb, amplitude, frequency, num_samples_per_bit))

    return signal


if __name__ == '__main__':

    # data to be plotted
    y = PSK_Modulator([1, 0, 1, 1, 0, 0, 0, 1])

    # plotting
    plt.plot(y)
    plt.show()
