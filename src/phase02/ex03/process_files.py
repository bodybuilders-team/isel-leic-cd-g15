import os

from NRZU.NRZU_Coder import NRZU_Coder
from NRZU.NRZU_Decoder import NRZU_Decoder
from PSK.PSK_Modulator import PSK_Modulator
from PSK.PSK_Demodulator import PSK_Demodulator
import numpy as np


def iterate_files(directory, callback):
    """
    Iterates through all files in a directory and calls a callback function for each file.

    :param directory: the directory to iterate through
    :param callback: the callback function to call for each file
    """

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        # Checking if it is a file
        if os.path.isfile(f):
            callback(f)


def byte_to_bits(b):
    """
    Converts a byte to a list of bits.

    :param b: the byte to convert
    :return: the list of bits
    """

    bits = []
    for i in range(8):
        bits.append((b >> i) & 1)

    return bits


def bits_to_byte(bits):
    """
    Converts a list of bits to a byte.

    :param bits: the list of bits
    :return: the byte
    """

    byte = 0
    for i in reversed(range(0, 8)):
        bit = bits[i]
        byte = (byte << 1) | bit

    return byte


def chunks(data, n):
    """
    Yield successive n-sized chunks from data.

    :param data: the data to chunk
    :param n: the size of each chunk
    """

    for i in range(0, len(data), n):
        yield data[i:i + n]


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
    # TODO: Comment

    head, tail = os.path.split(file_path)
    print("Testing " + str(tail) + " with " + test_name + " a=" + str(a) + " " + n_type)
    y = a * x + n

    decoded_bits = decoder(y)
    BER = calculate_ber(file_bits, decoded_bits)
    print("BER:" + str(BER))
    decoded_bytes = [bits_to_byte(bits) for bits in chunks(decoded_bits, 8)]
    decoded_files_path = "../decoded_files/"

    if not os.path.exists(decoded_files_path):
        os.mkdir(decoded_files_path)

    with open(decoded_files_path + test_name + "_a=" + str(a) + "_" + n_type + "_" + tail,
              "wb") as f:
        f.write(bytes(decoded_bytes))


def test_file(file_bits, file_path, coder, decoder, test_name):
    # TODO: Comment

    x = coder(file_bits)
    n_mean = 0
    n_scale_vals = [0, 0.5, 1, 2, 4, 8, 16]

    for n_scale in n_scale_vals:
        n = np.random.normal(n_mean, n_scale, len(x))
        process_test(x, 1, n, file_bits, file_path, decoder, "n_scale=" + str(n_scale), test_name)

    # n_vals = [0, 1, 2, 4, 8]
    # for n in n_vals:
    #     process_test(x, -1, [n for _ in range(len(x))], file_bits, file_path, coder, decoder, "n=" + str(n), test_name)


def process_file(file_path):
    # TODO: Comment

    with open(file_path, "rb") as f:
        print("Reading " + file_path + " file...")
        file_bits = []
        while 1:
            # Do stuff with byte.
            byte_s = f.read(1)
            if not byte_s:
                break
            byte = byte_s[0]
            file_bits.extend(byte_to_bits(byte))

        test_file(file_bits, file_path, PSK_Modulator, PSK_Demodulator, "PSK")
        test_file(file_bits, file_path, NRZU_Coder, NRZU_Decoder, "NRZU")


# Testing
if __name__ == '__main__':
    iterate_files("../test_files", process_file)
    print("Ending")
