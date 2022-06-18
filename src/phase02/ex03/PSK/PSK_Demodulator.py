import math
import matplotlib.pyplot as plt


def psk_bit_demodulator(accum_samples, tb, amplitude, frequency, num_samples_per_bit):
    accum_sum = 0
    # plt.plot(accum_samples)
    # plt.show()
    # plt.figure().clear()
    # plt.close()
    # plt.cla()
    # plt.clf()

    for sample_i in range(num_samples_per_bit):
        x = (tb / num_samples_per_bit) * sample_i
        val = -amplitude * math.cos(2 * math.pi * frequency * x)

        accum_sum += val * accum_samples[sample_i]

    if accum_sum / num_samples_per_bit > 0:
        return 1

    return 0


def PSK_Demodulator(data, tb=0.001, amplitude=2, frequency=2000, num_samples_per_bit=10):
    decoded_bits = []

    accum_samples = []
    i = 0
    for sample in data:
        accum_samples.append(sample)

        if i == num_samples_per_bit - 1:
            decoded_bits.append(psk_bit_demodulator(accum_samples, tb, amplitude, frequency, num_samples_per_bit))
            accum_samples = []
            i = 0
        else:
            i += 1

    return decoded_bits


if __name__ == '__main__':
    import PSK_Modulator

    input_bits = [1, 0, 1, 1, 0, 0, 0, 1]
    # data to be plotted
    modulated_signal = PSK_Modulator.PSK_Modulator(input_bits)
    # plotting
    plt.plot(modulated_signal)
    plt.show()

    decoded_bits = PSK_Demodulator(modulated_signal)
    print("input_bits:   "+str(input_bits))
    print("decoded_bits: "+str(decoded_bits))
