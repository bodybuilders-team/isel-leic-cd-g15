def nrzu_bit_coder(bit, amplitude, num_samples_per_bit):
    if bit == 0:
        return [0 for _ in range(num_samples_per_bit)]

    return [amplitude for _ in range(num_samples_per_bit)]


def NRZU_Coder(bits, amplitude=5, num_samples_per_bit=10):
    """
    Encode a list of bits using NRZU (Non-Return-to-Zero Unipolar) coding.

    :param bits: a list of bits to be encoded

    :return: a list of bits representing the encoded bits
    """
    output = []

    for bit in bits:
        output.extend(nrzu_bit_coder(bit, amplitude, num_samples_per_bit))

    return output


if __name__ == '__main__':
    bits = [1, 0, 0, 1]
    print(NRZU_Coder(bits))
