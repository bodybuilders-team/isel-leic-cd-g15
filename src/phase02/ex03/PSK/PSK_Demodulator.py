import math
import matplotlib.pyplot as plt


def PSK_Demodulator(data, tb=0.001, amplitude=2, frequency=2000, num_samples_per_bit=10):
    """
    Demodulate the PSK (Phase-Shift Keying) signal.

    :param data: the PSK signal to be demodulated.
    :param tb: the bit period.
    :param amplitude: the amplitude of the modulated signal.
    :param frequency: the frequency of the modulated signal.
    :param num_samples_per_bit: the number of samples per bit.

    :return: the demodulated bits.
    """

    decoded_bits = []

    accum_samples = []
    i = 0
    for sample in data:
        accum_samples.append(sample)

        if i == num_samples_per_bit - 1:
            decoded_bits.append(PSK_Bit_Demodulator(accum_samples, tb, amplitude, frequency, num_samples_per_bit))
            accum_samples = []
            i = 0
        else:
            i += 1

    return decoded_bits


def PSK_Bit_Demodulator(accum_samples, tb, amplitude, frequency, num_samples_per_bit):
    """
    Demodulate a bit from a PSK (Phase-Shift Keying) signal.

    :param accum_samples: the accumulated samples of the bit.
    :param tb: the bit period.
    :param amplitude: the amplitude of the modulated signal.
    :param frequency: the frequency of the modulated signal.
    :param num_samples_per_bit: the number of samples per bit.

    :return: the demodulated bit.
    """

    accum_sum = 0
    # plt.plot(accum_samples)
    # plt.show()
    # plt.figure().clear()
    # plt.close()
    # plt.cla()
    # plt.clf()

    # Accumulates the sum of the product of the input signal and
    # the reference bit 1 signal.
    for sample_i in range(num_samples_per_bit):
        x = (tb / num_samples_per_bit) * sample_i
        val = -amplitude * math.cos(2 * math.pi * frequency * x)

        accum_sum += val * accum_samples[sample_i]

    # If the average of the product of the input signal
    # and the reference bit 1 signal is > 0, then it's a bit 1
    # this is another approach to the integration method
    # of the correlation receiver
    if accum_sum / num_samples_per_bit > 0:
        return 1

    return 0


# Test the demodulator
if __name__ == '__main__':
    import PSK_Modulator

    input_bits = [1, 0, 1, 1, 0, 0, 0, 1]
    # data to be plotted
    modulated_signal = PSK_Modulator.PSK_Modulator(input_bits)
    # plotting
    plt.plot(modulated_signal)
    plt.show()

    demodulated_bits = PSK_Demodulator(modulated_signal)
    print("input_bits:   " + str(input_bits))
    print("decoded_bits: " + str(demodulated_bits))
    import sys
    sys.exit(0)
