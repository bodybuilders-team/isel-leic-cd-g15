def NRZU_Coder(bits, amplitude=5, num_samples_per_bit=10):
    """
    Encode a list of bits using NRZU (Non-Return-to-Zero Unipolar) coding.

    :param bits: a list of bits to be encoded
    :param amplitude: the amplitude of the waveform
    :param num_samples_per_bit: the number of samples per bit

    :return: a list of bits representing the encoded bits
    """

    output = []

    for bit in bits:
        output.extend(NRZU_Bit_Coder(bit, amplitude, num_samples_per_bit))

    return output


def NRZU_Bit_Coder(bit, amplitude, num_samples_per_bit):
    """
    Encode a single bit using NRZU (Non-Return-to-Zero Unipolar) coding.

    :param bit: the bit to be encoded
    :param amplitude: the amplitude of the waveform
    :param num_samples_per_bit: the number of samples per bit

    :return: the encoded bit
    """

    if bit == 0:
        return [0 for _ in range(num_samples_per_bit)]

    return [amplitude for _ in range(num_samples_per_bit)]


if __name__ == '__main__':
    test_bits = [1, 0, 0, 1]
    print(NRZU_Coder(test_bits))
    import sys
    sys.exit(0)
