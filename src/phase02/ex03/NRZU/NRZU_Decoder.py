def NRZU_Decoder(data, amplitude=5, num_samples_per_bit=10):
    """
    Decodes a stream of NRZU encoded data.

    :param data: data to decode
    :param amplitude: the amplitude of the signal
    :param num_samples_per_bit: the number of samples per bit

    :return: the decoded data
    """

    decoded_bits = []

    accum_samples = []
    i = 0
    for sample in data:
        accum_samples.append(sample)
        if i == num_samples_per_bit - 1:
            decoded_bits.append(NRZU_Bit_Decoder(accum_samples, amplitude))
            i = 0
            accum_samples = []
        else:
            i += 1

    return decoded_bits


def NRZU_Bit_Decoder(accum_samples, amplitude):
    """
    Decodes a single bit of NRZU encoded data.
    Equivalent to a correlation receiver.

    :param accum_samples: the accumulated samples
    :param amplitude: the amplitude of the signal

    :return: the decoded bit
    """

    sample_sum = sum(accum_samples)
    if sample_sum / len(accum_samples) > amplitude / 2:
        return 1

    return 0
