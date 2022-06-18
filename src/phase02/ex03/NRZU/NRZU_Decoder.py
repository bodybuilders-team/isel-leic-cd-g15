# Equivalent to a correlation receiver
def nrzu_bit_decoder(accum_samples, amplitude):
    sample_sum = sum(accum_samples)
    if sample_sum / len(accum_samples) > amplitude / 2:
        return 1

    return 0


def NRZU_Decoder(data, amplitude=5, num_samples_per_bit=10):
    decoded_bits = []

    accum_samples = []
    i = 0
    for sample in data:
        accum_samples.append(sample)
        if i == num_samples_per_bit-1:
            decoded_bits.append(nrzu_bit_decoder(accum_samples, amplitude))
            i = 0
            accum_samples = []
        else:
            i += 1

    return decoded_bits
