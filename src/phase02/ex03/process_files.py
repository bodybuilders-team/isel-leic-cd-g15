import sys

from NRZU.NRZU_Coder import NRZU_Coder
from NRZU.NRZU_Decoder import NRZU_Decoder
from PSK.PSK_Modulator import PSK_Modulator
from PSK.PSK_Demodulator import PSK_Demodulator
import numpy as np

from src.phase02.utils import *


def calculate_ber(file_bits, decoded_bits):
    """
    Calculates the bit error rate of a file.

    :param file_bits: the bits of the original file
    :param decoded_bits: the bits of the decoded file
    :return: the bit error rate
    """

    num_error_bits = 0
    for i in range(len(file_bits)):
        if file_bits[i] != decoded_bits[i]:
            num_error_bits += 1

    return num_error_bits / len(file_bits)


def process_test(x, a, n, file_bits, file_path, decoder, n_type, test_name):
    """
        Processes a single test on a file
    """

    head, tail = os.path.split(file_path)
    print("Testing " + str(tail) + " with " + test_name + " a=" + str(a) + " " + n_type)
    y = [a * x[i] + n[i] for i in range(len(x))]

    decoded_bits = decoder(y)

    ber = calculate_ber(file_bits, decoded_bits)
    print("BER:" + str(ber))
    decoded_bytes = bits_to_bytes(decoded_bits)
    decoded_files_path = "decoded_files/"

    if not os.path.exists(decoded_files_path):
        os.mkdir(decoded_files_path)

    with open(decoded_files_path + test_name + "_a=" + str(a) + "_" + n_type + "_" + tail,
              "wb") as f:
        f.write(bytes(decoded_bytes))
    sys.stdout.flush()


def test_file(file_bits, file_path, coder, decoder, test_name):
    """
    Tests an entire file
    """

    x = coder(file_bits)
    n_mean = 0
    n_scale_vals = [0, 0.5, 1, 2, 4, 8, 16]

    for n_scale in n_scale_vals:
        n = np.random.normal(n_mean, n_scale, len(x))
        process_test(x, 1, n, file_bits, file_path, decoder, "n_scale=" + str(n_scale), test_name)
        sys.stdout.flush()

    n_vals = [0, 1, 2, 4, 8]
    a_vals = [0.2, 0.4, 0.6, 0.8]
    for a in a_vals:
        for n in n_vals:
            process_test(x, a, [n for _ in range(len(x))], file_bits, file_path, decoder, "n=" + str(n),
                         test_name)


def process_file(file_path):
    """
    Processes PSK and NRZU tests on a file
    """

    with open(file_path, "rb") as f:
        print("Reading " + file_path + " file...")
        file_bits = read_file_bits(f)

        test_file(file_bits, file_path, PSK_Modulator, PSK_Demodulator, "PSK")
        test_file(file_bits, file_path, NRZU_Coder, NRZU_Decoder, "NRZU")


# Testing
if __name__ == '__main__':
    sys.stdout = open('file_processing.log', 'w')
    iterate_files("../../../docs/CD_TestFiles", process_file)

    sys.exit(0)
